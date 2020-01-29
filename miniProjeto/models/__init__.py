from .baseModel import BaseModel
import peewee
import datetime

class Execution(BaseModel):

    input = peewee.CharField(unique=False)
    outputs = peewee.CharField(unique=False)
    created_at = peewee.DateTimeField(default=datetime.datetime.now)

class ExecutionItem(BaseModel):

    status = peewee.CharField(unique=False)
    params = peewee.CharField(unique=False)
    result = peewee.CharField(unique=False)
    error = peewee.CharField(unique=False)
    started_at = peewee.DateTimeField(default=datetime.datetime.now)
    finished_at = peewee.DateTimeField(null=True)
    execution_id = peewee.ForeignKeyField(Execution)