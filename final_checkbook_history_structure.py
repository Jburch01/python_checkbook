import csv
import os
from prettytable import *

cols = ['category', 'description', 'amount', 'balance', 'time', 'date']
transaction = {}


def create_csv():
    with open('checkbookHistory.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=cols)
        writer.writeheader()


def add_history(amount, descript, category, balance, time, date):
    transaction["amount"] = amount
    transaction["description"] = descript
    transaction["category"] = category
    transaction["balance"] = balance
    transaction['time'] = time
    transaction['date'] = date
    with open('checkbookHistory.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=cols)
        writer.writerow(transaction)


def get_history():
    if os.path.exists('checkbookHistory.csv'):
        pass
    else:
        create_csv()
    with open("checkbookHistory.csv") as fp:
        table = from_csv(fp)
    print(table)


def search(category):
    with open('checkbookHistory.csv', 'r') as file:
        history = csv.reader(file)
        table = PrettyTable(next(history))
        for row in history:
            if row[0] == category:
                table.add_row(row)
        print(table)



