
import os
from sqlalchemy import MetaData
from sqlalchemy import (
    insert, select
)
from sqlalchemy.exc import ProgrammingError
from dotenv import load_dotenv

from .PostgresConnector import PostgreSQLConnector
from .postgres_obj.task import Task

load_dotenv("../.env")


class Postgres:
    def __init__(self):
        self.__conn = PostgreSQLConnector()
        self.__metadata = MetaData()
        self.__table_task = Task(self.__metadata )
        
        
        
    def getAll(self):
        try:
            query = self.__table_task.table.select()
            cursor = self.__conn.get_connection().execute(query)
            return cursor.fetchall()
        except ProgrammingError as e:
            raise e
        
        
    def save(self, req):
        print(req)
        try:
            print(req)
            stmt = insert(self.__table_task.table).values(
                title= req.get('title'),
                description = req.get('description'),
                completed = req.get('completed'),
                
            )
            res = self.__conn.get_connection().execute(stmt)
            return res
        except ProgrammingError as e:
            raise e
        
        
    def getById(self, request):
        try:
            print(request)
        except ProgrammingError as e:
            raise e
        
    def delete(self, id):
        try:
            stmt = self.__table_task.table.delete().where(self.__table_task.table.c.id == int(id))
            res = self.__conn.get_connection().execute(stmt)
            print(res)
        except ProgrammingError as e:
            raise e
        
    
