print("Welcome to Facebook\nEnter (NEXT) to continue")

while True:
    next = input().upper()
    if next == "NEXT":
        print("\nEnter First name")
        break
    else:
        print("\nPlease, enter (NEXT) to continue")

first_name = input().upper()
print ( "Enter Surname" )
surname = input().upper()
print ( "\nWelcome {} {}\nPlease, Enter (NEXT) to continue".format ( surname, first_name ) ) #how to add(.upper)
while True:
    next = input().upper()
    if next == "NEXT":
        print("\nCreate Username")
        break
    else:
        print("\nPlease, enter (NEXT) to continue")


user = input ().lower()
print ( "Are you sure you want '{}' as your username?\na = YES\nb = NO".format (user) )
reply = input ().lower ()
if reply == "a" :
    print ( "\nCreate New Password" )
elif reply == "b" :
    print ( "\nEnter desired username" ) #how to return to reply input when b is selected


pwd1 = input ()
print ( "Please, re-enter password" )
while True :    
    pwd2 = input ()
    if pwd1 == pwd2 :
        print ( "\nPassword Created Sucessfully\nPlease, Enter (NEXT) to continue" )
        break
    else :
        print ( "\nPassword doesnt match, please try again" )

while True:
    next = input().upper()
    if next == "NEXT":
        print("\nEnter Username to sign in")
        break
    else:
        print("\nPlease, enter (NEXT) to continue")

user = input ()
print ( "\nEnter password" )
pwd2 = input ()

username = user
password = pwd2
def validate_username(username , password):    
    if username == user and password == pwd2 :
        print("\nHello {} {}\nWellcome to Facebook\nPlease, enter (HOME) to continue" .format(surname, first_name))
    else:
        print("\nPlease, enter correct username or password")
validate_username(username  , password)


while True :
    hme = input ().upper ()
    if hme == "HOME" :
        print ( "\nEnter any number to continue\n1 Manamge Account.\n2 Settings.\n3 Privacy.\n4 Security.\n5 Report a problem.\n6 log out." )
        break 
    else:
        print ("\nPlease, Enter (next) to continue")