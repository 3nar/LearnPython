


# file name : PythonBasics.py
# Discription : now we are learning python basics
# author : Nasser hadi
# github : https://github.com/3nar




# Python Basics - Variables, Data Types, and Input/Output

'''
## **1. Variables in Python**
A **variable** is used to store data. Python does not require declaring variable types explicitly.

### **a) Declaring Variables**
```python
# Assigning values to variables
name = "Alice"    # String
age = 25         # Integer
height = 5.6     # Float
is_student = True # Boolean

print(name, age, height, is_student)
```
💡 Python is **dynamically typed**, meaning the type of a variable is determined automatically.

---

## **2. Data Types in Python**
Python has several built-in data types:

| Data Type   | Example            | Description                  |
|------------|-------------------|------------------------------|
| `int`      | `x = 10`          | Whole numbers                |
| `float`    | `y = 3.14`        | Decimal numbers              |
| `str`      | `name = "Alice"`  | Text data                    |
| `bool`     | `status = True`   | True or False                |
| `list`     | `[1, 2, 3]`       | Ordered, mutable collection  |
| `tuple`    | `(4, 5, 6)`       | Ordered, immutable collection |
| `dict`     | `{"key": "value"}` | Key-value pairs              |

### **a) Checking Data Types**
```python
x = 10
y = 3.14
text = "Hello"
is_python_fun = True

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(text))  # <class 'str'>
print(type(is_python_fun))  # <class 'bool'>
```

---

## **3. Taking User Input**
Python allows user interaction using `input()`.

### **a) Getting User Input**
```python
name = input("Enter your name: ")
print("Hello, " + name)
```
💡 `input()` always returns a **string**.

### **b) Converting Input to Numbers**
```python
age = int(input("Enter your age: "))
print("You are", age, "years old.")
```
- Use `int()` for whole numbers.
- Use `float()` for decimal numbers.

---

## **4. Comments in Python**
Comments help in explaining the code but are ignored by Python.

```python
# This is a single-line comment

"""
This is a multi-line comment.
It can span multiple lines.
"""
```

---

## **5. Operators in Python**
### **a) Arithmetic Operators**
```python
a = 10
b = 3

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a // b) # Floor division
print(a % b)  # Modulus
print(a ** b) # Exponentiation (10^3)
```

### **b) Comparison Operators**
```python
x = 10
y = 20

print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= y)  # False
print(x <= y)  # True
```

### **c) Logical Operators**
```python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```
---

'''
