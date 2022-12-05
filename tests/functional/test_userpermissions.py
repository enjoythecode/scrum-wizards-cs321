# import pytest

# import sys




# def test_athletepermissions(client):

#     response = client.post('/superadmin/athletepermissions.html', data = {
#     'deleteaccount':False, 'team':'soccer', 'switchrole':'athlete'})

#     text_data = response.get_data(as_text = True)

#     print(response.data)

#     assert 'soccer' in text_data
#     assert 'athlete' in text_data


# def test_coachpermissions(client):

#     response = client.post('/superadmin/coachpermissions.html', data = {
#         'deleteaccount':False, 'team':'soccer', 'switchrole':'coach'})

#     text_data = response.get_data(as_text = True)

#     print(response.data)

#     assert 'soccer' in text_data
#     assert 'coach' in text_data
