from __future__ import annotations
from random import randint, random
from . import atkinfo, skill

class Character(object):
    def __init__(self, name:str, max_health:int, min_attack:int, max_attack:int, defense:int, min_speed:int, max_speed:int, tease:int, critical_rate:float, critical_damage_bonus:float, skills:list[skill.Skill] = []) -> None:
        self._name:str = name
        self._max_health:int = max_health
        self._health:int = max_health
        self._min_attack:int = min_attack
        self._max_attack:int = max_attack
        self._defense:int = defense
        self._min_speed:int = min_speed
        self._max_speed:int = max_speed
        self._tease:int = tease
        self._critical_rate:float = critical_rate
        self._critical_damage_bonus:float = critical_damage_bonus
        self._skills:list[skill.Skill] = skills

    @property
    def name(self) -> str:
        return self._name

    @property
    def max_health(self) -> int:
        return self._max_health
    
    @property
    def health(self) -> int:
        return self._health if self._health > 0 else 0
    
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
    
    @property
    def speed(self):
        return randint(self.min_speed, self.max_speed)
    
    def attack(self, goal:Character) -> atkinfo.AtkInfo:
        damage = randint(self.min_attack, self.max_attack)
        damage = int(damage * self.critical_damage_bonus) if random() < self.critical_rate else damage
        damage = damage if damage > goal.defense else 1
        goal._health -= damage
        return atkinfo.AtkInfo(attacker=self, damage=damage, defender=goal)

    @property
    def is_dead(self) -> bool:
        return self._health <= 0
    
    def use_skills(self) -> None:
        for skill in self._skills:
            skill.use()