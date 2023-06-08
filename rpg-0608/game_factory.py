from . import game, player_factory
from typing import Sequence
from mysql.connector.cursor import CursorBase
from mysql.connector import MySQLConnection

class GameFactory(object):
    def __init__(self, connection:MySQLConnection, cursor:CursorBase) -> None:
        self.__connection:MySQLConnection = connection
        self.__cursor:CursorBase = cursor
        self.__player_factory:player_factory.PlayerFactory = player_factory.PlayerFactory()
        with open("./rpg/sql_scripts/create_character_table.sql", 'r') as file:
            self.__create_c_table:str = file.read()
        
            

    def generate(self, user_id:int,):
        player_factory.PlayerFactory().generate()
