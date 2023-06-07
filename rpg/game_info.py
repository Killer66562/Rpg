from __future__ import annotations

class GameInfo(object):
    def __init__(self, gained_money:int, gained_exp:int) -> None:
        self.__gained_money = gained_money
        self.__gained_exp = gained_exp

    @property
    def gained_money(self) -> int:
        return self.__gained_money
    
    @property
    def gained_exp(self) -> int:
        return self.__gained_exp