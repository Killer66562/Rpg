from __future__ import annotations
from . import item
from enum import Enum

class GearType(Enum):
    WEAPON = "weapon"
    HELMET = "helmet"
    CHESTPLATE = "chestplate"
    LEGGINGS = "leggings"
    BOOTS = "boots"
    NECKLACE = "necklace"
    RING = "ring"

class Gear(item.Item):
    def __init__(self, name:str, rarity:item.ItemRarity, gear_type:GearType, level:int, max_health:int, min_attack:int, max_attack:int, defense:int, min_speed:int, max_speed:int, tease:int, critical_rate:float, critical_damage_bonus:float) -> None:
        super().__init__(name, rarity)
        self._gear_type:GearType = gear_type
        self._level:int = level
        self._max_health:int = max_health
        self._min_attack:int = min_attack
        self._max_attack:int = max_attack
        self._defense:int = defense
        self._min_speed:int = min_speed
        self._max_speed:int = max_speed
        self._tease:int = tease
        self._critical_rate:float = critical_rate
        self._critical_damage_bonus:float = critical_damage_bonus

    @property
    def gear_type(self) -> GearType:
        return self._gear_type

    @property
    def level(self) -> int:
        return self._level

    @property
    def max_health(self) -> int:
        return self._max_health
    
    @property
    def min_attack(self) -> int:
        return self._min_attack
    
    @property
    def max_attack(self) -> int:
        return self._max_attack
    
    @property
    def defense(self) -> int:
        return self._defense
    
    @property
    def min_speed(self) -> int:
        return self._min_speed
    
    @property
    def max_speed(self) -> int:
        return self._max_speed
    
    @property
    def tease(self) -> int:
        return self._tease
    
    @property
    def critical_rate(self) -> float:
        return self._critical_rate
    
    @property
    def critical_damage_bonus(self) -> float:
        return self._critical_damage_bonus
    
