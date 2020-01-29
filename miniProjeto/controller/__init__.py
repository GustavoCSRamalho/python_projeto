from flask import Flask, jsonify, abort, make_response, request
from service import Database

def create_app():
    app = Flask(__name__)
    database = Database()

    @app.route('/api/v1.0/execution/all/<int:page_id>', methods=['GET'])
    def allExecution(page_id):
        try:
            data = database.getAllExecution(page_id)
        except Exception as exp:
            return jsonify({}), 400
        
        return jsonify(data), 200

    @app.route('/api/v1.0/execution/<int:execution_id>', methods=['GET'])
    def allExecutionItem(execution_id):
        try:
            data = database.getAllExecutionItem(execution_id)
        except Exception as exp:
            return jsonify({}), 400
        return jsonify(data), 200

    @app.route('/api/v1.0/execution', methods=['POST'])
    def allExecutionItema():
        body = {
            'input':request.json['input'],
            'outputs':request.json['outputs']
        }
        try:
            data = database.createExecution(body)
        except Exception as exp:
            return jsonify({}), 400
        
        return jsonify({}), 201

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error':'Not found'}), 404)

    return app