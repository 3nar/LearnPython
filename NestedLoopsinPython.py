


# file name : NestedloopinPython.py
# Discription : now we are learning Nested Loops and Patterns in Python
# author : Nasser hadi
# github : https://github.com/3nar




# Step 5: Nested Loops and Patterns in Python

'''
Nested loops are loops **inside** another loop. They are useful for **working with grids, tables, and patterns**.

---

## **1. Understanding Nested Loops**
A **nested loop** means a loop runs **inside another loop**.

### **Example: Basic Nested Loop**
```python
for i in range(3):  # Outer loop
    for j in range(3):  # Inner loop
        print(f"i={i}, j={j}")
```
💡 **How it works:**
- The **outer loop** runs **3 times**.
- Each time the outer loop runs, the **inner loop runs 3 times**.

**Output:**
```
i=0, j=0
i=0, j=1
i=0, j=2
i=1, j=0
i=1, j=1
i=1, j=2
i=2, j=0
i=2, j=1
i=2, j=2
```

---

## **2. Creating Patterns with Nested Loops**
Nested loops are often used to print **shapes and patterns**.

### **a) Right-Angled Triangle**
```python
rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")  # Print * without a newline
    print()  # Move to the next line
```
**Output:**
```
*
* *
* * *
* * * *
* * * * *
```

---

### **b) Inverted Right-Angled Triangle**
```python
rows = 5

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
```
**Output:**
```
* * * * *
* * * *
* * *
* *
*
```

---

### **c) Pyramid Pattern**
```python
rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
```
**Output:**
```
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
```

---

### **d) Diamond Shape**
```python
rows = 5

# Upper Part
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# Lower Part
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)
```
**Output:**
```
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
```

---

### **e) Number Pyramid**
```python
rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```
**Output:**
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

'''
