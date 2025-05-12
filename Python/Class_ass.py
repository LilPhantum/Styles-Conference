
#Assignment 1
class student:
    def __init__(self,name,course,matric_no,phone_no,):
        self.name = name
        self.course = course
        self.matric_no = matric_no
        self.phone_no = phone_no

    def students_info(self):
        print("1. Students Name:",self.name, "Students Matric number:",self.matric_no, "Students Course:",self.course, "Students Phone Number:",self.phone_no)
x = student("Muazu","Computer Science","22/03CMP039",+2349010204299)
x.students_info()



#Assignment 2
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def vehicle_info(self):
        print("Vehicle Brand:", self.brand, "Model:", self.model)

class Car(Vehicle):
    def __init__(self, brand, model, top_speed, horse_power, color):
        super().__init__(brand, model)  # Inherit brand and model from Vehicle
        self.top_speed = top_speed
        self.horse_power = horse_power
        self.color = color

    def cars_statistics(self):
        print("2. Car brand:", self.brand, 
              "Car model:", self.model, 
              "Car Topspeed:", self.top_speed, 
              "Car horsepower:", self.horse_power, 
              "Car color:", self.color)

x = Car("Ferrari", "812 Superfast", "221 mph", "812 hp", "Red")
x.cars_statistics()



#Assignment 3
class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def book_info(self):
        print("3. Book Title:", self.title, "Author:", self.author, "Pages:", self.pages, "Genre:", self.genre)

x = Book("2010", "Muazu Wakili", 328, "Software Development")
x.book_info()


#Assignment 4
class BankAccount:
    def __init__(self, account_holder, balance, account_number):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = account_number

    def account_info(self):
        print("4. Account Holder:", self.account_holder, "Account Balance:", self.balance, "Account Number:", self.account_number)

x = BankAccount("Muazu Wakili", 5000.75, "123456789")
x.account_info()


#Assignment 
class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)

class Teacher(Person):
    def __init__(self, name, subject, years_of_experience, school):
        super().__init__(name)  # Inheriting from Person
        self.subject = subject
        self.years_of_experience = years_of_experience
        self.school = school

    def teacher_info(self):
        print("5. Teacher Name:", self.name, 
              "Subject:", self.subject, 
              "Years of Experience:", self.years_of_experience, 
              "School:", self.school)

x = Teacher("Engr. Tijjani", "Computer Science", 10, "Alhikmah")
x.teacher_info()



#Assignment 6
class Dog:
    def __init__(self, breed, age, color, size):
        self.breed = breed
        self.age = age
        self.color = color
        self.size = size

    def dog_info(self):
        print("6. Dog Breed:", self.breed, "Age:", self.age, "Color:", self.color, "Size:", self.size)

x = Dog("Golden Retriever", 3, "Golden", "Large")
x.dog_info()


#Assignment 7
class Movie:
    def __init__(self, title, director, release_year, genre):
        self.title = title
        self.director = director
        self.release_year = release_year
        self.genre = genre

    def movie_info(self):
        print("7. Movie Title:", self.title, "Director:", self.director, "Release Year:", self.release_year, "Genre:", self.genre)

x = Movie("Inception", "Christopher Nolan", 2010, "Sci-Fi")
x.movie_info()


#Assignment 8
class MobilePhone:
    def __init__(self, brand, model, price, color):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color

    def phone_info(self):
        print("8. Phone Brand:", self.brand, "Model:", self.model, "Price:", self.price, "Color:", self.color)

x = MobilePhone("Apple", "iPhone 13", 999, "Blue")
x.phone_info()


#Assignment 9
class Computer:
    def __init__(self, brand, processor, ram, storage):
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def computer_info(self):
        print("9. Computer Brand:", self.brand, "Processor:", self.processor, "RAM:", self.ram, "Storage:", self.storage)

x = Computer("Lenovo", "AMD Ryzen 5", "8GB", "256GB SSD")
x.computer_info()


#Assignment 10
class Product:
    def __init__(self, name, price, category, stock_quantity):
        self.name = name
        self.price = price
        self.category = category
        self.stock_quantity = stock_quantity

    def product_info(self):
        print("10. Product Name:", self.name, "Price:", self.price, "Category:", self.category, "Stock Quantity:", self.stock_quantity)

x = Product("Laptop", 1200, "Electronics", 50)
x.product_info()
