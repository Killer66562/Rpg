from . import character, skill, gear

class Player(character.Character):
    def __init__(self, name: str, level:int, max_health: int, min_attack: int, max_attack: int, defense: int, min_speed: int, max_speed: int, tease: int, critical_rate: float, critical_damage_bonus: float, max_health_per_level: int, min_attack_per_level: int, max_attack_per_level: int, defense_per_level: float, min_speed_per_level: float, max_speed_per_level: float, tease_per_level: float, critical_rate_per_level: float, critical_damage_bonus_per_level: float, skills:list[skill.Skill] = [], weapon:gear.Weapon = None, helmet:gear.Helmet = None, chestplate:gear.ChestPlate = None, leggings:gear.Leggings = None, boots:gear.Boots = None, necklace:gear.Necklace = None, ring:gear.Ring = None, any_gear:gear.Gear = None) -> None:
        super().__init__(name, max_health, min_attack, max_attack, defense, min_speed, max_speed, tease, critical_rate, critical_damage_bonus, skills)
        self._level:int = level
        self._max_health += max_health_per_level * level
        self._min_attack += int(min_attack_per_level * level)
        self._max_attack += int(max_attack_per_level * level)
        self._defense += int(defense_per_level * level)
        self._min_speed += int(min_speed_per_level * level)
        self._max_speed += int(self._max_speed + max_speed_per_level * level)
        self._tease += int(tease_per_level * level)
        self._critical_rate += critical_rate_per_level * level
        self._critical_damage_bonus += critical_damage_bonus_per_level * level
        self._extra_max_health:int = 0
        self._extra_min_attack:int = 0
        self._extra_max_attack:int = 0
        self._extra_defense:int = 0
        self._extra_min_speed:int = 0
        self._extra_max_speed:int = 0
        self._extra_tease:int = 0
        self._extra_critical_rate:float = 0
        self._extra_critical_damage_bonus:float = 0
        if helmet:
            self._extra_max_health += helmet.max_health
            self._extra_min_attack += helmet.min_attack
            self._extra_max_attack += helmet.max_attack
            self._extra_defense += helmet.defense
            self._extra_min_speed += helmet.min_speed
            self._extra_max_speed += helmet.max_speed
            self._extra_tease += helmet.tease
            self._extra_critical_rate += helmet.critical_rate
            self._extra_critical_damage_bonus += helmet.critical_damage_bonus
        if chestplate:
            self._extra_max_health += chestplate.max_health
            self._extra_min_attack += chestplate.min_attack
            self._extra_max_attack += chestplate.max_attack
            self._extra_defense += chestplate.defense
            self._extra_min_speed += chestplate.min_speed
            self._extra_max_speed += helmet.max_speed
            self._extra_tease += chestplate.tease
            self._extra_critical_rate += chestplate.critical_rate
            self._extra_critical_damage_bonus += chestplate.critical_damage_bonus
        if leggings:
            self._extra_max_health += leggings.max_health
            self._extra_min_attack += leggings.min_attack
            self._extra_max_attack += leggings.max_attack
            self._extra_defense += leggings.defense
            self._extra_min_speed += leggings.min_speed
            self._extra_max_speed += leggings.max_speed
            self._extra_tease += leggings.tease
            self._extra_critical_rate += leggings.critical_rate
            self._extra_critical_damage_bonus += leggings.critical_damage_bonus
        if boots:
            self._extra_max_health += boots.max_health
            self._extra_min_attack += boots.min_attack
            self._extra_max_attack += boots.max_attack
            self._extra_defense += boots.defense
            self._extra_min_speed += boots.min_speed
            self._extra_max_speed += boots.max_speed
            self._extra_tease += boots.tease
            self._extra_critical_rate += boots.critical_rate
            self._extra_critical_damage_bonus += boots.critical_damage_bonus
        if necklace:
            self._extra_max_health += necklace.max_health
            self._extra_min_attack += necklace.min_attack
            self._extra_max_attack += necklace.max_attack
            self._extra_defense += necklace.defense
            self._extra_min_speed += necklace.min_speed
            self._extra_max_speed += necklace.max_speed
            self._extra_tease += necklace.tease
            self._extra_critical_rate += necklace.critical_rate
            self._extra_critical_damage_bonus += necklace.critical_damage_bonus
        if ring:
            self._extra_max_health += ring.max_health
            self._extra_min_attack += ring.min_attack
            self._extra_max_attack += ring.max_attack
            self._extra_defense += ring.defense
            self._extra_min_speed += ring.min_speed
            self._extra_max_speed += ring.max_speed
            self._extra_tease += ring.tease
            self._extra_critical_rate += ring.critical_rate
            self._extra_critical_damage_bonus += ring.critical_damage_bonus
        if weapon:
            self._extra_max_health += weapon.max_health
            self._extra_min_attack += weapon.min_attack
            self._extra_max_attack += weapon.max_attack
            self._extra_defense += weapon.defense
            self._extra_min_speed += weapon.min_speed
            self._extra_max_speed += weapon.max_speed
            self._extra_tease += weapon.tease
            self._extra_critical_rate += weapon.critical_rate
            self._extra_critical_damage_bonus += weapon.critical_damage_bonus
        if any_gear:
            self._extra_max_health += any_gear.max_health
            self._extra_min_attack += any_gear.min_attack
            self._extra_max_attack += any_gear.max_attack
            self._extra_defense += any_gear.defense
            self._extra_min_speed += any_gear.min_speed
            self._extra_max_speed += any_gear.max_speed
            self._extra_tease += any_gear.tease
            self._extra_critical_rate += any_gear.critical_rate
            self._extra_critical_damage_bonus += any_gear.critical_damage_bonus
        self._health = self.max_health

    @property
    def level(self) -> int:
        return self._level
    
    @property
    def extra_max_health(self) -> int:
        return self._extra_max_health
    
    @property
    def extra_min_attack(self) -> int:
        return self._extra_min_attack
    
    @property
    def extra_max_attack(self) -> int:
        return self._extra_max_attack
    
    @property
    def extra_defense(self) -> int:
        return self._extra_defense
    
    @property
    def extra_min_speed(self) -> int:
        return self._extra_min_speed
    
    @property
    def extra_max_speed(self) -> int:
        return self._extra_max_speed
    
    @property
    def extra_tease(self) -> int:
        return self._extra_tease
    
    @property
    def extra_critical_rate(self) -> float:
        return self._extra_critical_rate
    
    @property
    def extra_critical_damage_bonus(self) -> float:
        return self._extra_critical_damage_bonus