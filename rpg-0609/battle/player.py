from . import character, skill, gear

class Player(character.Character):
    def __init__(self, name: str, level:int, max_health: int, min_attack: int, max_attack: int, defense: int, min_speed: int, max_speed: int, tease: int, critical_rate: float, critical_damage_bonus: float, max_health_per_level: int, min_attack_per_level: int, max_attack_per_level: int, defense_per_level: float, min_speed_per_level: float, max_speed_per_level: float, tease_per_level: float, critical_rate_per_level: float, critical_damage_bonus_per_level: float, skills:list[skill.Skill] = [], gears:list[gear.Gear] = []) -> None:
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
        weapon = False
        helmet = False
        chestplate = False
        leggings = False
        boots = False
        necklace = False
        ring = False
        for g in gears:
            if g.gear_type is gear.GearType.WEAPON:
                if weapon:
                    raise Exception()
                weapon = True
            if g.gear_type is gear.GearType.HELMET:
                if helmet:
                    raise Exception()
                helmet = True
            if g.gear_type is gear.GearType.CHESTPLATE:
                if chestplate:
                    raise Exception()
                chestplate = True
            if g.gear_type is gear.GearType.LEGGINGS:
                if leggings:
                    raise Exception()
                leggings = True
            if g.gear_type is gear.GearType.BOOTS:
                if boots:
                    raise Exception()
                boots = True
            if g.gear_type is gear.GearType.NECKLACE:
                if necklace:
                    raise Exception()
                necklace = True
            if g.gear_type is gear.GearType.RING:
                if ring:
                    raise Exception()
                ring = True 
            self._extra_max_health += g.max_health
            self._extra_min_attack += g.min_attack
            self._extra_max_attack += g.max_attack
            self._extra_defense += g.defense
            self._extra_min_speed += g.min_speed
            self._extra_max_speed += g.max_speed
            self._extra_tease += g.tease
            self._extra_critical_rate += g.critical_rate
            self._extra_critical_damage_bonus += g.critical_damage_bonus    
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