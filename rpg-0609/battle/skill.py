from __future__ import annotations
from . import character, atkinfo
from abc import ABCMeta, abstractmethod

class Skill(object, metaclass=ABCMeta):
    def __init__(self, owner:character.Character, name:str, level:int) -> None:
        self._owner:character.Character = owner
        self._name:str = name
        self._level:int = level

    @property
    def owner(self) -> character.Character:
        return self._owner
    
    @property
    def level(self) -> int:
        return self._level

    @abstractmethod
    def use(self) -> None:
        pass

