def main_func():
    while True:
        print("Main Menu")
        print("1. Sign up")
        print("2. Sign in")
        print("3. Exit")
        choice = input("Select you choice: ")
        if choice == "1":
            sign_up()
        elif choice == "2" :
            sign_in()
        elif choice == "3" :
            print("Exiting...")
            break
        else:
            print("Invalid choice, please choose again.")        



def sign_up():
    print("You selected option one")
    first_name = input("Enter your first name: ").upper()  
    surname = input("Enter your Surname: ").upper()
    print ( "\nWelcome {} {}".format ( surname, first_name ) ) #how to add(.upper)
    while True:
        next = input("Please, Enter (NEXT) to continue: ").upper()
        if next == "NEXT":
            user = input("Create Username: ").lower()
            break
        else:
            print("\nPlease, enter (NEXT) to continue")
    print ( "Are you sure you want '{}' as your username?\na = YES\nb = NO".format (user) )
    reply = input ().lower ()
    if reply == "a" :
        print ( "\nCreate New Password" )
    elif reply == "b" :
        print ( "\nEnter desired username" ) #how to return to reply input when b is selected
    pwd1 = input ()
    while True :    
        pwd2 = input ("Please, re-enter password: ")
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

    


def sign_in():
    print("You selected option two")
    user = input ("\nEnter Username: ")
    pwd2 = input ("Enter password: ")
    print("Account Created Successfully!\nPlease return to Main Menu ")
    def validate_username(username , password):    
        if username == user and password == pwd2 :
            print("\nHello {} {}\nWellcome to Facebook\nPlease, enter (HOME) to continue")#.format(first_name, surname))
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



if __name__ == "__main__" :
    main_func()