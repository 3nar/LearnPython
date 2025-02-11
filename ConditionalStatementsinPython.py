


# file name : ConditionalStatementsinPython.py
# Discription : now we are learning Conditional Statements in Python
# author : Nasser hadi
# github : https://github.com/3nar




# Conditional Statements in Python (`if`, `elif`, `else`)

'''
Conditional statements allow the program to **make decisions** based on conditions. The main statements are:

1. `if` - Executes a block of code **if** the condition is true.
2. `elif` - (else if) Executes a block of code if the previous conditions were false.
3. `else` - Executes a block of code if **all previous conditions** are false.

---

## **1. Basic `if` Statement**
```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
```
💡 The **indentation** (spaces before `print()`) is important in Python. It determines the **block of code** inside `if`.

---

## **2. Using `if-else`**
```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```
- If the condition `age >= 18` is **True**, the first block runs.
- Otherwise, the `else` block runs.

---

## **3. Using `if-elif-else`**
When there are multiple conditions, use `elif` (else if):

```python
age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif 13 <= age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")
```
- The `if` condition is checked first.
- If `if` is **False**, Python checks `elif`.
- If **none** of them are True, `else` runs.

---

## **4. Using Multiple Conditions (`and`, `or`, `not`)**
### **a) `and` - Both conditions must be True**
```python
temperature = int(input("Enter temperature: "))

if temperature > 30 and temperature < 40:
    print("It's hot outside.")
```
💡 Both conditions must be **True** for the block to execute.

### **b) `or` - At least one condition must be True**
```python
rainy = input("Is it rainy? (yes/no): ")

if rainy == "yes" or rainy == "Yes":
    print("Take an umbrella!")
```
💡 If **either** condition is True, the block runs.

### **c) `not` - Reverses the condition**
```python
is_sunny = False

if not is_sunny:
    print("It is not sunny today.")
```
💡 `not` reverses the boolean value (`True` → `False`, `False` → `True`).

---

## **5. Nested `if` Statements**
You can place an `if` inside another `if`.

```python
age = int(input("Enter your age: "))

if age > 0:
    if age < 13:
        print("You are a child.")
    elif age < 18:
        print("You are a teenager.")
    else:
        print("You are an adult.")
else:
    print("Invalid age!")
```

---

## **6. Short `if` Statement (Ternary Operator)**
```python
age = int(input("Enter your age: "))

message = "Adult" if age >= 18 else "Minor"
print(message)
```
💡 This is a **shorter way** to write an `if-else` statement.

---

'''
