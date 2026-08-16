# RENT CALCULATOR IN PYTHON

import time

# TAKING REQUIRED INPUTS FROM THE USER

# TOTAL RENT OF THE HOSTEL OR FLAT
rent = float(input("ENTER YOUR HOSTEL/FLAT RENT = "))

# TOTAL AMOUNT SPENT ON FOOD AND SNACKS
food = float(input("ENTER THE TOTAL AMOUNT SPENT ON FOOD = "))

# TOTAL ELECTRICITY UNITS CONSUMED
electricity_units = float(input("ENTER THE TOTAL ELECTRICITY UNITS USED = "))

# ELECTRICITY CHARGE PER UNIT
charge_per_unit = float(input("ENTER THE ELECTRICITY CHARGE PER UNIT = "))

# TOTAL NUMBER OF PEOPLE LIVING IN THE ROOM OR FLAT
persons = int(input("ENTER THE NUMBER OF PERSONS LIVING IN THE ROOM/FLAT = "))


# CHECKING IF THE NUMBER OF PERSONS IS VALID
if persons <= 0:
    print("ERROR: NUMBER OF PERSONS MUST BE GREATER THAN 0.")

else:
    # CALCULATING THE TOTAL ELECTRICITY BILL
    electricity_bill = electricity_units * charge_per_unit

    # CALCULATING THE TOTAL EXPENSE
    total_expense = rent + food + electricity_bill

    # CALCULATING THE AMOUNT TO BE PAID BY EACH PERSON
    amount_per_person = round(total_expense / persons,1)

    # DISPLAYING THE FINAL RESULT
    print("\nTOTAL ELECTRICITY BILL =", electricity_bill)
    time.sleep(0.5)
    print("TOTAL EXPENSE =", total_expense)
    time.sleep(0.5)
    print("EACH PERSON WILL PAY =", amount_per_person,)


