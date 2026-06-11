from project import app

client = app.test_client()

def test_client():
     index = client.get("/")
     assert index.status_code == 200

     list = client.get("/list")
     assert list.status_code == 200

def test_add():
     add = client.post("/", data={"item": "avocado", "quantity": "1", "action": "add"})
     assert add.status_code == 204

     list_response = client.get("/list")
     assert b"avocado" in list_response.data

def test_check():
     check = client.post("/", data={"item": "avocado", "quantity": "1", "action": "check"})
     response = client.get("/")
     assert b"avocado" in response.data and b"Checked" in response.data
