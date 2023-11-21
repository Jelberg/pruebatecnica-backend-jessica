
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv("../.env")


class PostgreSQLConnector:
    def __init__(self):
        self.__connection_string = "postgresql+psycopg2://{}:{}@{}/{}".format(
        os.environ["POSTGRES_USER"],
        os.environ["POSTGRES_PASSWORD"],
        os.environ["POSTGRES_HOSTNAME"],
        os.environ["POSTGRES_DB"])

    
    def getconnlocal(self):
        return create_engine(self.__connection_string)
    

    def get_connection(self):
        print("In use Local connection DB")
        return self.getconnlocal().connect()
