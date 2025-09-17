from peewee import *
import datetime
import os

if not os.path.exists("data"):
    os.makedirs("data")
    
db = SqliteDatabase("data/ids.db")

class BaseModel(Model):
    class Meta:
        database = db

class Alerta(BaseModel):
    tipo = CharField()
    host = CharField()
    severidad = IntegerField()
    timestamp = DateTimeField(default=datetime.datetime.now)
