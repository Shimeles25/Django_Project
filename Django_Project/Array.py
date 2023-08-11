import time
''' 
cars=["ford", "Volvo", "BMW"]
print(cars[0])
cars[0]="New XCar"

cars.append("Holand")
cars.append("Vitz")
for i in cars:
    print(i) 
#cars.clear()
cars_new=[]
cars_new=cars.copy()
print("############################")
cars_new.insert(2,"Shimeles");
cars_new.extend(cars)
#cars_new.remove("Shimeles")
#cars_new.reverse()

cars_new.sort(reverse=True)
print("Cars and Cars_new Started Here")
for i in cars_new:
    print(i)
#print(cars_new.count("ford"))
#print(cars.index("Volvo"))

class MyClass:
    def hello(self):
        print("A hello method is called now")
    def __str__(self):
        return f"{self.first_name}{self.age}"

    def __init__(self,name,Age) -> None:
        self.first_name=name
        self.age=Age

p1=MyClass("Shimeles ",40)
#del p1
""" "print(p1.first_name,"\n")
print(p1.age,"\n")"""
print(p1)
class names:
    pass

p1.hello()

print("##### INHERITANCE #####")
class Person:
    def __init__(self,fname,lname,year):
        self.first_name=fname
        self.last_name=lname
        self.year=year

    def printname(self):
        print(self.first_name, self.last_name,self.year)
    def WorkExpYear():
        print("Work experience is only calculated by child class")
class Student(Person):
    def __init__(self, fname, lname,year):
      super().__init__("Umer","kedir",year)
      self.graduationyear=year
    def WorkExpYear(self):
        print("Work experience:" ,2023-self.year)
        
student=Student("hunde","JU",2019)
student.WorkExpYear()
student.printname()

mytuple=("apple","banana","cherry","Orange","Mango")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
mytuple=("apple","banana","cherry","Orange","Mango")
myit=iter(mytuple)
print("###########################")
for x in myit:
    print(x)
print("###########################")
mystr="Knowledge"
mit=iter(mystr)
for i in mit:
    print(i)

class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=50:
            x=self.a
            self.a+=1
            return x
        else:
            print(" I love coding")
            raise StopIteration
myclass=MyNumbers()
myiter=iter(myclass)
while(True):
    print(next(myiter))
    time.sleep(0)

print("##### Class Polymorphism #####")
class Car:
    def __init__(self,name,brand) -> None:
        self.name=name
        self.brand=brand
    def move(self):
        print("Drive")
class Boat:
    def __init__(self,name,brand) -> None:
        self.name=name
        self.brand=brand
    def move(self):
        print("Sail!")
class Plane:
    def __init__(self,name,brand) -> None:
        self.name=name
        self.brand=brand
    def move(self):
        print("Fly!")
car=Car("Ford","Mustang")
boat=Boat("Ibiza","Touring 20")
plane =Plane("Boeing","747")
for x in (car,boat,plane):
    x.move()      
'''
class Vehicle:
    def __init__(self,brand,name) -> None:
        self.brand=brand
        self.name=name
    def move(self):
        print("Move!")
class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
        print("Sail!")
class Plane(Vehicle):
    def move(self):
        print("Fly !")
car=Car("Ford","Mustang")
boat=Boat("Ibiza","Touring 20")
plane=Plane("Boeing","747")
for x in (car,boat,plane):
    print(x.brand)
    print(x.name)
    x.move()

