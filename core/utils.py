from config import USERS
from graph import Graph
from json_parser import Parser
from models import BaseTransaction
import numpy as np
from datetime import date, time
from models import BaseTransaction, User, Subpayer
import os


def calculate_payments(transactions: list[BaseTransaction]) -> dict[str, float]:
    current_graph = Graph()
    for transaction in transactions:
        current_graph.process_one_transaction(transaction)

    subres = current_graph.adj_matrix - current_graph.adj_matrix.T
    res = np.sum(subres, axis=1)

    return {user.name: float(res[index]) for index, user in current_graph.users.values()}


def get_all_transactions() -> list[BaseTransaction]:
    datadir = 'data'
    parser = Parser(USERS)
    transactions = []
    for month in os.listdir(datadir):
        month_dir = os.path.join(datadir, month)
        for day in os.listdir(month_dir):
            day_dir = os.path.join(month_dir, day)
            for file in os.listdir(day_dir):
                filepath = os.path.join(day_dir, file)
                transaction = parser.get_transaction(filepath)
                transactions.append(transaction)
    return transactions


def calculate_per_day():
    datadir = 'data'
    parser = Parser(USERS)
    for month in os.listdir(datadir):
        month_dir = os.path.join(datadir, month)
        for day in os.listdir(month_dir):
            day_dir = os.path.join(month_dir, day)
            transactions = []
            for file in os.listdir(day_dir):
                filepath = os.path.join(day_dir, file)
                transaction = parser.get_transaction(filepath)
                transactions.append(transaction)
            res = calculate_payments(transactions)
            print(month, day, res)


def calculate_whole():
    transactions = get_all_transactions()
    res = calculate_payments(transactions)
    print(res)