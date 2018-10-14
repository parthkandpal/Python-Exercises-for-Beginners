import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')


def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')



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



import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -%(levelname)s - %(message)s')
logging.debug('Some debugging details.')

logging.info('The logging module is working.')

logging.warning('An error message is about to be logged.')

logging.error('An error has occurred.')

logging.critical('The program is unable to recover!')


#logging.disable() function disables these so that you don’t have to go into your program and remove all the logging calls by hand.
#  You simply pass logging.disable() a logging level, and it will suppress all log messages at that level or lower.
#So if you want to disable logging entirely, just add logging.disable(logging.CRITICAL) to your program

logging.disable(logging.CRITICAL)