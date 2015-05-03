import random

#FUNCTION TO PRINT SUGGESTION
def generateSuggestion(data):

  dataCombined = [0]
  dataCombined.remove(0)

  i = 0
  while i < len(data):
     if(i == 0):
       dataCombined.extend([data[i]])
     else:
       dataCombined.extend([data[i] + dataCombined[i-1]])
     i += 1
  else:
     print dataCombined

  done = False; #used to control getting out of loop
  dataLength = dataCombined[len(dataCombined) - 1]; #adds up the ratings of the data
  firstValue = 1; #initial value
  lastValue = 0; #last value to compare
  generatedNumber = 0; #the generated suggested number
  selected = 0; #return value (index of option to return to user)

  #print dataLength
  #print "dataLength: %r" % dataLength
  
  #randomly generate number
  generatedNumber = random.randrange(1, dataLength+1)
  
  #print generated number
  #print "generatedNumber: %r" % generatedNumber

  j = 0;
 
  #loops through data and prints closest result
  while j < len(data) and not done:

    if(j == 0):
      lastValue = data[j]
    elif(j > 0):
      lastValue += data[j-1]   
    if((firstValue <= generatedNumber) and (generatedNumber <= dataCombined[j])):
      selected = j
      done = True

    if(j == 0):
      firstValue = data[j] + 1
    else:
      firstValue += data[j]

    j += 1
  
  return selected

#MAIN COMMAND
testData = [7, 4, 3] #data that's been looked at/changed
def wrapper(lst):
  return generateSuggestion(lst)

