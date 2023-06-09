# This is a client side factory using mysql.
# You can create your own factory.

from . import sql_processor, game, player_factory, dungeon_factory, player
from mysql.connector.cursor import CursorBase
from mysql.connector import MySQLConnection

class GameFactory(sql_processor.SQLProcessor):
    def __init__(self, connection: MySQLConnection, cursor: CursorBase) -> None:
        super().__init__(connection, cursor)
        self.__player_factory:player_factory.PlayerFactory = player_factory.PlayerFactory()
        self.__dungeon_factory:dungeon_factory.DungeonFactory = dungeon_factory.DungeonFactory()
    
    def __get_cid_from_uid_and_p_c_id(self, uid: int, p_c_id: int) -> int:
        self._reconnect()
        self._cursor.execute(f"SELECT `cid` FROM rpg.characters WHERE `owner_id` = {uid} AND `character_id` = '{p_c_id}'")
        return int(self._cursor.fetchone()[0])

    def __load_character_level(self, cid:int) -> int:
        self._reconnect()
        self._cursor.execute(f"SELECT `level` FROM rpg.characters WHERE `cid` = {cid}")
        return int(self.__cursor.fetchone()[0])

    def __load_character_gears(self, cid: int) -> list[tuple[int, int]]:
        self._reconnect()
        self._cursor.execute(f"SELECT `gear_id`, `level` FROM rpg.gears WHERE `wearer_id` = {cid}")
        gear_id_level_pairs = self.__cursor.fetchall()
        for p in gear_id_level_pairs:
            p = tuple(int(p[0]), int(p[1]))
        return gear_id_level_pairs

    def generate(self, dc_id:int, p_c_ids:list[int], dungeon_type:str, dungeon_chapter:str, dungeon_id:str):
        players:list[player.Player] = []
        uid = self.get_uid_from_dc_id(dc_id=dc_id)
        for p_c_id in p_c_ids:
            cid = self.__get_cid_from_uid_and_p_c_id(uid=uid, p_c_id=p_c_id)
            p_c_level = self.__load_character_level(cid)
            gear_id_level_paris = self.__load_character_gears(cid)
            players.append(self.__player_factory.generate(p_c_id, p_c_level, [], gear_id_level_paris))
        dungeon = self.__dungeon_factory.generate(dungeon_id=dungeon_id, dungeon_chapter=dungeon_chapter, dungeon_type=dungeon_type)
        return game.Game(creator_id=dc_id, players=players, dungeon=dungeon)
