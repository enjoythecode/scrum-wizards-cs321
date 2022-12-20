from flask import Blueprint, Response, request
from . import helper_db
import json
from random import randrange

api = Blueprint('api', __name__)

def getStatus():
    randnum = randrange(1, 11)
    status = "Not Cleared"
    if randnum < 8:
        status = ('Cleared')
    elif randnum < 10:
        status = ('Partially Cleared')

    return status

def filter_by_permission(permission_id, name = ''):
    users = helper_db.getUsers()

    athletes = []

    for user in users:

        if user.permission_id == permission_id:
            updated_user = {'user_id' : user.id, 'Name':user.first_name + ' ' + user.last_name, 'status': getStatus()}
            if name.lower() in updated_user['Name'].lower():
                athletes.append(updated_user)

    return athletes


@api.route('/athletes')
def list_athletes():
    name = request.args.get('name') or ''
    athletes = filter_by_permission(3, name)
    return Response(json.dumps(athletes), mimetype='application/json', status=200)

@api.route('/coaches')
def list_coaches():
    name = request.args.get('name') or ''
    coaches = filter_by_permission(2, name)
    return Response(json.dumps(coaches), mimetype='application/json', status=200)
