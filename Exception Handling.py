def div42by(number):
    try:
        print(42/number)
    except ZeroDivisionError:
        print("division by zero")

div42by(0)
div42by(1)
div42by(2)
div42by(3)



# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)

#Raising Exceptions

def boxPrint(symbol, width, height):
    if len(symbol) != 1:

        raise Exception('Symbol must be a single character string.')
    if width <= 2:
     raise Exception('Width must be greater than 2.')
    if height <= 2:
            raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
            print(symbol + (' ' * (width - 2)) + symbol)
            print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))


#Getting the Traceback as a String
import traceback
try:
         raise Exception('This is the error message.')
except:
         errorFile = open('errorInfo.txt', 'w')
         errorFile.write(traceback.format_exc())
         errorFile.close()
         print('The traceback info was written to errorInfo.txt.')

#Assertions

'''In code, an assert statement consists of the following:

The assert keyword

A condition (that is, an expression that evaluates to True or False)

A comma

A string to display when the condition is False'''
podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'


#Using Assertion in traffic light simulation
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)

switchLights(market_2nd)





