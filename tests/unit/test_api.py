from website import api, addDummyUserList, addDummyUser

def test_getStatus(client):
    status = api.getStatus()

    assert status == "Not Cleared" or status == "Cleared" or status == "Partially Cleared"


def test_filter_by_permission(client):
    addDummyUser()

    assert api.filter_by_permission(0, "Chandra")[0]["Name"] == "Chandra Gowda"
    assert api.filter_by_permission(1, "Sinan")[0]["Name"] == "Sinan Yumurtaci"
    assert api.filter_by_permission(3, "Jasper")[0]["Name"] == "Jasper Loverude"
