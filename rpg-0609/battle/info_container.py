from __future__ import annotations
from random import randint

class InfoContainer(object):
    def __init__(self, min_money:int, max_money:int, min_exp:int, max_exp:int) -> None:
        self._min_money = min_money
        self._max_money = max_money
        self._min_exp = min_exp
        self._max_exp = max_exp

    @property
    def min_money(self) -> int:
        return self._min_money
    
    @property
    def max_money(self) -> int:
        return self._max_money
    
    @property
    def min_exp(self) -> int:
        return self._min_exp
    
    @property
    def max_exp(self) -> int:
        return self._max_exp
    
    @property
    def money(self) -> int:
        return randint(min(self.min_money, self.max_money), max(self.min_money, self.max_money))
    
    @property
    def exp(self) -> int:
        return randint(min(self.min_exp, self.max_exp), max(self.min_exp, self.max_exp))