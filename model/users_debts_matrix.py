import numpy as np

class UsersDebtsMatrix:

    user_id_to_shape_idx = {}


    def __init__(self, size):
        self.data = np.zeros((size, size))


    def populate(self, user_id):
        new_shape_index = self.data.shape[0] + 1
        self.data.shape = (self.data.shape[0] + 1, self.data.shape[1] + 1)
        self.user_id_to_shape_idx[user_id] = new_shape_index


    def add_debt(self, user_id_from, user_id_to, amount) -> bool:
        if user_id_from not in self.user_id_to_shape_idx
                or user_id_to not in self.user_id_to_shape_idx
                or self.user_id_to_shape_idx[user_id_from]
                        == self.user_id_to_shape_idx[user_id_to]:
            return False
        self.data[
            self.user_id_to_shape_idx[user_id_from],
            self.user_id_to_shape_idx[user_id_to]
        ] = amount
        return True
