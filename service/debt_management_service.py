from model.users_debts_matrix import UsersDebtsMatrix

class DebtManagementService:


    def __init__(self, data: UsersMatrix):
        self.data = data


    def calculate(self) -> UsersMatrix:
        ...
