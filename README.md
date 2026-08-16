# Rent Calculator

A simple **Python-based Rent Calculator** that calculates the total expenses of a hostel or flat and determines how much each person needs to pay.

## Features

* Takes the total rent as input.
* Takes the total amount spent on food and snacks.
* Calculates the total electricity bill using:
  `Electricity Units × Charge Per Unit`
* Calculates the total overall expense.
* Divides the total expense among the number of people.
* Rounds the amount per person to **1 decimal place**.
* Checks that the number of persons is greater than `0`.
* Displays the results with a short delay between each output.

## How It Works

The program asks the user to enter:

1. Total hostel/flat rent
2. Total amount spent on food
3. Total electricity units used
4. Electricity charge per unit
5. Number of people living in the room/flat

It then calculates:

```text
Electricity Bill = Electricity Units × Charge Per Unit

Total Expense = Rent + Food + Electricity Bill

Amount Per Person = Total Expense ÷ Number of Persons
```

The amount paid by each person is rounded to **one decimal place**.

## Example

```text
ENTER YOUR HOSTEL/FLAT RENT = 20000
ENTER THE TOTAL AMOUNT SPENT ON FOOD = 10000
ENTER THE TOTAL ELECTRICITY UNITS USED = 300
ENTER THE ELECTRICITY CHARGE PER UNIT = 50
ENTER THE NUMBER OF PERSONS LIVING IN THE ROOM/FLAT = 4

TOTAL ELECTRICITY BILL = 15000.0
TOTAL EXPENSE = 45000.0
EACH PERSON WILL PAY = 11250.0
```

## Error Handling

The program checks whether the number of persons is valid.

If the user enters `0` or a negative number:

```text
ERROR: NUMBER OF PERSONS MUST BE GREATER THAN 0.
```

This prevents the program from attempting to divide by zero.

## Requirements

* Python 3.x

The program uses Python's built-in `time` module, so no external libraries are required.

## How to Run

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Open the project folder in your terminal or VS Code.
4. Run the Python file:

```bash
python rent_calculator.py
```

5. Enter the required values when prompted.

## Concepts Used

This project demonstrates basic Python concepts such as:

* `input()`
* `float()` and `int()`
* Variables
* Arithmetic operators
* `if-else` statements
* Division
* `round()` function
* `time.sleep()`
* Basic error prevention

## 👨‍💻 Author

**Muhammad Noman**

Student | Python Learner | Aspiring Computer Scientist

I'm currently learning programming and building small projects to improve my problem-solving and software development skills.

🔗 **GitHub:** [Noman-Stacks](https://github.com/Noman-Stacks)

Feel free to explore my other projects and repositories on GitHub.


