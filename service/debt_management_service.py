from model.users_debts_matrix import UsersDebtsMatrix

class DebtManagementService:


    def __init__(self, data: UsersDebtsMatrix):
        self.data = data


    def calculate(self) -> UsersDebtsMatrix:
        return self.data.data - self.data.data.T
