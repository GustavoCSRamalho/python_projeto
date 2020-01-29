from models import Execution,ExecutionItem


def createTables():
    try:
        Execution.create_table()
        print("Tabela 'Execution' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Execution' ja existe!")
    try:
        ExecutionItem.create_table()
        print("Tabela 'ExecutionItem' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'ExecutionItem' ja existe!")

def inserTablesData():
    execution_1 = Execution.create(input='JAN21-A',outputs='none')

    execution_2 = Execution.create(input='JAN21-B',outputs='noneA')

    execution_3 = Execution.create(input='JAN23-C',outputs='nonec')

    executionItem_1 = {
        'status': 'STARTED',
        'params': 'nada',
        'result': '',
        'error': '',
        'execution_id' : execution_1
    }

    executionItem_2 = {
        'status': 'SUCCESS',
        'params': 'nada',
        'result': '',
        'error': '',
        'execution_id' : execution_1
    }

    executionItem_3 = {
        'status': 'STARTED',
        'params': 'nada',
        'result': '',
        'error': '',
        'execution_id' : execution_2
    }

    executionItem_4 = {
        'status': 'STARTED',
        'params': 'nada',
        'result': '',
        'error': '',
        'execution_id' : execution_3
    }
    arrayOfExecutionItens = [executionItem_1,executionItem_2, executionItem_3,executionItem_4]
    
    ExecutionItem.insert_many(arrayOfExecutionItens).execute()