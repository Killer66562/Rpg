from __future__ import annotations
from random import choice
from . import player, dungeon, character, mob, item, game_info

class Game(object):
    def __init__(self, creator_id:int, players:list[player.Player], dungeon:dungeon.Dungeon) -> None:
        self._creator_id:int = creator_id
        self._players:list[player.Player] = players
        self._dungeon:dungeon.Dungeon = dungeon
        self._drop_items:list[item.DropItem] = []

    @property
    def creator_id(self) -> int:
        return self._creator_id
    
    @property
    def players(self) -> list[player.Player]:
        return self._players

    @property
    def dungeon(self) -> dungeon.Dungeon:
        return self._dungeon
    
    @property
    def drop_items(self) -> list[item.DropItem]:
        return self._drop_items
    
    @property
    def all_player_dead(self) -> bool:
        return True if len(self._players) == 0 else False

    def run(self) -> game_info.GameInfo:
        round = 0
        gained_money = 0
        gained_exp = 0
        for stage in self.dungeon.stages:
            while(True):
                round += 1
                order:list[character.Character] = self.players + stage.mobs
                order.sort(key= lambda c : c.speed, reverse=True)
                for chara in order:
                    if isinstance(chara, player.Player):
                        atkinfo = chara.attack(goal=choice(stage.mobs))
                        if atkinfo.defender.is_dead:
                            order.remove(atkinfo.defender)
                            if isinstance(atkinfo.defender, mob.Mob):
                                stage.mobs.remove(atkinfo.defender)
                                d_item = atkinfo.defender.drop_item()
                                if d_item.item_id != 0:
                                    self.drop_items.append(d_item)
                            if stage.clear:
                                gained_money += stage.money
                                gained_exp += stage.exp
                                break
                    elif isinstance(chara, mob.Mob):
                        atkinfo = chara.attack(goal=choice(self.players))
                        if atkinfo.defender.is_dead:
                            order.remove(atkinfo.defender)
                            if isinstance(atkinfo.defender, player.Player):
                                self.players.remove(atkinfo.defender)
                                if self.all_player_dead:
                                    return game_info.GameInfo(gained_money=0, gained_exp=0)
                if stage.clear:
                    break
        return game_info.GameInfo(gained_money=gained_money, gained_exp=gained_exp)

        
