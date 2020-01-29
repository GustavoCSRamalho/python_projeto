from models import Execution,ExecutionItem
from playhouse.shortcuts import model_to_dict, dict_to_model
import json
class Database():
        
    def getAllExecution(self, page_id):
        values = Execution.select().paginate(page_id,2)
        arrayOfData = [model_to_dict(book) for book in values]
        return arrayOfData

    def getAllExecutionItem(self, execution_id):
        values = ExecutionItem.select(
            ExecutionItem.id,
            ExecutionItem.status,
            ExecutionItem.params,
            ExecutionItem.result,
            ExecutionItem.error,
            ExecutionItem.started_at,
            ExecutionItem.finished_at
        ).join(Execution).where(Execution.id == execution_id)
        arrayOfData = [model_to_dict(book) for book in values]
        return arrayOfData
        
    def createExecution(self, body):
        print(body['outputs'])
        return Execution.create(input=body['input'],outputs=body['outputs'])
       