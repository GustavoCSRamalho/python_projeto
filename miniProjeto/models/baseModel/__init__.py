import peewee
db = peewee.SqliteDatabase('bancoDeDados.db')
class BaseModel(peewee.Model):
    class Meta:
        database = db