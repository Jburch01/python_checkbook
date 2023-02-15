import csv
import os
from prettytable import from_csv

cols = ['category', 'amount', 'balance', 'time', 'date']
transaction = {}


def create_csv():
    with open('checkbookHistory.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=cols)
        writer.writeheader()


def add_history(amount, category, balance, time, date):
    transaction["amount"] = amount
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





