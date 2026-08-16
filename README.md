# 🏠 Rent Calculator

A simple and beginner-friendly **Rent Calculator built with Python** that helps calculate the total monthly expenses of a hostel room, flat, or shared accommodation and determines how much each person needs to pay.

This project was created to practice **Python fundamentals, user input, arithmetic operations, conditional statements, functions from built-in modules, and basic error handling**.

---

## 📌 About The Project

Managing shared accommodation expenses can sometimes be confusing when rent, food, and electricity costs need to be divided among multiple people.

This **Rent Calculator** simplifies the process by taking the required expenses from the user and automatically calculating:

* Total electricity bill
* Total combined expenses
* Amount that each person needs to pay

The program also validates the number of people to prevent a **division-by-zero error**.

---

## ✨ Features

* 🏠 Takes hostel or flat rent as input
* 🍔 Takes total food and snack expenses
* ⚡ Calculates the electricity bill
* 👥 Supports multiple people sharing the expenses
* 💰 Calculates the total combined expense
* ➗ Calculates each person's share
* 🔢 Rounds the amount per person to **1 decimal place**
* 🛡️ Prevents division by zero
* ⏱️ Uses a small delay between result messages for better output presentation
* 🐍 Uses only Python's built-in functionality, so no external packages are required

---

## 🧮 Calculations Used

The program performs three main calculations.

### 1. Electricity Bill

The electricity bill is calculated using:

```text
Electricity Bill = Electricity Units × Charge Per Unit
```

For example:

```text
300 units × 50 = 15,000
```

---

### 2. Total Expense

The total expense is calculated by adding:

```text
Total Expense = Rent + Food + Electricity Bill
```

For example:

```text
20,000 + 10,000 + 15,000 = 45,000
```

---

### 3. Amount Per Person

The total expense is divided equally among all people:

```text
Amount Per Person = Total Expense ÷ Number of Persons
```

For example:

```text
45,000 ÷ 4 = 11,250
```

The program uses Python's `round()` function to display the amount with **one digit after the decimal point**.

---

## 💻 Technologies Used

| Technology    | Purpose                              |
| ------------- | ------------------------------------ |
| Python        | Main programming language            |
| `input()`     | Taking user input                    |
| `if-else`     | Validating the number of persons     |
| `round()`     | Rounding the final amount            |
| `time` module | Adding a short delay between outputs |

---

## 📂 Project Structure

```text
Rent-Calculator/
│
├── rent_calculator.py
└── README.md
```

---

## ⚙️ Requirements

You only need:

* **Python 3.x**

No external libraries or packages are required.

The project uses Python's built-in `time` module.

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Rent-Calculator.git
```

### 2. Navigate to the Project Directory

```bash
cd Rent-Calculator
```

### 3. Run the Python Program

```bash
python rent_calculator.py
```

On some systems, you may need to use:

```bash
python3 rent_calculator.py
```

---

## 🖥️ How To Use

When the program starts, it asks the user for five values:

```text
ENTER YOUR HOSTEL/FLAT RENT =
ENTER THE TOTAL AMOUNT SPENT ON FOOD =
ENTER THE TOTAL ELECTRICITY UNITS USED =
ENTER THE ELECTRICITY CHARGE PER UNIT =
ENTER THE NUMBER OF PERSONS LIVING IN THE ROOM/FLAT =
```

Enter the required values and the program will calculate the expenses automatically.

---

## 📊 Example

### Input

```text
ENTER YOUR HOSTEL/FLAT RENT = 20000
ENTER THE TOTAL AMOUNT SPENT ON FOOD = 10000
ENTER THE TOTAL ELECTRICITY UNITS USED = 300
ENTER THE ELECTRICITY CHARGE PER UNIT = 50
ENTER THE NUMBER OF PERSONS LIVING IN THE ROOM/FLAT = 4
```

### Calculation

```text
Electricity Bill = 300 × 50
                 = 15000

Total Expense = 20000 + 10000 + 15000
              = 45000

Amount Per Person = 45000 ÷ 4
                  = 11250
```

### Output

```text
TOTAL ELECTRICITY BILL = 15000.0

TOTAL EXPENSE = 45000.0

EACH PERSON WILL PAY = 11250.0
```

---

## 🛡️ Error Handling

The program includes a basic validation check for the number of people.

If the user enters `0` or a negative number, the program displays:

```text
ERROR: NUMBER OF PERSONS MUST BE GREATER THAN 0.
```

This check is important because dividing by `0` would cause a Python `ZeroDivisionError`.

The relevant logic is:

```python
if persons <= 0:
    print("ERROR: NUMBER OF PERSONS MUST BE GREATER THAN 0.")
```

If the number of persons is valid, the program continues with the calculations.

---

## 📚 Python Concepts Practiced

This project is designed as a beginner Python project and demonstrates several important programming concepts.

### Variables

The program stores user input in variables such as:

```python
rent
food
electricity_units
charge_per_unit
persons
```

### User Input

The `input()` function is used to collect information from the user.

```python
rent = float(input("ENTER YOUR HOSTEL/FLAT RENT = "))
```

### Type Conversion

The program uses:

* `float()` for values that can contain decimals
* `int()` for the number of persons

### Arithmetic Operators

The program uses arithmetic operations such as:

```python
+
*
/
```

### Conditional Statements

An `if-else` statement checks whether the number of persons is valid.

### Rounding

The `round()` function is used to keep the final amount at one decimal place:

```python
amount_per_person = round(total_expense / persons, 1)
```

### Python Modules

The built-in `time` module is used to add a small delay between output messages:

```python
import time
```

---

## 🔍 Current Limitations

This is a basic version of the project, so there are some limitations:

* It does not store previous calculations.
* It does not save expenses to a file or database.
* All expenses are divided equally.
* It does not separately track expenses for each person.
* It does not provide a graphical user interface.
* It does not validate every possible invalid input, such as entering text instead of a number.

---

## 🚀 Future Improvements

Some possible improvements for future versions include:

* [ ] Add better input validation
* [ ] Allow individual food expenses for each person
* [ ] Add different rent contributions for different people
* [ ] Add a graphical user interface using Tkinter
* [ ] Save calculations to a file
* [ ] Add monthly expense history
* [ ] Generate an expense report
* [ ] Add support for different currencies
* [ ] Create a web-based version
* [ ] Add a menu-driven interface
* [ ] Allow users to calculate expenses for multiple months

---

## 🎯 Learning Objective

The main purpose of this project is to strengthen my understanding of **Python fundamentals** by building a practical program based on a real-life problem.

Through this project, I practiced:

> **Taking user input → Processing data → Performing calculations → Validating input → Displaying results**

It is a small project, but it helped me understand how basic Python concepts can be combined to create a useful application.

---

## 🤝 Contributing

This is a beginner-level learning project, but suggestions and improvements are welcome.

If you find a bug or have an idea for improving the calculator, feel free to open an **Issue** or submit a **Pull Request**.

---

## 📄 License

This project is open-source and available for learning and educational purposes.

---

## 👨‍💻 Author

**Muhammad Noman**

Student | Python Learner | Aspiring Computer Scientist

I'm currently learning programming and building small projects to improve my problem-solving and software development skills.

🔗 **GitHub:** [Noman-Stacks](https://github.com/Noman-Stacks)

Feel free to explore my other projects and repositories on GitHub.

⭐ **If you found this project useful or helpful, consider giving the repository a star!**
