

def square(nums):
    for i in nums:
        yield i*i
list=[3,4,5]

squ=square(list)


print(next(squ))
print(next(squ))
print(next(squ))

for num in squ:
   print(num)

#Benefits of Generators

#List vs Generator

import random
import time

names=['john','Suraj','Hari','Parth','Prasobh']
majors=['maths','arts','physics', 'Business', 'Computer']



def people_list(num_people):
    result=[]
    for i in range(num_people):
        person= {
            'id':i,
            'name':random.choice(names),
            'major':random.choice(majors)

        }
        result.append(person)
    return result



def people_generator(num_people):

    for i in range(num_people):
        person= {
            'id':i,
            'name':random.choice(names),
            'major':random.choice(majors)

        }
        yield person

t1=time.clock()
people=people_list(1000000)
t2=time.clock()

print("List took time of", t2-t1 , "seconds")

t1=time.clock()
people=people_generator(1000000)
t2=time.clock()

print("Generator took time of", t2-t1 , "seconds")
