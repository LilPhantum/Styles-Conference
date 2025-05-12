print("Provide Username")
userna = input()
print("Provide Password")
pwd = input()

username ="Wakili@1234"
password = "12345"
def validate_username(username , password):
    if username == userna and password == pwd:
        print("Hello Wakili")
    else:
        print("Wrong Credentials")
validate_username(username  , password)