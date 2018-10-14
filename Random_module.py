import random
val=random.random()
print(val)

#floating point value b/w 1 and 10

val=random.uniform(1,10)
print(val)

#integer value b/w 1 and 10
val=random.randint(1,10)
print(val)

#random choice

greetings=['Hi','Hello','Hey']

greet=random.choice(greetings)

print(greet, "Parth")

#multiple random choices

color=['red','green','blue','white']
choice_color=random.choices(color,k=60)
print(choice_color)

choice_color=random.choices(color,weights=[18,18,20,4],k=60)  #weight define chances red:18 chances out of 60, blue:20 chances out of 60, white 4 chances
print(choice_color)

# red_count=0
# green_count=0
# white_count=0
# blue_count=0


# for color in choice_color:
#     if color =='red':
#         red_count +=1
#     elif color =='green':
#         green_count +=1
#     elif color =='blue':
#         blue_count +=1
#     else:
#         white_count +=1
#
# print("red= {} green= {} blue={} white={} ".format(red_count,green_count,blue_count,white_count))

deck=list(range(1,53))
print(deck)

random.shuffle(deck)
print(deck)

hand=random.sample(deck,k=5)
print(hand)










