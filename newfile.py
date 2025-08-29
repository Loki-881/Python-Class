#Create a class Student that takes name and marks in 5 subjects. 
#Add a method to calculate total and average marks and percentage(Assuming each subject is out of 100).
"""
class Student:
    def __init__(self,name,s1,s2,s3,s4,s5):
        self.name = name
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        
    def totalmarks(self):
        total = float(self.s1+self.s2+self.s3+self.s4+self.s5)
        print("Total marks = ",total)
        
    def averagemarks(self):
        average = float((self.s1+self.s2+self.s3+self.s4+self.s5) / 5)
        print("Average marks = ",average)
    
    def percentage(self):
        percent = float((self.s1+self.s2+self.s3+self.s4+self.s5) / 5)
        print("Percentage = ",percent)

name = input("Enter a name = ")
s1=float(input("enter first subject marks = "))
s2=float(input("enter second subject marks = "))
s3=float(input("enter third subject marks = "))
s4=float(input("enter fourth subject marks = "))
s5=float(input("enter fifth subject marks = "))

student = Student(name,s1,s2,s3,s4,s5)

student.totalmarks()
student.averagemarks()
student.percentage()
""" 
#Write a class bankAccount with: 
#Attributes: account holder, balance
#Methods: deposit,withdraw, check balance
#Add logic to prevent withdrawing more than the balance
"""
class Bankaccount:
    def __init__ (self,accountholder,balance):
        self.accountholder = accountholder
        self.balance = balance
    
    def deposit(self,amount):
        if amount <= 0:
            print("Deposited must be positive.")
        else:
            self.balance = 0.0
            self.balance = self.balance + amount
            print("Desposited amount = ",self.balance)
    
    def withdraw(self,amount):
        if amount <= 0:
            print("Withdrawn must be positive.")
            
        elif amount > self.balance:
            print("Insufficient to withdraw.")
        
        else:
            self.balance = self.balance - amount
            print("Withdrawn amount = ",self.balance)
    
    def checkbalance(self):
        print("Current balance = ",self.balance)

accountholder = input("Enter the name of accountholder = ")    
amount = float(input("Enter the amount = ")) 

bankaccount = Bankaccount(accountholder, amount)

bankaccount.deposit(amount)
bankaccount.withdraw(1000)
bankaccount.checkbalance()
""" 
#Create a class library:   
#Maintains the list of books with method to add_book, remove_book and display_book
class Library:
    def __init__(self):
        self.book = []
        
    def addbook(self,bookname):
        if bookname in self.book:
            print(f"'{bookname}' is available in library.")
        else:
            self.book.append(bookname)
            print(f"'{bookname}' is added in library. ")
            
    def removebook(self,bookname):
        if bookname in self.book:
            self.book.remove(bookname)
            print(f"'{bookname}' is removed from the library.")
        else:
            print(f"'{bookname}' is not available.")

    def displaybook(self):
        if not self.book:
            print("The library has no books.")
        else:
            print("Books are available in library.")
            index = 1
            for bookname in self.book:
                print(str(index) + ". " + bookname)
                index = index + 1

library = Library()

library.addbook("Radha")
library.addbook("Khusi")
library.addbook("Rich Dad, Poor Dad")
library.addbook("Ikigai")
library.displaybook()

library.removebook("Radha")
library.displaybook()