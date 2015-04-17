var connString = 'postgres://pdwmzbxpyvusli:pQiDqSFevqvLw6HurnZKthWZHT@ec2-107-20-244-236.compute-1.amazonaws.com:5432/d3gphhtnujhnad?ssl=true&sslfactory=org.postgresql.ssl.NonValidatingFactory'

var pg = require('pg');

var express = require('express');

var app = express();

var fs = require('fs')

var router = express.Router();

var http = require('http')

var path = require('path');

app.use(express.logger());

app.configure(function(){
  app.set('port', process.env.PORT || 3000);
  app.set('views', __dirname + '/views');
  app.set('view engine', 'jade');
  app.use(express.favicon());
  app.use(express.logger('dev'));
  app.use(express.bodyParser());
  app.use(express.methodOverride());
  app.use(express.static(path.join(__dirname, 'public')));
});

app.configure('development', function(){
  app.use(express.errorHandler());
});

app.post('/test', function(req, res) {

    var newuser = req.body.newuser;
    var newpass = req.body.newpass;
    console.log("post received: %s %s", newuser, newpass);
});

app.get('/', function(request, response) {

        pg.connect(connString, function(err, client, done) {
                if(err) response.send("Could not connect to DB: " + err);
                client.query('SELECT * FROM users ', function(err, result) {
                        done();
                        if(err) return response.send(err);
                        response.send(result.rows);
                });
        });
});

app.get('/form', function(req, res) {
    fs.readFile('./sign_up.html', function(error, content) {
        if (error) {
            res.writeHead(500);
            res.end();
        }
        else {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.end(content, 'utf-8');
        }
    });
});




app.post('/signup', function(req, res) {
    // Grab data from http request

    var results = [];
    var newuser = req.body.newuser;
    var newpass = req.body.newpass;
    
    // Get a Postgres client from the connection pool
    pg.connect(connString, function(err, client, done) {

        // SQL Query > Insert Data
        client.query("INSERT INTO users(username, password) values($1, $2)", [newuser, newpass]);

        // SQL Query > Select Data
        var query = client.query("SELECT * FROM users");

        // Stream results back one row at a time
        query.on('row', function(row) {
            results.push(row);
        });

        // After all data is returned, close connection and return results
        query.on('end', function() {
            client.end();
            return res.json(results);
        });

        // Handle Errors
        if(err) {
          console.log(err);
        }

    });
});



var port = process.env.PORT || 5000;
app.listen(port, function() {
        console.log("Listening on " + port);
});
