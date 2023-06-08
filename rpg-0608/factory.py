from __future__ import annotations
from abc import ABCMeta, abstractmethod

class Factory(object, metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def generate(self):
        pass