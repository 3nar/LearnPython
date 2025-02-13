


# file name : FunctionsinPython.py
# Discription : now we are learning Functions in Python (def, Parameters, *args, **kwargs)
# auther : Nasser hadi
# github : https://github.com/3nar




# Functions in Python (`def`, Parameters, `*args`, `**kwargs`)

'''
Functions **help organize code**, **reduce repetition**, and **increase reusability**. In this step, we will learn:

✅ **Defining and calling functions**  
✅ **Default arguments**  
✅ **Variable-length arguments (`*args`)**  
✅ **Keyword arguments (`**kwargs`)**  

---

## **1. Defining and Calling Functions**
A function is defined using the `def` keyword.

### **a) Basic Function**
```python
def greet():
    print("Hello, welcome to Python!")

# Calling the function
greet()
```
💡 **Output:** `Hello, welcome to Python!`

### **b) Function with Parameters**
```python
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")  # Output: Hello, Alice!
greet_user("Bob")    # Output: Hello, Bob!
```
- **Parameters** allow functions to accept inputs.
- `name` is a **parameter**, `"Alice"` is an **argument**.

---

## **2. Function with Return Value**
A function can return a value using `return`.

```python
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)  # Output: Sum: 8
```
- The function **returns** `a + b`, and we store it in `result`.

---

## **3. Default Arguments**
You can set a **default value** for parameters.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet()         # Output: Hello, Guest!
```
- If no argument is given, `name` defaults to `"Guest"`.

---

## **4. `*args` (Variable-Length Arguments)**
`*args` allows a function to accept **any number of arguments**.

```python
def sum_numbers(*numbers):
    total = sum(numbers)
    print("Sum:", total)

sum_numbers(1, 2, 3)        # Output: Sum: 6
sum_numbers(10, 20, 30, 40) # Output: Sum: 100
```
- `*args` collects **all extra arguments** into a **tuple**.

---

## **5. `**kwargs` (Keyword Arguments)**
`**kwargs` allows passing **multiple named arguments**.

```python
def user_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

user_info(name="Alice", age=25, city="New York")
```
**Output:**
```
name: Alice
age: 25
city: New York
```
- `**kwargs` collects extra named arguments into a **dictionary**.

---

## **6. Combining `*args` and `**kwargs`**
```python
def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

display_info(1, 2, 3, name="Alice", age=25)
```
**Output:**
```
Positional arguments: (1, 2, 3)
Keyword arguments: {'name': 'Alice', 'age': 25}
```

---

'''
