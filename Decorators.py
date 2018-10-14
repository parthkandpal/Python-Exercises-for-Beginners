
'''
Decorators
A decorator is any callable Python object that is used to modify a function, method or class definition.
A decorator is passed the original object being defined and returns a modified object, which is then bound to the name in the definition.
Python decorators were inspired in part by Java annotations, and have a similar syntax; the decorator syntax is pure syntactic sugar, using @ as the keyword:
'''

def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

# def display():
#     print("display function ran")
#
# decorator_display = decorator_function(display)
#
# decorator_display()

#Decorating our function allows us to easily add functionality to existing function

@decorator_function    #@decorator_function here   is used for display is equals to decorator_function(display)
def display():
    print("display function ran")

display()

@decorator_function        #@decorator_function here   is used for display_info is equals to decorator_function(display_info)
def displayinfo(name,age):
    print("display info ran with arguments {}  {}".format(name,age))

displayinfo("parth",22)

#Decorator Class

class decorator_class(object):

    def __init__(self,original_function):
        self.original_function=original_function

    def __call__(self, *args, **kwargs):
        print("dunder call method executed this before {}".format(self.original_function.__name__))
        return self.original_function(*args,**kwargs)

@decorator_class
def display():
    print("display function ran")

display()

@decorator_class
def displayinfo(name,age):
    print("display info ran with arguments {}  {}".format(name,age))

displayinfo("parth",22)

# logging and time with decorators
from functools import wraps

def my_logger(original_func):
    import logging
    logging.basicConfig(level=logging.INFO,filename='{}.log'.format(original_func.__name__),format='%(asctime)s-%(message)s')

    @wraps(original_func)
    def wrapper_fun(*args,**kwargs):
        logging.info("Ran with args {} and kwargs  {}".format(args,kwargs))
        return original_func(*args,**kwargs)
    return wrapper_fun

def my_timer(original_func):
    import time

    @wraps(original_func)
    def wrapper_fun(*args, **kwargs):
        t1=time.time()

        result=original_func(*args,**kwargs)

        t2=time.time()
        t3=t2-t1

        print("It took {} time to run the {}".format(t3,original_func.__name__))
        return result
    return wrapper_fun

# @my_logger
# def display():
#     print("display function ran")
#
# display()

import time
@my_logger
@my_timer                #my_logger(my_time(displayinfo))
def displayinfo(name,age):
    time.sleep(1)
    print("display info ran with arguments {}  {}".format(name,age))

displayinfo("parth",22)

