def prime_fnc(numbers):
    x = ""
    for number in numbers:
        if number %2 == 0 :
            x = x + "{} is a prime\n".format(number)
        else:
            x = x + "{} is not a prime\n".format(number)
    return x 
print(prime_fnc([1, 2,3,4,5,6,7,8,9,10,11,12,13,14,15,20,25,30,50,88,87]))