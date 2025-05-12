print('what is your name')
MyName = input()
print('it is good to meet you, {}'.format(MyName))
print('what was your score?')
score = input()
score1=int(float(score))
if score1>50:
    print("Great job!")
else:
    print('sorry, you are not qualified, {}'.format(MyName))
print(type(score))
animal="ram"
legs=4
print("{} has {} legs".format(animal,legs))
salary=178251.7476
name="Muazu"
print("{} has ${:.2f} monthly".format(name,salary))