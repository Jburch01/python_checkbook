import csv
import datetime as dt

import os
from checkbook_history_structure import *



def view():
    balance = get_balance()
    print(f"Your current balance is: {balance}\n")


def withdraw(num):
    balance = float(get_balance())
    if num > balance:
        print("Sorry you to broke for that!\n")
    else:
        balance -= num
        balance = round(balance, 2)
        str(change_balance(balance))
        if os.path.exists('checkbookHistory.csv'):
            add_history(num, "Withdraw", balance, get_time(), get_date())
        else:
            create_csv()
            add_history(num, "Withdraw", balance, get_time(), get_date())




def deposit(num):
    balance = float(get_balance())
    balance += num
    balance = round(balance, 2)
    print(balance)
    change_balance(balance)
    if os.path.exists('checkbookHistory.csv'):
        add_history(num, "Deposit", balance, get_time(), get_date())
    else:
        create_csv()
        add_history(num, "Deposit", balance, get_time(), get_date())


def get_balance():
    if os.path.exists('checkbook.txt'):
        with open('checkbook.txt', 'r') as f:
            return f.read()
    else:
        with open('checkbook.txt', 'w') as f:
            f.write('0.00')
        with open('checkbook.txt', 'r') as f:
            return f.read()



def change_balance(amount):
    with open("checkbook.txt", 'w') as f:
        f.write(str(amount))


def check_input(a):
    return a.isdigit() or a.replace(".", "").isdigit()


def clear_terminal():
    os.system('clear')


def more_options():
    more_questions = input(
        "1) View all balance history\n"
        # "2) View deposit history\n"
        # "3) View withdraw history\n"
    )
    return more_questions



def get_date():
    date_and_time = str(dt.datetime.now())
    date = date_and_time[:10]
    return date

def get_time():
    date_and_time = str(dt.datetime.now())
    time = date_and_time[10:19]
    return time


