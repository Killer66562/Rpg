from __future__ import annotations
from . import player, skill, gear, gear_factory
from json import load


class PlayerFactory(object):
    def __init__(self) -> None:
        with open(file= "./rpg/data/characters.json", mode='r', encoding='utf8') as file:
            self.__blueprint:dict = load(file)
        self.__general_gear_factory: gear_factory.GearFactory = gear_factory.GearFactory()
        self.__weapon_factory: gear_factory.WeaponFactory = gear_factory.WeaponFactory()
        self.__helmet_factory: gear_factory.WeaponFactory = gear_factory.HelmetFactory()
        self.__chestplate_factory: gear_factory.WeaponFactory = gear_factory.ChestPlateFactory()
        self.__leggings_factory: gear_factory.WeaponFactory = gear_factory.LeggingsFactory()
        self.__boots_factory: gear_factory.WeaponFactory = gear_factory.BootsFactory()
        self.__necklace_factory: gear_factory.WeaponFactory = gear_factory.NecklaceFactory()
        self.__ring_factory: gear_factory.WeaponFactory = gear_factory.RingFactory()

    @property
    def blueprint(self) -> dict:
        return self.__blueprint
    
    @property
    def general_gear_factory(self):
        return self.__general_gear_factory
    
    @property
    def weapon_factory(self):
        return self.__weapon_factory
    
    @property
    def helmet_factory(self):
        return self.__helmet_factory
    
    @property
    def chestplate_factory(self):
        return self.__chestplate_factory
    
    @property
    def leggings_factory(self):
        return self.__leggings_factory
    
    @property
    def boots_factory(self):
        return self.__boots_factory
    
    @property
    def necklace_factory(self):
        return self.__necklace_factory
    
    @property
    def ring_factory(self):
        return self.__ring_factory

    def generate(self, p_c_id:str, level:int, skills:list[skill.Skill] = [], weapon_id:int = None, weapon_level:int = 1, helmet_id:int = None, helmet_level:int = 1, chestplate_id:int = None, chestplate_level:int = 1, leggings_id:int = None, leggings_level:int = 1, boots_id:int = None, boots_level:int = 1, necklace_id:int = None, necklace_level:int = 1, ring_id:int = None, ring_level:int = 1, any_type_gear_id:int = None, any_type_gear_level:int = 1) -> player.Player:
        p_c_data = self.blueprint[p_c_id]
        name = p_c_data["name"]
        max_health = p_c_data["max_health"]
        min_attack = p_c_data["min_attack"]
        max_attack = p_c_data["max_attack"]
        defense = p_c_data["defense"]
        min_speed = p_c_data["min_speed"]
        max_speed = p_c_data["max_speed"]
        tease = p_c_data["tease"]
        critical_rate = p_c_data["critical_rate"]
        critical_damage_bonus = p_c_data["critical_damage_bonus"]
        max_health_per_level = p_c_data["max_health_per_level"]
        min_attack_per_level = p_c_data["min_attack_per_level"]
        max_attack_per_level = p_c_data["max_attack_per_level"]
        defense_per_level = p_c_data["defense_per_level"]
        min_speed_per_level = p_c_data["min_speed_per_level"]
        max_speed_per_level = p_c_data["max_speed_per_level"]
        tease_per_level = p_c_data["tease_per_level"]
        critical_rate_per_level = p_c_data["critical_rate_per_level"]
        critical_damage_bonus_per_level = p_c_data["critical_damage_bonus_per_level"]
        weapon = self.weapon_factory.generate(gear_id=weapon_id, level=weapon_level) if weapon_id is not None else None        
        helmet = self.helmet_factory.generate(gear_id=helmet_id, level=helmet_level) if helmet_id is not None else None
        chestplate = self.chestplate_factory.generate(gear_id=chestplate_id, level=chestplate_level) if chestplate_id is not None else None
        leggings = self.leggings_factory.generate(gear_id=leggings_id, level=leggings_level) if leggings_id is not None else None
        boots = self.boots_factory.generate(gear_id=boots_id, level=boots_level)if boots_id is not None else None
        necklace = self.necklace_factory.generate(gear_id=necklace_id, level=necklace_level) if necklace_id is not None else None
        ring = self.ring_factory.generate(gear_id=ring_id, level=ring_level) if ring_id is not None else None
        any_gear = self.general_gear_factory.generate(gear_id=any_type_gear_id, level=any_type_gear_level) if any_type_gear_id is not None else None
        return player.Player(name, level, max_health, min_attack, max_attack, defense, min_speed, max_speed, tease, critical_rate, critical_damage_bonus, max_health_per_level, min_attack_per_level, max_attack_per_level, defense_per_level, min_speed_per_level, max_speed_per_level, tease_per_level, critical_rate_per_level, critical_damage_bonus_per_level, skills, weapon, helmet, chestplate, leggings, boots, necklace, ring, any_gear)
