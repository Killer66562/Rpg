from __future__ import annotations
from . import character

class AtkInfo(object):
    def __init__(self, attacker:character.Character, damage:int, defender:character.Character) -> None:
        self.__attacker:character.Character = attacker
        self.__damage:int = damage
        self.__defender:character.Character = defender

    @property
    def attacker(self) -> character.Character:
        return self.__attacker
    
    @property
    def damage(self) -> int:
        return self.__damage
    
    @property
    def defender(self) -> character.Character:
        return self.__defender