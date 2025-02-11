


# file name : LoopinPython.py
# Discription : now we are learning loops in Python
# author : Nasser hadi
# github : https://github.com/3nar




# Loops in Python (`for`, `while`, `break`, `continue`)

'''
Loops are used to **repeat a block of code** multiple times.

---

## **1. `for` Loop**
A `for` loop is used to **iterate over a sequence** (like a list, tuple, or string).

### **a) Basic `for` Loop**
```python
for i in range(5):  # Loops from 0 to 4
    print("Iteration:", i)
```
💡 `range(5)` generates numbers **0 to 4** (not including 5).

### **b) Using `range(start, stop, step)`**
```python
for i in range(1, 10, 2):  # Start at 1, end before 10, step 2
    print(i)
```
- `range(1, 10, 2)` generates: **1, 3, 5, 7, 9**.

### **c) Looping Through a List**
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

### **d) Looping Through a String**
```python
word = "Python"

for letter in word:
    print(letter)
```

---

## **2. `while` Loop**
A `while` loop **runs as long as** a condition is `True`.

### **a) Basic `while` Loop**
```python
count = 0

while count < 5:
    print("Count:", count)
    count += 1  # Increment count
```

### **b) Infinite `while` Loop (With `break`)**
```python
while True:
    answer = input("Type 'exit' to stop: ")
    if answer == "exit":
        break
```
💡 **Without `break`, this loop runs forever!**

---

## **3. `break` Statement**
The `break` statement **exits the loop** immediately.

```python
for i in range(10):
    if i == 5:
        break  # Stops loop when i is 5
    print(i)
```
💡 Output: **0, 1, 2, 3, 4** (stops at 5).

---

## **4. `continue` Statement**
The `continue` statement **skips** the current iteration **but continues the loop**.

```python
for i in range(10):
    if i == 5:
        continue  # Skips 5, but continues
    print(i)
```
💡 Output: **0, 1, 2, 3, 4, 6, 7, 8, 9** (5 is skipped).

---

## **5. Nested Loops**
A loop inside another loop.

```python
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
```

---

## **6. `else` with Loops**
An `else` block **runs when the loop completes normally** (without `break`).

```python
for i in range(5):
    print(i)
else:
    print("Loop completed successfully!")
```

If `break` is used, the `else` block **won't run**:
```python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed!")  # This won't run
```

---

'''
