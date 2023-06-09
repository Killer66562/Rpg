from mysql.connector import MySQLConnection
from . import game_info, sql_processor
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import CursorBase

class GameInfoProcessor(sql_processor.SQLProcessor):
    def __init__(self, connection: MySQLConnection, cursor: CursorBase) -> None:
        super().__init__(connection, cursor)

    def add_money_and_exp(self, dc_id:int, gameinfo:game_info.GameInfo) -> None:
        if not gameinfo.success:
            return
        uid = self.get_uid_from_dc_id(dc_id=dc_id)
        self.add_money_to_uid(uid=uid, money=gameinfo.gained_money)
        self.add_exp_to_uid(uid=uid, exp=gameinfo.gained_exp)

        

