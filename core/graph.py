import numpy as np
from numpy import ndarray

from models import User, BaseTransaction

def pad_matrix(arr: np.ndarray) -> np.ndarray:
    return np.array([[0]]) if len(arr.shape) == 1 else np.pad(arr, ((0, 1), (0, 1)))


class Graph:

    def __init__(self) -> None:
        self.adj_matrix: ndarray = np.array([])
        self.users: dict[int, tuple[int, User]] = {}

    def add_user_if_not_in(self, user: User) -> None:
        if user.id_ not in self.users:
            self.users[user.id_] = (len(self.users), user)
            self.adj_matrix = pad_matrix(self.adj_matrix)

    def add_bill(self, user_a: User, user_b: User, sum_: float) -> None:
        index_a = self.users[user_a.id_][0]
        index_b = self.users[user_b.id_][0]
        self.adj_matrix[index_a, index_b] += sum_
    
    def process_one_transaction(self, transaction: BaseTransaction) -> None:
        self.add_user_if_not_in(transaction.payer)
        transaction.recalculate_bills()
        for add_payer in transaction.add_payers:
            self.add_user_if_not_in(add_payer.user)
            self.add_bill(transaction.payer, add_payer.user, add_payer.sum_)