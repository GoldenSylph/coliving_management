import numpy as np

class UsersDebtsMatrix:

    user_name_to_shape_idx = {}


    def __init__(self, size: int):
        self.data = np.zeros((size, size))


    def populate(self, user_name: str) -> bool:
        if user_name in self.user_name_to_shape_idx:
            return False
        new_shape_index = self.data.shape[0] + 1
        self.data.shape = (self.data.shape[0] + 1, self.data.shape[1] + 1)
        self.user_name_to_shape_idx[user_name] = new_shape_index
        return True


    def add_debt(self, user_name_from: str, user_name_to, amount: str) -> bool:
        if user_name_from not in self.user_name_to_shape_idx
                or user_name_to not in self.user_name_to_shape_idx
                or self.user_name_to_shape_idx[user_name_from]
                        == self.user_name_to_shape_idx[user_name_to]:
            return False
        self.data[
            self.user_name_to_shape_idx[user_name_from],
            self.user_name_to_shape_idx[user_name_to]
        ] += amount
        return True
