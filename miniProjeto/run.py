import os

from controller import create_app
from utils.bancoDeDados import createTables, inserTablesData

app = create_app()

if __name__ == '__main__':
    createTables()
    inserTablesData()

    app.run()