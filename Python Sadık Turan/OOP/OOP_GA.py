# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 16:29:48 2021

@author: Gökhan Akay
"""

class Person:
    
    #class attributes
    address = 'miralay tevfik bey'
    
    #constructor: bir instance(object) yaratıldığında ilk önce bu blok çalışıyor.
    def __init__(self,name,year):
        #object attributes
        self.name= name
        self.year= year
        print("init çalıştı.")
        
    def intro(self):
        print(f'Hey girl! I am {self.name}')
        
    def calculateAge(self):
        return 2021-self.year
        
        
p1 = Person('Gökhan', 1992)
p2 = Person('Sena', 1991)

print(f'p1_name: {p1.name}, p1_year: {p1.year}, p1_address: {p1.address}')    
print(f'p2_name: {p2.name}, p2_year: {p2.year}')      

p1.intro()
p1.calculateAge()    



class Circle:
    
    pi = 3.14
    
    def __init__(self, radius = 1):
        self.radius = radius
        
    def calculateLength(self):
        return 2*self.radius*self.pi
    
    def calculateArea(self):
        return self.pi * (self.radius**2)
    

c1 = Circle(3)
c1.calculateLength()
c1.calculateArea()    


class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('person created.')
        
    def who_am_i(self):
        print("I am a person.")
        
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        print('student created.')
      
    #başına override yazmamıza gerek yok.    
    def who_am_i(self):
        print("I am a student.")
        
s1 = Student("Gökhan", "Akay")        
s1.firstName
s1.who_am_i()
