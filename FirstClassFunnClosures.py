'''
first-class functions
In computer science, a programming language is said to have first-class functions if it treats functions as first-class citizens.
This means the language supports passing functions as arguments to other functions, returning them as the values from other functions,
 and assigning them to variables or storing them in data structures.'''

'''higher-order function 
a higher-order function is a function that does at least one of the following:

takes one or more functions as arguments (i.e. procedural parameters),
returns a function as its result.


'''

def square(x):
    return x*x
f= square

print(square)
print(f)

print(f(5))

#passing a function as an argument to another function

def square(x):
    return x*x
def cube(x):
    return x*x*x


def my_map(func,arg):
    result=[]
    for i in arg:
        result.append(func(i))
    return result

squares=my_map(square,[1,2,3,4,5])
print(squares)

cubes=my_map(cube,[1,2,3,4,5])
print(cubes)





def logger(msg):
    def log_message():
        print('log:',msg)
    return log_message


log_hi=logger("Hi")
log_hi()





def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))
    return wrap_text


print_h1=html_tag("h1")
print(print_h1)

print_h1("Hi, This is a h1")
print_h1("Hi, This is a another h1")

print_para=html_tag("p")
print_para("This is a paragraph")

'''Closures
In programming languages, a closure (also lexical closure or function closure) is a technique for implementing lexically scoped name binding in a language with first-class functions.
 Operationally, a closure is a record storing a function[a] together with an environment.
  The environment is a mapping associating each free variable of the function (variables that are used locally, but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created.
   A closure—unlike a plain function—allows the function to access those captured variables through the closure's copies of their values or references, even when the function is invoked outside their scope.
'''



def outer_fun(msg):
    message=msg
    def inner_fun():
        print(message)
    return inner_fun

hi_msg=outer_fun("hi")
print(hi_msg)
hi_msg()
hello_msg=outer_fun("Hello")
hello_msg()


import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

def logger(fun):
    def log_fun(*args):
        logging.info('Running {} with arguments {}'.format(fun,args))
        print(fun(*args))
    return log_fun

add_log=logger(add)
print(add_log)

add_log(1,2)







