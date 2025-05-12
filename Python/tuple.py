states=("bauchi","yobe")#tuple cannot be modified, used in security applications
print(states)
first_state,second_state=states #packing 
print("{} is for PDP".format(first_state)) #unpacking
print("{} is for young Emir".format(second_state)) #unpacking


#Python Dictionary

scores={
    "john" : 57,
    "mike" : 92,
}
print(scores)
scores["john"] = 75
print(scores)


#

a=23
b=2
c=a/b
d=a//b
e=a%23
print(c,d,e)

#Comparism Operators
y=0
x=3
if x==y:
    print(y)
elif y != x:
    print(True)
else:
    print(False)

#Logical 
print(" put the value for x :")
guest1 = int(input())
print(" put the value for y in form of name:")
guest2 = int(input())
x = 5 
y = 7
if guest1 == x and guest2 == y :
    print("WOW, you win the game!")
elif guest1 == x or guest2 == y :
    print("OOPS, you just guessed one of the answer")
#elif  guest1 in y return True #or guest2 in x :
    #print("OHH, you mixed up the game")
else :
    print("you failed, game over")
guess = [1,2,3,4,5,6,7]
if y in guess:
    print("match number")
else :
    print("no match number")

#Assignment Operators

