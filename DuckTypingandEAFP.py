class Duck:
    def quack(self):
        print("Quack!Quack!")

    def fly(self):
        print("flap!flap!")


class person:
    def quack(self):
        print("I m Quacking like a duck")

    def fly(self):
        print("I m flapping my arms")


def quack_and_fly(thing):
    #Non Duck type and Non Pythonic
    if isinstance(thing,Duck):
        thing.quack()
        thing.fly()
    else:
        print("This has to be a duck")

    print()

d=Duck()

quack_and_fly(d)

p=person()

quack_and_fly(p)

def quack_and_fly(thing):
    #Duck type and Pythonic

    thing.quack()
    thing.fly()


    print()

d=Duck()

quack_and_fly(d)

p=person()

quack_and_fly(p)



#Lbyl-Look before you leap
#EAFP Easier to ask forgiveness than permission

def quack_and_fly(thing):
    #LBYL and Non Pythonic
    if hasattr(thing,'quack'):
        if callable(thing.quack):
            thing.quack()
    else:
        print("This has to be a duck")

    print()

d=Duck()

quack_and_fly(d)

p=person()

quack_and_fly(p)

def quack_and_fly(thing):
    #EAFP and Pythonic
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

    print()

d=Duck()

quack_and_fly(d)

p=person()

quack_and_fly(p)


person={'name':'parth','age':'22','job':'Python Developer'}

#LBYL

if 'name' in person and 'age' in person and 'job' in person:
    print('I am {name} . I\'m {age} years old. I\'m a {job}'.format(**person))
else:
    print('missing some keys')

#EAFP

try:
    print('I am {name} . I\'m {age} years old. I\'m a {job}'.format(**person))
except KeyError as e:
    print("Missing {} key".format(e))




