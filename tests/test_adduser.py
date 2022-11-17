from website import models


def test_adduser():
    email = 'ben@gmail.com'
    password = 'somepassword'
    first_name = 'ben'
    last_name = 'putnam'
    permission_id = 0
    id = 736259

    user = models.User(email = email, password = password, first_name = first_name, last_name = last_name, permission_id = permission_id, id = id)

    assert user.email == 'ben@gmail.com'
    assert user.password == 'somepassword'
    assert user.first_name == 'ben'
    assert user.last_name == 'putnam'
    assert user.permission_id == 0
    assert user.id == 736259

