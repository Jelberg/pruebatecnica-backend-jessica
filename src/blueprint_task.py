
from flask import Blueprint, Response, request, abort, jsonify
from postgres.Postgres import Postgres
from serializers.TaskSchema import TaskSchema
from marshmallow import ValidationError

task_routes_blueprint = Blueprint('task_routes_blueprint', __name__ )


@task_routes_blueprint.route('/health')
def health()-> Response:
    """This is a health endpoint"""
    return 'Hello John Doe, everything is OK '

@task_routes_blueprint.route('/get-all', methods=['GET'])
def get_all():
    response = Postgres().getAll()
    return jsonify(response)

@task_routes_blueprint.route('/save', methods=['POST'])
def save():
    try:
        task_schema =  TaskSchema()
        data = task_schema.dump(request.get_json())
        print(data)
        req = request.get_json()
        response = Postgres().save(req)
        return jsonify('')
    except ValidationError as error:
        print(error.message)
        return jsonify({'error': error.messages}), 400

@task_routes_blueprint.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    print(id)
    req = request.get_json()
    response = Postgres().delete(id)
    return jsonify('')