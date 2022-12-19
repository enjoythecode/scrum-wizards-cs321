from flask import Blueprint, Response, request
from . import helper_db
import json
from random import *

api = Blueprint('api', __name__)


def make_database(user_id):
    user = helper_db.getUserById(user_id)
    randnum = random()
    status = "Not Cleared"
    if randnum < 0.7:
        status = ('Cleared')
    elif randnum < 0.9:
        status = ('Partially Cleared')
    return {'user_id' : user_id, 'Name':user.first_name + ' ' + user.last_name, 'status': status}


@api.route('/athletes')
def list_athletes():
    name = request.args.get('name') or ''
    print('helo', request.args.get('name'))
    users = helper_db.getUsers()
    ids = []
    for user in users:
        ids.append(user.id)

    athletes = []

    for id in ids:

        permission_id = helper_db.getUserById(id).permission_id

        if permission_id == 3:
            user = make_database(id)
            print(user, user['Name'])
            if name.lower() in user['Name'].lower():
                athletes.append(user)


    return Response(json.dumps(athletes), mimetype='application/json', status=200)


@api.route('/coaches')
def list_coaches():
    name = request.args.get('name') or ''
    print('helo', request.args.get('name'))
    users = helper_db.getUsers()
    ids = []
    for user in users:
        ids.append(user.id)

    athletes = []

    for id in ids:

        permission_id = helper_db.getUserById(id).permission_id

        if permission_id == 2:
            user = make_database(id)
            print(user, user['Name'])
            if name.lower() in user['Name'].lower():
                athletes.append(user)


    return Response(json.dumps(athletes), mimetype='application/json', status=200)
