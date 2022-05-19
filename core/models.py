from datetime import time, date
from typing import Optional
from pydantic import BaseModel, validator


class User(BaseModel):
    id_: int
    name: str


class Subpayer(BaseModel):
    user: User
    sum_: Optional[float] = None

    def set_sum(self, new_sum: float) -> None:
        if self.sum_ is None:
            self.sum_ = new_sum

    @validator('sum_')
    def check_sum(cls, v: float) -> float:
        if v and v < 0:
            raise ValueError(f'Invalid sum: {v}. Every payment must be positive')
        return v

class BaseTransaction(BaseModel):
    payment_date: date
    payment_time: time
    payer: User
    bill: float
    add_payers: list[Subpayer]
    description: Optional[str]

    def recalculate_bills(self) -> None:
        payers_num = sum(payer.sum_ is None for payer in self.add_payers)
        if not payers_num:
            return

        payers_bills_sum = sum(payer.sum_ for payer in self.add_payers if payer.sum_ is not None)
        res = self.bill - payers_bills_sum

        bill_from_every_user = res / payers_num

        for payer in self.add_payers:
            payer.set_sum(bill_from_every_user)

    @validator('add_payers')
    def check_payers_sum(cls, v: list[Subpayer], values, **kwargs) -> list[Subpayer]:
        payers_bills_sum = sum(payer.sum_ for payer in v if payer.sum_ is not None)
        if not sum(payer.sum_ is None for payer in v):
            if payers_bills_sum != values['bill']:
                msg = f'Sum of payments {payers_bills_sum} does not match whole bill {values["bill"]}, date={values["payment_date"]}'
                raise ValueError(msg)
        if payers_bills_sum > values['bill']:
            raise ValueError('Sum of payers is more than whole pay')
        return v
    
