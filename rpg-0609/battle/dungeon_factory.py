from __future__ import annotations
from . import dungeon, stage, mob
from json import load
from random import choices

class DungeonFactory(object):
    def __init__(self) -> None:
        pass

    def generate(self, dungeon_type:str, dungeon_chapter:str, dungeon_id:str) -> dungeon.Dungeon:
        with open(file=f"./rpg/data/dungeons/{dungeon_type}/{dungeon_chapter}/{dungeon_id}.json", mode='r', encoding='utf8') as file:
            dungeon_data = load(file)
        mobs_data:dict = dungeon_data["mobs"]
        stages_data:dict = dungeon_data["stages"]
        main_data:dict = dungeon_data["main"]
        dungeon_name = main_data["name"]
        dungeon_min_money = main_data["min_money"]
        dungeon_max_money = main_data["max_money"]
        dungeon_min_exp = main_data["min_exp"]
        dungeon_max_exp = main_data["max_exp"]
        stage_ids:list[str] = main_data["stages"]
        stages:list[stage.Stage] = []
        for stage_id in stage_ids:
            stage_min_money = stages_data[stage_id]["min_money"]
            stage_max_money = stages_data[stage_id]["max_money"]
            stage_min_exp = stages_data[stage_id]["min_exp"]
            stage_max_exp = stages_data[stage_id]["max_exp"]
            mob_count = stages_data[stage_id]["mob_count"]
            mob_data_of_stage:dict = stages_data[stage_id]["mobs"]
            mobs:list[mob.Mob] = []
            for mob_id in mob_data_of_stage.keys():
                name:str = mobs_data[mob_id]["name"]
                max_health:int = mobs_data[mob_id]["max_health"]
                min_attack:int = mobs_data[mob_id]["min_attack"]
                max_attack:int = mobs_data[mob_id]["max_attack"]
                defense:int = mobs_data[mob_id]["defense"]
                min_speed:int = mobs_data[mob_id]["min_speed"]
                max_speed:int = mobs_data[mob_id]["max_speed"]
                tease: int = mobs_data[mob_id]["tease"]
                critical_rate: float = mobs_data[mob_id]["critical_rate"]
                critical_damage_bonus: float = mobs_data[mob_id]["critical_damage_bonus"]
                mobs.append(mob.Mob(mob_id, name, max_health, min_attack, max_attack, defense, min_speed, max_speed, tease, critical_rate, critical_damage_bonus, [], []))
            stages.append(stage.Stage(stage_min_money, stage_max_money, stage_min_exp, stage_max_exp, choices(population=mobs, weights=[mob_data_of_stage[m.mob_id] for m in mobs], k=mob_count)))
        return dungeon.Dungeon(name=dungeon_name, min_money=dungeon_min_money, max_money=dungeon_max_money, min_exp=dungeon_min_exp, max_exp=dungeon_max_exp, stages=stages)
    

        
