from model.users_debts_matrix import UsersDebtsMatrix
from jinja2 import Environment, PackageLoader, select_autoescape

class DebtTable:


    def __init__(self):
        self.env = Environment(
            loader=PackageLoader("main"),
            autoescape=select_autoescape()
        )
        self.template = self.env.get_template("debt_table.md")


    def render(self, data: UsersMatrix):
        ...
