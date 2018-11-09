from flask import request, jsonify, Blueprint
from database.db import FootballTable, football_schema, footballs_schema, db


API = Blueprint('api', __name__, static_folder='./static', template_folder='./template')

@API.route('/api', methods=['GET'])
def get_all():
    football = FootballTable.query.order_by(FootballTable.id).all()
    return jsonify(footballs_schema.dump(football))

@API.route('/api/<int:id>', methods=['GET'])
def get_certain(id):
    footballer = FootballTable.query.filter_by(id=id).first()
    return football_schema.jsonify(footballer)


@API.route('/api/<int:id>', methods=['DELETE'])
def delete_certain(id):
    footballer = FootballTable.query.filter_by(id=id).first()

    db.session.delete(footballer)
    db.session.commit()
    return football_schema.jsonify(footballer)

@API.route('/api/<int:id>', methods=['PUT'])
def put_certain(id):
    data = request.get_json(force=True)
    footballer = FootballTable.query.filter_by(id=id).first()

    footballer.age = data.get('age', footballer.age)

    db.session.commit()

    return "Successfylly updated age"

@API.route('/api', methods=['POST'])
def products_post():
    data = request.get_json(force=True)
    new_footballer = FootballTable(**data)

    db.session.add(new_footballer)
    db.session.commit()
    return football_schema.jsonify(new_footballer)
