from __future__ import annotations
from . import player, skill, gear, gear_factory
from json import load


class PlayerFactory(object):
    def __init__(self) -> None:
        with open(file= "./rpg/data/characters.json", mode='r', encoding='utf8') as file:
            self.__blueprint:dict = load(file)
        self.__gear_factory: gear_factory.GearFactory = gear_factory.GearFactory()

    def generate(self, p_c_id:str, level:int, skills:list[skill.Skill] = [], gear_id_level_pairs:list[tuple[int,int]] = []) -> player.Player:
        p_c_data = self.__blueprint[p_c_id]
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
        gears = [self.__gear_factory.generate(g_info[0], g_info[1]) for g_info in gear_id_level_pairs]
        return player.Player(name, level, max_health, min_attack, max_attack, defense, min_speed, max_speed, tease, critical_rate, critical_damage_bonus, max_health_per_level, min_attack_per_level, max_attack_per_level, defense_per_level, min_speed_per_level, max_speed_per_level, tease_per_level, critical_rate_per_level, critical_damage_bonus_per_level, skills, gears)
