from __future__ import annotations
from json import load
from . import gear, item
from abc import ABCMeta, abstractmethod

class GearFactory(object, metaclass = ABCMeta):
    def __init__(self) -> None:
        with open(file="./rpg/data/gears.json", mode="r", encoding="utf8") as file:
            self.__g_blueprint = load(file)
        with open(file="./rpg/data/items.json", mode="r", encoding="utf8") as file:
            self.__i_blueprint = load(file)

    def generate(self, gear_id:int, level:int) -> gear.Gear:
        item_data = self.__i_blueprint[str(gear_id)]
        gear_data = self.__g_blueprint[str(gear_id)]
        gear_level_data = gear_data[str(level)]
        name = item_data["name"]
        rarity = item_data["rarity"]
        gear_type = gear_data["gear_type"]
        max_health = gear_level_data["max_health"]
        min_attack = gear_level_data["min_attack"]
        max_attack = gear_level_data["max_attack"]
        defense = gear_level_data["defense"]
        min_speed = gear_level_data["min_speed"]
        max_speed = gear_level_data["max_speed"]
        tease = gear_level_data["tease"]
        critical_rate = gear_level_data["critical_rate"]
        critical_damage_bonus = gear_level_data["critical_damage_bonus"]
        return gear.Gear(name, item.ItemRarity(rarity), gear.GearType(gear_type), level, max_health, min_attack, max_attack, defense, min_speed, max_speed, tease, critical_rate, critical_damage_bonus)