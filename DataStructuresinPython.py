


# file name : DataStructuresinPython.py
# Discription : now we are learning Data Structures in Python (Lists , Tuples , Sets , Dictionaries)
# auther : Nasser hadi
# github : https://github.com/3nar




# Data Structures in Python (Lists , Tuples , Sets , Dictionaries)

'''
Python provides **powerful data structures** to store and manipulate data efficiently. In this step, we will learn:

✅ **Lists** (Mutable, Slicing, List Comprehension)  
✅ **Tuples** (Immutable, Unpacking)  
✅ **Sets** (Unordered, Unique Values, Set Operations)  
✅ **Dictionaries** (Key-Value Pairs, Iterating through Dictionaries)  

---

## **1. Lists in Python (Mutable)**
A **list** is an **ordered, mutable** collection of elements.

### **a) Creating a List**
```python
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']
```

### **b) Accessing List Elements**
```python
print(fruits[0])  # Output: apple
print(fruits[-1]) # Output: cherry
```

### **c) Modifying a List**
```python
fruits.append("orange")  # Adds at the end
fruits.insert(1, "grape") # Inserts at index 1
print(fruits)  # Output: ['apple', 'grape', 'banana', 'cherry', 'orange']
```

### **d) Removing Elements**
```python
fruits.remove("banana")  # Removes specific element
fruits.pop()  # Removes last element
print(fruits)
```

### **e) Slicing a List**
```python
numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:4])  # Output: [1, 2, 3] (From index 1 to 3)
print(numbers[:3])   # Output: [0, 1, 2] (First 3 elements)
print(numbers[3:])   # Output: [3, 4, 5, 6] (Elements from index 3 onwards)
```

### **f) List Comprehension (Shorter way to create lists)**
```python
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

---

## **2. Tuples in Python (Immutable)**
A **tuple** is an **ordered, immutable** collection.

### **a) Creating a Tuple**
```python
colors = ("red", "green", "blue")
print(colors)  # Output: ('red', 'green', 'blue')
```

### **b) Accessing Tuple Elements**
```python
print(colors[1])  # Output: green
```

### **c) Tuple Unpacking**
```python
coordinates = (10, 20, 30)
x, y, z = coordinates
print(x, y, z)  # Output: 10 20 30
```

---

## **3. Sets in Python (Unordered, Unique Values)**
A **set** is an **unordered collection** that does **not allow duplicate values**.

### **a) Creating a Set**
```python
numbers = {1, 2, 3, 4, 4, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5} (Duplicates removed)
```

### **b) Adding and Removing Elements**
```python
numbers.add(6)
numbers.remove(3)
print(numbers)  # Output: {1, 2, 4, 5, 6}
```

### **c) Set Operations**
```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # Union: {1, 2, 3, 4, 5}
print(A & B)  # Intersection: {3}
print(A - B)  # Difference: {1, 2}
```

---

## **4. Dictionaries in Python (Key-Value Pairs)**
A **dictionary** is a collection of **key-value pairs**.

### **a) Creating a Dictionary**
```python
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

### **b) Accessing and Modifying Dictionary Values**
```python
print(person["name"])  # Output: Alice
person["age"] = 26  # Modify a value
person["country"] = "USA"  # Add new key-value pair
print(person)
```

### **c) Iterating Through a Dictionary**
```python
for key, value in person.items():
    print(key, ":", value)
```

### **d) Removing a Key-Value Pair**
```python
del person["city"]
print(person)  # Output: {'name': 'Alice', 'age': 26, 'country': 'USA'}
```

---

'''
