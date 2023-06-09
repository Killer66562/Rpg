from mysql.connector.cursor import CursorBase
from mysql.connector import MySQLConnection

class SQLProcessor(object):
    def __init__(self, connection:MySQLConnection, cursor:CursorBase) -> None:
        self._connection:MySQLConnection = connection
        self._cursor:CursorBase = cursor
        with open("./rpg/sql_scripts/create_user_table.sql", 'r') as file:
            self._create_u_table_cmd:str = file.read()
        with open("./rpg/sql_scripts/create_item_table.sql", 'r') as file:
            self._create_i_table_cmd:str = file.read()
        with open("./rpg/sql_scripts/create_character_table.sql", 'r') as file:
            self._create_c_table_cmd:str = file.read()
        with open("./rpg/sql_scripts/create_gear_table.sql", 'r') as file:
            self._create_g_table_cmd:str = file.read()
        
    def _reconnect(self):
        try:
            self._connection.reconnect()
        except:
            pass

    # Create a schema named 'rpg' at first.
    # Always initial environment when you start this service!
    def initial_environment(self):
        self._reconnect()
        try:
            self._cursor.execute(self._create_u_table_cmd)
            self._connection.commit()
        except:
            pass
        try:
            self._cursor.execute(self._create_i_table_cmd)
            self._connection.commit()
        except:
            pass
        try:
            self._cursor.execute(self._create_c_table_cmd)
            self._connection.commit()
        except:
            pass
        try:
            self._cursor.execute(self._create_g_table_cmd)
            self._connection.commit()
        except:
            pass

    def _add_user(self, dc_id:int) -> None:
        self._reconnect()
        self._cursor.execute(f"INSERT INTO rpg.users (`dc_id`) ({dc_id})")
        self._connection.commit()

    # Always do this at first no matter what command you use!!!
    def get_uid_from_dc_id(self, dc_id:int) -> int:
        self._reconnect()
        self._cursor.execute(f"SELECT `uid` FROM rpg.users WHERE `dc_id` = {dc_id}")
        if not self._cursor.fetchone():
            self._add_user(dc_id=dc_id)
        return int(self._cursor.fetchone()[0])
    
    def get_character_id_level_pairs(self, uid:int) -> list[tuple[str, int]]:
        self._reconnect()
        self._cursor.execute(f"SELECT `character_id`, `level` FROM rpg.characters WHERE `owner_id` = {uid}")
        pairs = self._cursor.fetchall()
        return [(pair[0], int(pair[1])) for pair in pairs]
    
    def get_money_from_uid(self, uid:int) -> int:
        self._reconnect()
        self._cursor.execute(f"SELECT `money` FROM rpg.users WHERE `uid` = {uid}")
        return int(self._cursor.fetchone()[0])
    
    def add_money_to_uid(self, uid:int, money:int) -> None:
        self._reconnect()
        original_money = self.get_money_from_uid(uid=uid)
        self._cursor.execute(f"UPDATE rpg.users SET `money` = {original_money + money} WHERE `uid` = {uid}")
        self._connection.commit()

    def remove_money_from_uid(self, uid:int, money:int) -> None:
        self._reconnect()
        original_money = self.get_money_from_uid(uid=uid)
        self._cursor.execute(f"UPDATE rpg.users SET `money` = {original_money - money} WHERE `uid` = {uid}")
        self._connection.commit()

    def get_level_from_uid(self, uid:int) -> int:
        self._reconnect()
        self._cursor.execute(f"SELECT `level` FROM rpg.users WHERE `uid` = {uid}")
        return int(self._cursor.fetchone()[0])

    def get_exp_from_uid(self, uid:int) -> int:
        self._reconnect()
        self._cursor.execute(f"SELECT `exp` FROM rpg.users WHERE `uid` = {uid}")
        return int(self._cursor.fetchone()[0])
    
    def add_exp_to_uid(self, uid:int, exp:int) -> None:
        self._reconnect()
        original_money = self.get_money_from_uid(uid=uid)
        self._cursor.execute(f"UPDATE rpg.users SET `exp` = {original_money + exp} WHERE `uid` = {uid}")
        self._connection.commit()

    def remove_exp_from_uid(self, uid:int, exp:int) -> None:
        self._reconnect()
        original_money = self.get_money_from_uid(uid=uid)
        self._cursor.execute(f"UPDATE rpg.users SET `exp` = {original_money - exp} WHERE `uid` = {uid}")
        self._connection.commit()

    def upgradable(self, uid:int) -> bool:
        self._reconnect()
        level = self.get_level_from_uid(uid=uid)
        exp = self.get_exp_from_uid(uid=uid)
        return (exp >= level * 100)

    def upgrade_from_uid(self, uid:int) -> None:
        self._reconnect()
        level = self.get_level_from_uid(uid=uid)
        self.remove_exp_from_uid(uid=uid, exp=level*100)
        self._cursor.execute(f"UPDATE rpg.users SET `level` = {level+1} WHERE `uid` = {uid}")
        self._connection.commit()

    

    

    

    