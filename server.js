var connString = 'postgres://pdwmzbxpyvusli:pQiDqSFevqvLw6HurnZKthWZHT@ec2-107-20-244-236.compute-1.amazonaws.com:5432/d3gphhtnujhnad?ssl=true&sslfactory=org.postgresql.ssl.NonValidatingFactory'

var pg = require('pg');
var express = require("express");
var app = express();
app.use(express.logger());

app.get('/', function(request, response) {

        pg.connect(connString, function(err, client, done) {
                if(err) response.send("Could not connect to DB: " + err);
                client.query('SELECT * FROM opshun_test ', function(err, result) {
                        done();
                        if(err) return response.send(err);
                        response.send(result.rows);
                });
        });
});

var port = process.env.PORT || 5000;
app.listen(port, function() {
        console.log("Listening on " + port);
});
