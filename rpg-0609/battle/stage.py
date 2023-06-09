from __future__ import annotations
from . import info_container, mob

class Stage(info_container.InfoContainer):
    def __init__(self, min_money: int, max_money: int, min_exp: int, max_exp: int, mobs:list[mob.Mob]) -> None:
        super().__init__(min_money, max_money, min_exp, max_exp)
        self._mobs:list[mob.Mob] = mobs

    @property
    def mobs(self) -> list[mob.Mob]:
        return self._mobs

    @property
    def clear(self):
        return True if len(self.mobs) == 0 else False