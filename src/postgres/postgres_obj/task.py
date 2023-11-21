from sqlalchemy import Column, String, Integer, Table, MetaData, Boolean

class Task:
    def __init__(self, metadata):
        self.table = Table('task', metadata,
            Column('id', Integer, primary_key=True ),
            Column('title', String),
            Column('description', String),
            Column('completed', Boolean),
            )