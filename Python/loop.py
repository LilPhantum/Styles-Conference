#Loop Through List
fruits = ["pineapple", "watermelon", "Mango"]
for t in fruits: #(for) loop is used to iteratre elements of a sequence/list
    print(t)

#Loop Through Numbers
for b in range(1 , 11):
    print(b)

#Loop Through String
for letter in "wellcome":
    print(letter)


#WHILE LOOP(YLOOP)
#yloop repeats a block as long as a condition stays TRUE

#Basic Loop
x = 2
while x <= 8:
    print(x)
    x += 1 #depends on inputed no

print('///////////////')

#Countdown
count = 5
while count > 0:
    print(count)
    count -= 1 #decrement

#Break Statement  
# break is used to immediately exit the loop
for num in range(1, 10):
    if num == 5:
        break
    print(num)

print('***break***')

#CONTINUE STATEMENT
#continue tells Python to skip the rest of the code inside the loop 
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

cars=["Toyota", "Tesla", "Hilux Truck", "Ford"]
for model in cars:
    if model == "Tesla":
        print("I wish to have Tesla one day")
    elif model == "Toyota":
        print("Toyota is overrated")
    elif model == "Hilux Truck":
        print("Hilux Trucks are expensive ")
    else:
        print("I am fine with any car")    
        