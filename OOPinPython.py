


# file name : OOPinPython.py
# Discription : now we are learning Object-Oriented Programming in Python
# auther : Nasser hadi
# github : https://github.com/3nar




# OOP in Python

'''
# Understanding the Basics of OOP in Python

Before writing OOP code, we need to **understand the core concepts of Object-Oriented Programming (OOP)** and why it’s useful.

---

## **1. What is Object-Oriented Programming (OOP)?**
OOP is a **programming paradigm** based on the concept of **objects** and **classes**.

### **Why Use OOP?**
✅ **Code Reusability** – Avoid writing the same code multiple times.  
✅ **Encapsulation** – Hide data to protect it from direct modification.  
✅ **Abstraction** – Focus on important details while hiding the complex implementation.  
✅ **Inheritance** – Reuse code from existing classes.  
✅ **Polymorphism** – Same method behaves differently for different objects.  

---

## **2. Difference: Procedural vs. OOP Programming**
| Feature           | Procedural Programming (e.g., C) | OOP (e.g., Python) |
|------------------|--------------------------------|--------------------|
| **Focus**       | Functions & Procedures        | Objects & Classes |
| **Data Handling** | Stored in variables         | Stored inside objects |
| **Code Reusability** | No reuse, functions repeated | Inheritance allows reuse |
| **Example**     | `print_student(name, age)` | `student.display_info()` |

### **Example**
#### **Procedural Approach**
```python
def student_details(name, age):
    print(f"Student: {name}, Age: {age}")

student_details("Alice", 21)
```

#### **OOP Approach**
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student: {self.name}, Age: {self.age}")

student1 = Student("Alice", 21)
student1.display_info()
```
**Why is OOP better?**
- **Encapsulates data** (name & age belong to `Student`).
- **Code is reusable** (we can create multiple students without rewriting code).

---

## **3. Key OOP Terminology**
| Term          | Definition |
|--------------|------------|
| **Class**    | A **blueprint** for creating objects. |
| **Object**   | An **instance** of a class with real data. |
| **Attributes** | Variables that belong to an object (e.g., `name`, `age`). |
| **Methods**  | Functions inside a class that define behavior. |
| **Encapsulation** | Hiding data to prevent modification. |
| **Inheritance** | A class can **inherit** from another class. |
| **Polymorphism** | Same function name, different behavior. |

---

'''

## **Next Step**

# Creating Classes and Objects in Python

'''

Now that we understand the **concept of OOP**, let’s start writing **actual OOP code** by learning:

✅ **How to define a class**  
✅ **Creating objects (instances) of a class**  
✅ **Using the `__init__` constructor method**  
✅ **Instance Variables vs. Class Variables**  

---

## **1. Defining a Class**
A **class** is a blueprint for creating objects.

### **🔹 Basic Syntax**
```python
class Car:
    pass  # Empty class (for now)
```
💡 The `pass` keyword is used as a placeholder when the class has no code yet.

---

## **2. Creating an Object (Instance)**
An **object** is an **instance of a class**.

### **🔹 Example**
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Instance variable
        self.model = model  # Instance variable

# Creating objects (instances)
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.brand, car1.model)  # Output: Toyota Corolla
print(car2.brand, car2.model)  # Output: Honda Civic
```
💡 **Each object (`car1`, `car2`) has its own separate data!**

---

## **3. Understanding the `__init__` Constructor Method**
- The `__init__` method **initializes the object** when created.
- It is **automatically called** when an object is created.
- The `self` keyword refers to **the current object**.

### **🔹 Example with `__init__`**
```python
class Student:
    def __init__(self, name, age):
        self.name = name  # Instance Variable
        self.age = age    # Instance Variable

    def display(self):
        print(f"Student Name: {self.name}, Age: {self.age}")

# Creating instances
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

student1.display()  # Output: Student Name: Alice, Age: 20
student2.display()  # Output: Student Name: Bob, Age: 22
```
💡 `self.name` and `self.age` store data **inside each object**.

---

## **4. Instance Variables vs. Class Variables**
- **Instance Variables**: Unique for each object (defined inside `__init__`).
- **Class Variables**: Shared among all objects (defined outside `__init__`).

### **🔹 Example**
```python
class Employee:
    company = "TechCorp"  # Class Variable (shared)

    def __init__(self, name, salary):
        self.name = name  # Instance Variable (unique per object)
        self.salary = salary

# Creating objects
emp1 = Employee("John", 5000)
emp2 = Employee("Emma", 6000)

print(emp1.name, emp1.salary, emp1.company)  # Output: John 5000 TechCorp
print(emp2.name, emp2.salary, emp2.company)  # Output: Emma 6000 TechCorp

# Changing the class variable (affects all instances)
Employee.company = "NewTech"

print(emp1.company)  # Output: NewTech
print(emp2.company)  # Output: NewTech
```
💡 **Class variables** are shared, while **instance variables** are unique to each object.

---

'''

## **Next Step**

# Working with Methods in Python OOP

'''

Now that we have learned about **classes and objects**, let's explore **methods**, which define behaviors for objects.

In this step, we will cover:
✅ **Instance Methods (`self`)**  
✅ **Class Methods (`@classmethod`)**  
✅ **Static Methods (`@staticmethod`)**  

---

## **1. What Are Methods?**
A **method** is a function **inside a class** that operates on an object.

---

## **2. Instance Methods (`self`)**
- Operate on **instance variables** (unique to each object).
- Use `self` to access object attributes.

### **🔹 Example**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):  # Instance method
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

# Creating objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Calling instance method
person1.introduce()  # Output: Hi, I'm Alice and I'm 25 years old.
person2.introduce()  # Output: Hi, I'm Bob and I'm 30 years old.
```
💡 `self` refers to the **current object**.

---

## **3. Class Methods (`@classmethod`)**
- Operate on **class variables** (shared across all objects).
- Use `@classmethod` decorator.
- `cls` represents the **class itself**.

### **🔹 Example**
```python
class Employee:
    company = "TechCorp"  # Class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

# Creating objects
emp1 = Employee("John")
emp2 = Employee("Emma")

print(emp1.company)  # Output: TechCorp
print(emp2.company)  # Output: TechCorp

# Changing class variable using class method
Employee.change_company("NewTech")

print(emp1.company)  # Output: NewTech
print(emp2.company)  # Output: NewTech
```
💡 **All objects share class variables**, so `change_company()` affects **all instances**.

---

## **4. Static Methods (`@staticmethod`)**
- Do **not** operate on instance or class variables.
- Behave like regular functions but inside a class.
- Use `@staticmethod` decorator.

### **🔹 Example**
```python
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

# Calling static method
print(MathOperations.add(5, 3))  # Output: 8
```
💡 **No `self` or `cls`** is needed since it does not modify instance or class data.

---

## **5. Combining Instance, Class, and Static Methods**
```python
class BankAccount:
    bank_name = "Global Bank"  # Class variable

    def __init__(self, holder, balance):
        self.holder = holder  # Instance variable
        self.balance = balance

    def deposit(self, amount):  # Instance method
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    @classmethod
    def change_bank_name(cls, new_name):  # Class method
        cls.bank_name = new_name

    @staticmethod
    def bank_policy():  # Static method
        print("Bank policy: Minimum balance must be $100.")

# Creating an account
acc = BankAccount("Alice", 500)

# Using instance method
acc.deposit(200)  # Output: 200 deposited. New balance: 700

# Using class method
BankAccount.change_bank_name("Future Bank")
print(acc.bank_name)  # Output: Future Bank

# Using static method
BankAccount.bank_policy()  # Output: Bank policy: Minimum balance must be $100.
```

---

'''

## **Next Step**

# The Four Pillars of Object-Oriented Programming (OOP)

'''

OOP is built on **four key principles** (pillars) that make it powerful and efficient:

✅ **Encapsulation** – Hiding data to protect it.  
✅ **Abstraction** – Showing only necessary details.  
✅ **Inheritance** – Reusing code from parent classes.  
✅ **Polymorphism** – Same method, different behavior.  

---

## **1. Encapsulation (Data Hiding)**
Encapsulation is the **bundling of data (variables) and methods** that operate on that data into a **single unit (class)**.

### **🔹 Private Variables**
- In Python, variables with a **double underscore `__`** are **private** (cannot be accessed directly outside the class).

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public variable
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Creating an object
acc = BankAccount("123456", 1000)

print(acc.account_number)  # Output: 123456
# print(acc.__balance)  # ❌ Error: Cannot access private variable

# Accessing private variable using a method
print(acc.get_balance())  # Output: 1000

# Modifying balance using a method
acc.deposit(500)
print(acc.get_balance())  # Output: 1500
```
💡 **Why Encapsulation?**  
- Prevents direct modification of sensitive data.  
- Provides **controlled access** through methods.  

---

## **2. Abstraction (Hiding Complexity)**
Abstraction means **hiding unnecessary details** and showing only the relevant parts.

### **🔹 Example of Abstraction**
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract class
    @abstractmethod
    def start(self):
        pass  # Must be implemented in subclasses

class Car(Vehicle):
    def start(self):
        print("Car is starting with a key.")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting with a self-start button.")

# Creating objects
car = Car()
bike = Bike()

car.start()  # Output: Car is starting with a key.
bike.start()  # Output: Bike is starting with a self-start button.
```
💡 **Why Abstraction?**  
- Hides **unnecessary details** (e.g., how the engine works).  
- Provides a **simplified interface** to interact with objects.  

---

## **3. Inheritance (Code Reusability)**
Inheritance allows a **child class to reuse** attributes and methods from a **parent class**.

### **🔹 Example of Inheritance**
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Animal makes a sound.")

# Dog class inherits from Animal
class Dog(Animal):
    def make_sound(self):  # Overriding parent method
        print("Woof! Woof!")

# Cat class inherits from Animal
class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.make_sound()  # Output: Woof! Woof!
cat.make_sound()  # Output: Meow!
```
💡 **Why Inheritance?**  
- **Code reusability** – Child classes don’t need to redefine common behavior.  
- **Hierarchy structure** – Organizes related classes.  

---

## **4. Polymorphism (Multiple Forms)**
Polymorphism allows **one function name** to work **differently for different objects**.

### **🔹 Method Overriding (Different Behavior in Subclasses)**
```python
class Bird:
    def fly(self):
        print("Birds can fly.")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly.")

# Creating objects
sparrow = Bird()
penguin = Penguin()

sparrow.fly()  # Output: Birds can fly.
penguin.fly()  # Output: Penguins cannot fly.
```
💡 **Why Polymorphism?**  
- Allows **flexibility** and **extensibility** in code.  
- Makes it easy to **add new functionalities** without modifying existing code.  

---

## **5. Real-World Example: OOP in a Banking System**
```python
class Account:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Inheriting Account class
class SavingsAccount(Account):
    def __init__(self, holder, balance, interest_rate):
        super().__init__(holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.deposit(self.get_balance() * self.interest_rate)

# Creating objects
savings = SavingsAccount("Alice", 1000, 0.05)

savings.add_interest()
print(savings.get_balance())  # Output: 1050 (1000 + 5% interest)
```

---

'''

## **Next Step**

# Advanced OOP Features in Python

'''

Now that we understand the **four pillars of OOP**, let’s explore **advanced OOP features** that add flexibility and power to Python’s OOP.

In this step, we will cover:
✅ **Magic Methods (`__str__`, `__repr__`, `__len__`, etc.)**  
✅ **Operator Overloading (`+`, `-`, `*`, etc.)**  
✅ **Method Overriding (Modifying Parent Class Methods)**  
✅ **Multiple Inheritance (Inheriting from Multiple Classes)**  

---

## **1. Magic Methods (`dunder` methods)**
Magic methods (also called **dunder methods**, short for "double underscore") **begin and end with `__`**.  
They allow customization of **built-in Python operations**.

### **🔹 Common Magic Methods**
| Method       | Purpose |
|-------------|---------|
| `__init__`  | Constructor (initialize object) |
| `__str__`   | String representation (`print(object)`) |
| `__repr__`  | Official representation of an object |
| `__len__`   | Defines behavior for `len(object)` |
| `__add__`   | Defines behavior for `+` operator (operator overloading) |

---

### **🔹 Example: `__str__` and `__repr__`**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # Called when using print()
        return f"Person: {self.name}, Age: {self.age}"

    def __repr__(self):  # Called in debugging (interactive shell)
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 30)
print(p)  # Output: Person: Alice, Age: 30
print(repr(p))  # Output: Person('Alice', 30)
```
💡 **Why `__str__` and `__repr__`?**
- `__str__`: Human-readable output.
- `__repr__`: Developer-friendly representation.

---

### **🔹 Example: `__len__`**
```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

book = Book("Python Programming", 450)
print(len(book))  # Output: 450
```
💡 **Why `__len__`?**  
- Allows objects to work with `len()` like built-in types.

---

## **2. Operator Overloading (`+`, `-`, `*`, etc.)**
Operator overloading allows **custom objects to use standard operators (`+`, `-`, `*`, etc.)**.

### **🔹 Example: Overloading `+` Operator**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)

p3 = p1 + p2  # Calls __add__()
print(p3)  # Output: Point(6, 8)
```
💡 **Why Operator Overloading?**
- Allows custom objects to behave **like built-in types**.

---

## **3. Method Overriding (Modifying Parent Class Methods)**
A child class **can override** methods from a parent class.

### **🔹 Example: Overriding a Method**
```python
class Animal:
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):
        return "Bark!"

dog = Dog()
print(dog.make_sound())  # Output: Bark!
```
💡 **Why Override Methods?**
- Allows a subclass to **modify behavior** without changing the parent class.

---

## **4. Multiple Inheritance (Inheriting from Multiple Classes)**
Python allows a class to **inherit from multiple parent classes**.

### **🔹 Example: Multiple Inheritance**
```python
class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):  # Inherits from A and B
    def method_c(self):
        print("Method C")

obj = C()
obj.method_a()  # Output: Method A
obj.method_b()  # Output: Method B
obj.method_c()  # Output: Method C
```
💡 **Why Multiple Inheritance?**
- Allows a class to **combine features** from multiple sources.
- Should be used carefully to **avoid complexity** (diamond problem).

---

'''

## **Next Step**

# OOP Best Practices in Python

'''

Now that we’ve covered the technical aspects of OOP, let's focus on **best practices** to write **efficient, maintainable, and clean OOP code**.

✅ **Code Reusability and Clean Design**  
✅ **Composition vs. Inheritance (When to Use Each)**  
✅ **Avoiding Overuse of Inheritance (Favor Composition)**  

---

## **1. Code Reusability and Clean Design**  

**Best practices** for writing clean, reusable OOP code:

### **🔹 Use Meaningful Class & Method Names**  
Good naming makes code **self-explanatory**.  
❌ **Bad Practice:**  
```python
class P:
    def x(self, y):
        return y * 2
```
✅ **Good Practice:**  
```python
class Calculator:
    def double(self, number):
        return number * 2
```

---

### **🔹 Keep Classes Focused (Single Responsibility Principle - SRP)**  
Each class should have **only one job**.  

❌ **Bad Practice (Too Many Responsibilities in One Class)**  
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary * 12  # Business logic (bad inside Employee class)

    def save_to_database(self):
        print("Saving employee data to DB")  # Database logic (should be separate)
```
✅ **Good Practice (Separate Responsibilities)**  
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class SalaryCalculator:
    def calculate_salary(self, employee):
        return employee.salary * 12

class EmployeeDatabase:
    def save(self, employee):
        print("Saving employee data to DB")
```
💡 **Why?**  
- **Easier to modify** (if salary logic changes, only `SalaryCalculator` needs updating).  
- **Better separation** of concerns.  

---

## **2. Composition vs. Inheritance (When to Use Each)**  
Inheritance is **powerful** but **not always the best choice**. Sometimes, **composition is better**.

### **🔹 What is Composition?**
Instead of inheriting, **an object contains another object** (has-a relationship).

### **Example: Inheritance (❌ Bad Approach)**
```python
class Engine:
    def start(self):
        print("Engine started")

class Car(Engine):  # ❌ Bad inheritance (Car is not an Engine)
    def drive(self):
        print("Car is driving")

car = Car()
car.start()  # Inherited from Engine
car.drive()
```
**Problem:**  
- A **Car is not an Engine**.  
- This **doesn’t make sense** in real-world modeling.  

---

### **🔹 Better Approach: Composition (✅ Good Practice)**
```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS an Engine

    def drive(self):
        self.engine.start()
        print("Car is driving")

car = Car()
car.drive()
```
💡 **Why is Composition Better?**  
- **More flexible** (a car **has** an engine, it **is not** an engine).  
- **Easier to change** (replace `Engine` with `ElectricEngine` without modifying `Car`).  

---

## **3. Avoiding Overuse of Inheritance (Favor Composition)**
Too much inheritance creates **complex hierarchies** that are hard to manage.

### **🔹 Deep Inheritance (❌ Bad Practice)**
```python
class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

class Labrador(Dog):
    pass

class ShowLabrador(Labrador):
    pass  # Too many levels of inheritance!
```
**Problems with Deep Inheritance:**
- Hard to understand **which class does what**.  
- Changing **one class affects everything below it**.  
- Breaks the **Open/Closed Principle** (difficult to extend without modifying the base class).  

### **🔹 Better Approach: Favor Composition**
Instead of deep hierarchies, **break responsibilities into smaller classes** and use **composition**.

✅ **Good Practice:**
```python
class Animal:
    def breathe(self):
        print("Breathing")

class CanBark:
    def bark(self):
        print("Woof!")

class Dog(Animal, CanBark):  # Using composition
    pass

dog = Dog()
dog.breathe()  # Output: Breathing
dog.bark()  # Output: Woof!
```
💡 **Why?**
- **More flexible** (Dog can **bark**, but other animals can inherit `Animal` without it).  
- **Avoids unnecessary deep inheritance**.  

---

## **4. Additional OOP Best Practices**
### **🔹 Use Getters and Setters (Encapsulation)**
Instead of directly accessing attributes, use **getter and setter methods**.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def get_balance(self):
        return self.__balance  # Getter method

    def set_balance(self, new_balance):
        if new_balance > 0:
            self.__balance = new_balance  # Setter method

account = BankAccount(1000)
print(account.get_balance())  # ✅ Access balance safely
account.set_balance(1200)
print(account.get_balance())  # ✅ Updated balance
```
💡 **Why?**  
- Protects data from **accidental modification**.  
- Allows **validation checks** before updating values.  

---

'''

## **Next Step**

# Real-World OOP Projects

'''

Now that we’ve covered **OOP concepts**, it's time to **apply them in real-world projects**.  

---

## **📌 Project 1: Banking System (Encapsulation + Inheritance)**
We will build a **Banking System** with:
✅ **Encapsulation** – Secure bank account balance  
✅ **Inheritance** – Different types of accounts  
✅ **Methods** – Deposit, Withdraw, and Check Balance  

### **🔹 Code Implementation**
```python
class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.__balance = balance  # Private attribute (Encapsulation)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

# Inheriting from BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: ${interest}")

# Creating objects
account1 = SavingsAccount("123456", "Alice", 1000, 0.05)

# Performing operations
account1.deposit(500)
account1.withdraw(200)
account1.add_interest()
print(f"Final Balance: ${account1.get_balance()}")
```

💡 **Concepts Used:**  
- **Encapsulation** – `__balance` is **private**.  
- **Inheritance** – `SavingsAccount` extends `BankAccount`.  
- **Methods** – Deposit, Withdraw, Add Interest.  

---

## **📌 Project 2: Student Management System**  
We will create a **Student Management System** with:
✅ **Classes for Students and Courses**  
✅ **Encapsulation** – Student details hidden  
✅ **Composition** – A student can have multiple courses  

### **🔹 Code Implementation**
```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.__courses = []  # Private attribute (Encapsulation)

    def enroll(self, course):
        self.__courses.append(course)
        print(f"{self.name} enrolled in {course.course_name}")

    def get_courses(self):
        return [course.course_name for course in self.__courses]

class Course:
    def __init__(self, course_name):
        self.course_name = course_name

# Creating students and courses
student1 = Student("Alice", "S1001")
student2 = Student("Bob", "S1002")

course1 = Course("Python Programming")
course2 = Course("Data Science")

# Enrolling students
student1.enroll(course1)
student1.enroll(course2)

student2.enroll(course1)

print(f"{student1.name}'s courses: {student1.get_courses()}")
print(f"{student2.name}'s courses: {student2.get_courses()}")
```

💡 **Concepts Used:**  
- **Encapsulation** – Courses are private.  
- **Composition** – A student **has** courses.  

---

## **📌 Project 3: Employee Payroll System**  
We will create an **Employee Payroll System** with:
✅ **Encapsulation** – Employee salary hidden  
✅ **Inheritance** – Different types of employees  
✅ **Polymorphism** – Override salary calculation  

### **🔹 Code Implementation**
```python
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.__base_salary = base_salary  # Private attribute

    def calculate_salary(self):
        return self.__base_salary

    def get_salary(self):
        return self.calculate_salary()

class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):  # Overriding method
        return super().calculate_salary() + self.bonus

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, hourly_rate * hours_worked)

# Creating objects
emp1 = FullTimeEmployee("Alice", 5000, 1000)
emp2 = PartTimeEmployee("Bob", 20, 80)

# Getting salary details
print(f"{emp1.name}'s Salary: ${emp1.get_salary()}")
print(f"{emp2.name}'s Salary: ${emp2.get_salary()}")
```

💡 **Concepts Used:**  
- **Encapsulation** – Base salary is private.  
- **Inheritance** – Full-time and part-time employees extend `Employee`.  
- **Polymorphism** – Different salary calculations.  

---

'''

