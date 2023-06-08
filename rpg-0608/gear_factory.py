from __future__ import annotations
from json import load
from . import gear, item
from abc import ABCMeta, abstractmethod

class GearFactory(object, metaclass = ABCMeta):
    def __init__(self) -> None:
        with open(file="./rpg/data/gears.json", mode="r", encoding="utf8") as file:
            self._blueprint = load(file)

    @property
    def blueprint(self) -> dict:
        return self._blueprint

    def generate(self, gear_id:str, level:int) -> gear.Gear:
        gear_data = self.blueprint[gear_id][str(level)]
        name = gear_data["name"]
        rarity = gear_data["rarity"]
        max_health = gear_data["max_health"]
        min_attack = gear_data["min_attack"]
        max_attack = gear_data["max_attack"]
        defense = gear_data["defense"]
        min_speed = gear_data["min_speed"]
        max_speed = gear_data["max_speed"]
        tease = gear_data["tease"]
        critical_rate = gear_data["critical_rate"]
        critical_damage_bonus = gear_data["critical_damage_bonus"]
        return gear.Gear(name, item.ItemRarity(rarity), level, max_health, min_attack, max_attack, defense, min_speed, max_speed, tease, critical_rate, critical_damage_bonus)

class WeaponFactory(GearFactory):
    def __init__(self) -> None:
        super().__init__()

    def generate(self, gear_id:str, level:int) -> gear.Weapon:
        gear_data = self.blueprint[gear_id][str(level)]
        name = gear_data["name"]
        rarity = gear_data["rarity"]
        max_health = gear_data["max_health"]
        min_attack = gear_data["min_attack"]
        max_attack = gear_data["max_attack"]
        defense = gear_data["defense"]
        min_speed = gear_data["min_speed"]
        max_speed = gear_data["max_speed"]
        tease = gear_data["tease"]
        critical_rate = gear_data["critical_rate"]
        critical_damage_bonus = gear_data["critical_damage_bonus"]
        return gear.Weapon(name, item.ItemRarity(rarity), level, max_health, min_attack, max_attack, defense, min_speed, max_speed, tease, critical_rate, critical_damage_bonus)
    
class HelmetFactory(GearFactory):
    def __init__(self) -> None:
        super().__init__()

    def generate(self, gear_id:str, level:int) -> gear.Helmet:
        gear_data = self.blueprint[gear_id][str(level)]
        name = gear_data["name"]
        rarity = gear_data["rarity"]
        max_health = gear_data["max_health"]
        min_attack = gear_data["min_attack"]
        max_attack = gear_data["max_attack"]
        defense = gear_data["defense"]
        min_speed = gear_data["min_speed"]
        max_speed = gear_data["max_speed"]
        tease = gear_data["tease"]
        critical_rate = gear_data["critical_rate"]
        critical_damage_bonus = gear_data["critical_damage_bonus"]
        return gear.Helmet(name, item.ItemRarity(rarity), level, max_health, min_attack, max_attack, defense, min_speed, max_speed, tease, critical_rate, critical_damage_bonus)
    
class ChestPlateFactory(GearFactory):
    def __init__(self) -> None:
        super().__init__()

    def generate(self, gear_id:str, level:int) -> gear.ChestPlate:
        gear_data = self.blueprint[gear_id][str(level)]
        name = gear_data["name"]
        rarity = gear_data["rarity"]
        max_health = gear_data["max_health"]
        min_attack = gear_data["min_attack"]
        max_attack = gear_data["max_attack"]
        defense = gear_data["defense"]
        min_speed = gear_data["min_speed"]
        max_speed = gear_data["max_speed"]
        tease = gear_data["tease"]
        critical_rate = gear_data["critical_rate"]
        critical_damage_bonus = gear_data["critical_damage_bonus"]
        return gear.ChestPlate(name, item.ItemRarity(rarity), level, max_health, min_attack, max_attack, defense, min_speed, max_speed, tease, critical_rate, critical_damage_bonus)
    
class LeggingsFactory(GearFactory):
    def __init__(self) -> None:
        super().__init__()

    def generate(self, gear_id:str, level:int) -> gear.Leggings:
        gear_data = self.blueprint[gear_id][str(level)]
        name = gear_data["name"]
        rarity = gear_data["rarity"]
        max_health = gear_data["max_health"]
        min_attack = gear_data["min_attack"]
        max_attack = gear_data["max_attack"]
        defense = gear_data["defense"]
        min_speed = gear_data["min_speed"]
        max_speed = gear_data["max_speed"]
        tease = gear_data["tease"]
        critical_rate = gear_data["critical_rate"]
        critical_damage_bonus = gear_data["critical_damage_bonus"]
        return gear.Leggings(name, item.ItemRarity(rarity), level, max_health, min_attack, max_attack, defense, min_speed, max_speed, tease, critical_rate, critical_damage_bonus)
    
class BootsFactory(GearFactory):
    def __init__(self) -> None:
        super().__init__()

    def generate(self, gear_id:str, level:int) -> gear.Boots:
        gear_data = self.blueprint[gear_id][str(level)]
        name = gear_data["name"]
        rarity = gear_data["rarity"]
        max_health = gear_data["max_health"]
        min_attack = gear_data["min_attack"]
        max_attack = gear_data["max_attack"]
        defense = gear_data["defense"]
        min_speed = gear_data["min_speed"]
        max_speed = gear_data["max_speed"]
        tease = gear_data["tease"]
        critical_rate = gear_data["critical_rate"]
        critical_damage_bonus = gear_data["critical_damage_bonus"]
        return gear.Boots(name, item.ItemRarity(rarity), level, max_health, min_attack, max_attack, defense, min_speed, max_speed, tease, critical_rate, critical_damage_bonus)
    
class NecklaceFactory(GearFactory):
    def __init__(self) -> None:
        super().__init__()

    def generate(self, gear_id:str, level:int) -> gear.Necklace:
        gear_data = self.blueprint[gear_id][str(level)]
        name = gear_data["name"]
        rarity = gear_data["rarity"]
        max_health = gear_data["max_health"]
        min_attack = gear_data["min_attack"]
        max_attack = gear_data["max_attack"]
        defense = gear_data["defense"]
        min_speed = gear_data["min_speed"]
        max_speed = gear_data["max_speed"]
        tease = gear_data["tease"]
        critical_rate = gear_data["critical_rate"]
        critical_damage_bonus = gear_data["critical_damage_bonus"]
        return gear.Necklace(name, item.ItemRarity(rarity), level, max_health, min_attack, max_attack, defense, min_speed, max_speed, tease, critical_rate, critical_damage_bonus)
    
class RingFactory(GearFactory):
    def __init__(self) -> None:
        super().__init__()

    def generate(self, gear_id:str, level:int) -> gear.Ring:
        gear_data = self.blueprint[gear_id][str(level)]
        name = gear_data["name"]
        rarity = gear_data["rarity"]
        max_health = gear_data["max_health"]
        min_attack = gear_data["min_attack"]
        max_attack = gear_data["max_attack"]
        defense = gear_data["defense"]
        min_speed = gear_data["min_speed"]
        max_speed = gear_data["max_speed"]
        tease = gear_data["tease"]
        critical_rate = gear_data["critical_rate"]
        critical_damage_bonus = gear_data["critical_damage_bonus"]
        return gear.Ring(name, item.ItemRarity(rarity), level, max_health, min_attack, max_attack, defense, min_speed, max_speed, tease, critical_rate, critical_damage_bonus)
    