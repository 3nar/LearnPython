


# file name : AdvancedPython.py
# Discription : now we are learning advanced features in Python
# auther : Nasser hadi
# github : https://github.com/3nar




# Advanced Python Features  

'''
Now that you have a solid understanding of Python basics, let's explore **advanced features** that make Python more powerful.

In this step, we will cover:
✅ **Lambda functions (anonymous functions)**  
✅ **Functional programming (`map()`, `filter()`, `reduce()`)**  
✅ **Exception handling (`try-except-finally`)**  
✅ **File handling (`open()`, `read()`, `write()`)**  

---

## **1. Lambda Functions (Anonymous Functions)**
Lambda functions are **small, one-line functions** that don’t need a `def` statement.

### **a) Basic Lambda Function**
```python
# Normal function
def square(x):
    return x ** 2

print(square(5))  # Output: 25

# Lambda equivalent
square_lambda = lambda x: x ** 2
print(square_lambda(5))  # Output: 25
```
💡 **Why use lambda?** It's useful for **short, simple functions**.

### **b) Lambda with Multiple Arguments**
```python
add = lambda x, y: x + y
print(add(3, 4))  # Output: 7
```

### **c) Lambda with Sorting**
```python
points = [(2, 3), (1, 5), (4, 2)]
points.sort(key=lambda point: point[1])  # Sort by second value
print(points)  # Output: [(4, 2), (2, 3), (1, 5)]
```

---

## **2. Functional Programming (`map()`, `filter()`, `reduce()`)**
Python allows **functional programming** using built-in functions.

### **a) `map()` - Apply Function to All Elements**
```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```
💡 `map()` applies a function to **each item** in a list.

### **b) `filter()` - Keep Only Matching Elements**
```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
```
💡 `filter()` removes elements that don’t match the condition.

### **c) `reduce()` - Reduce List to a Single Value**
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120 (1*2*3*4*5)
```
💡 `reduce()` combines all list elements into **one final result**.

---

## **3. Exception Handling (`try-except-finally`)**
Exception handling prevents your program from crashing.

### **a) Basic `try-except`**
```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid number!")
```
💡 If an **error occurs**, the program **doesn’t crash**.

### **b) Using `finally`**
```python
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()
```
💡 The `finally` block **always runs**, whether there is an error or not.

---

## **4. File Handling (`open()`, `read()`, `write()`)**
Python allows you to **read and write** files easily.

### **a) Writing to a File**
```python
with open("sample.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is a file example.")
```
💡 `with open(...)` automatically **closes the file** after writing.

### **b) Reading a File**
```python
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
```

### **c) Appending to a File**
```python
with open("sample.txt", "a") as file:
    file.write("\nAdding a new line!")
```
💡 `"a"` mode **appends** new content without deleting existing text.

---

'''
