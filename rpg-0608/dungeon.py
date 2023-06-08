from __future__ import annotations
from . import stage, info_container

class Dungeon(info_container.InfoContainer):
    def __init__(self, name:str, min_money: int, max_money: int, min_exp: int, max_exp: int, stages:list[stage.Stage]) -> None:
        super().__init__(min_money, max_money, min_exp, max_exp)
        self._name = name
        self._stages = stages

    @property
    def name(self) -> str:
        return self._name

    @property
    def stages(self) -> list[stage.Stage]:
        return self._stages

    @property
    def clear(self):
        return True if len(self.stages) == 0 else False