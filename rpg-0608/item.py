from __future__ import annotations
from enum import Enum

class ItemRarity(Enum):
    COMMON = 1
    RARE = 2
    EPIC = 3
    LEGENDARY = 4
    SPECIAL = 0


class Item(object):
    def __init__(self, name:str, rarity:ItemRarity) -> None:
        self._name:str = name
        self._rarity:ItemRarity = rarity.value
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def rarity(self) -> int:
        return self._rarity.value
    

class DropItem(Item):
    def __init__(self, item_id:int, name: str, rarity: ItemRarity, drop_weight: int) -> None:
        super().__init__(name, rarity)
        self._item_id = item_id
        self._drop_weight:int = drop_weight
    
    @property
    def item_id(self) -> int:
        return self._item_id

    @property
    def drop_weight(self):
        return self._drop_weight