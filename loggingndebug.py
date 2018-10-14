import logging

'''
DEBUG

logging.debug()

The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.

INFO

logging.info()

Used to record information on general events in your program or confirm that things are working at their point in the program.

WARNING

logging.warning()

Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.

ERROR

logging.error()

Used to record an error that caused the program to fail to do something.

CRITICAL

logging.critical()

The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.'''

logging.basicConfig(level=logging.DEBUG,filename='test.log',format='%(asctime)s:%(levelname)s:%(message)s')

# logging.debug('Start of program')

# def factorial(n):
#     logging.debug('Start of factorial(%s)' % (n))
#     total = 1
#     for i in range(n + 1):
#         total *= i
#         logging.debug('i is ' + str(i) + ', total is ' + str(total))
#     logging.debug('End of factorial(%s)' % (n))
#     return total
#
# print(factorial(5))
# logging.debug('End of program')
#
#
# def factorial(n):
#     logging.debug('Start of factorial(%s)' % (n))
#     total = 1
#     for i in range(1,n + 1):
#         total *= i
#         logging.debug('i is ' + str(i) + ', total is ' + str(total))
#     logging.debug('End of factorial(%s)' % (n))
#     return total
#
# print(factorial(5))
# logging.debug('End of program')




def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y




num1=10
num2=5

add_result=add(num1,num2)

logging.debug('Add {} + {} = {}'.format(num1,num2,add_result))

subtract_result=subtract(num1,num2)

logging.debug('Subtract {} - {} = {}'.format(num1,num2,subtract_result))

multiply_result=multiply(num1,num2)

logging.debug('Multiply {} * {} = {}'.format(num1,num2,multiply_result))

divide_result=divide(num1,num2)

logging.warning('Divide {} + {} = {}'.format(num1,num2,divide_result))


add_result=add(num1,num2)

logging.warning('Add {} + {} = {}'.format(num1,num2,add_result))

subtract_result=subtract(num1,num2)

logging.warning('subtract {} - {} = {}'.format(num1,num2,subtract_result))

multiply_result=multiply(num1,num2)

logging.warning('Multiply {} * {} = {}'.format(num1,num2,multiply_result))

divide_result=divide(num1,num2)

logging.warning('Divide {} + {} = {}'.format(num1,num2,divide_result))

