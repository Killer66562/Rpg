from __future__ import annotations
from . import item, character, skill, player
from random import choices

class Mob(character.Character):
    def __init__(self, mob_id:str, name: str, max_health: int, min_attack: int, max_attack: int, defense: int, min_speed: int, max_speed: int, tease: int, critical_rate: float, critical_damage_bonus: float, skills: list[skill.Skill] = [], drop_items:list[item.DropItem] = []) -> None:
        super().__init__(name, max_health, min_attack, max_attack, defense, min_speed, max_speed, tease, critical_rate, critical_damage_bonus, skills)
        self._mob_id = mob_id
        self._drop_items = drop_items

    @property
    def mob_id(self) -> str:
        return self._mob_id

    def drop_item(self) -> item.DropItem:
        return choices(population=self._drop_items, weights=[d_item.drop_weight for d_item in self._drop_items], k=1) if len(self._drop_items) > 0 else item.DropItem(item_id=0, name="", rarity=item.ItemRarity.SPECIAL, drop_weight=0)