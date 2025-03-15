class Person:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstaw_sie(self):
        return f"Mam na imię {self.imie} i mam {self.wiek} lat."

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

class Student:
    studenci = {}

    def __init__(self, name, grade=None):
        self.name = name
        self.grade = grade
        Student.studenci[name] = []

    @classmethod
    def add_student(cls, name):
        if name not in cls.studenci:
            cls.studenci[name] = []

    @classmethod
    def add_grade(cls, name, grade):
        if name in cls.studenci:
            cls.studenci[name].append(grade)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        self.price -= self.price * percent / 100

class User:
    users = {}

    @classmethod
    def register(cls, username, password):
        if username not in cls.users:
            cls.users[username] = password
            return True
        return False

    @classmethod
    def login(cls, username, password):
        return cls.users.get(username) == password
