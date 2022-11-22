# import pytest

# import sys




# def test_addathlete(client):

#     response = client.post('/superadmin/addathlete.html', data = {
#         'email':'kelly@gmail.com', 'password':'abcd', 'firstname':'Kelly'
#         , 'lastname':'Putnam','id':1234})

#     text_data = response.get_data(as_text = True)

#     print(response.data)
#     print(type(response.data), type("dfgfd"))

#     assert 'kelly@gmail.com' in text_data
#     assert 'Kelly' in text_data
#     assert 'Putnam' in text_data
#     assert 'abcd' in text_data

#     # user = User.query.filter_by(username='bob').first()
#     # assert user is not None
#     # assert user.email == 'bob@example.com'


# def test_addcoach(client):

#     response = client.post('/superadmin/addcoach.html', data = {
#         'email':'kelly@gmail.com', 'password':'abcd', 'firstname':'Kelly'
#         , 'lastname':'Putnam','id':1234})

#     text_data = response.get_data(as_text = True)

#     print(response.data)

#     assert 'kelly@gmail.com' in text_data
#     assert 'Kelly' in text_data
#     assert 'Putnam' in text_data
#     assert 'abcd' in text_data

# def test_addadmin(client):

#     response = client.post('/superadmin/addpeak.html', data = {
#         'email':'kelly@gmail.com', 'password':'abcd', 'firstname':'Kelly'
#         , 'lastname':'Putnam','id':1234})

#     text_data = response.get_data(as_text = True)

#     print(response.data)

#     assert 'kelly@gmail.com' in text_data
#     assert 'Kelly' in text_data
#     assert 'Putnam' in text_data
#     assert 'abcd' in text_data
