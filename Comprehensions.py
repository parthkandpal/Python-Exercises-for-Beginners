nums=[1,2,3,4,5,6,7,8,9]

#I want 'n' for each 'n' in nums
mylist=[]
for n in nums:
    mylist.append(n)
print(mylist)

#list Comprehension
mylist=[n for n in nums]
print(mylist)

#I want 'n*n' for each 'n' in nums
mylist=[]
for n in nums:
    mylist.append(n*n)
print(mylist)


#list Comprehension
mylist=[]
mylist=[n*n for n in nums]
print(mylist)

#Using a map and lambda
mylist=[]
mylist=map(lambda n: n*n, nums)
print(mylist)    #gives output as <map object at 0x03976690>
for i in mylist:
    print(i)

#I want 'n' for each 'n' in nums if 'n' is even
mylist=[]
for n in nums:
    if n%2==0:
        mylist.append(n)
print(mylist)

#list Comprehension

mylist=[n for n in nums if n%2==0]
print(mylist)


#I want a (letter,num) pair for each letters in 'abcd' and each number '1234'
mylist=[]
for letter in "abcd":
    for num in range(4):
        mylist.append((letter,num))
print(mylist)

#list Comprehension

mylist=[(letter,num) for letter in "abcd"  for num in range(4) ]
print(mylist)

#Dictionary Comprehensions

names=['john','Suraj','Hari','Parth','Prasobh']
majors=['maths','arts','physics', 'Business', 'Computer']
print(zip(names,majors)) #<zip object at 0x00809620>

#I want a dict{'name':'major} for each name,major in zip(names,majors)
dict={}
for name,major  in zip(names,majors):
    dict[name]=major
print(dict)


mydict={name:major for name,major in zip(names,majors)}
print(mydict)

#Set
nums=[1,1,2,2,3,3,4,5,6,6,7,7,8,8,8,9]
set=set()
for num in nums:
    set.add(num)
print(set)

#Set comprehension
set ={n for n in nums}
print(set)


#generator

# def square(nums):
#     for i in nums:
#         yield i*i
list=[3,4,5]

for num in square(list):
   print(num)

#generator  comprehension

mygen=[n*n for n in list]
print(mygen)




