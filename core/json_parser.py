from datetime import date, time
import json
from typing import Optional

from models import BaseTransaction, Subpayer, User


class Parser:
    
    def __init__(self, users: dict[str, User]) -> None:
        self.users = users


    def get_payers(self, data: dict) -> list[Subpayer]:
        payers: list[dict] = data['payers']
        subpayers: list[Subpayer] = []
        for payer in payers:
            user = self.users[payer['payer']]
            
            sum_ = payer.get('sum_')
            sum_ = float(sum_) if not sum_ is None else sum_
            sp = Subpayer(
                    user=user,
                    sum_=sum_,
                )
            subpayers.append(sp)
        return subpayers

    def get_time(self, data: dict) -> time:
        return time.fromisoformat(data['payment_time'])

    def get_date(self, data: dict) -> date:
        return date.fromisoformat(data['payment_date'])

    def get_main_payer(self, data: dict) -> User:
        return self.users[data['payer']]

    def get_bill(self, data: dict) -> float:
        return float(data['bill'])

    def get_description(self, data: dict) -> Optional[str]:
        return data['description']
    
    def get_transaction(self, filepath: str) -> BaseTransaction:
        data = read_json(filepath)
        return BaseTransaction(
            payment_date=self.get_date(data),
            payment_time=self.get_time(data),
            payer=self.get_main_payer(data),
            bill=self.get_bill(data),
            add_payers=self.get_payers(data),
            description=self.get_description(data),
        )

    
def read_json(filepath: str) -> dict:
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data