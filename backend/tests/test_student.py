def test_add_student(test_client):
    response = test_client.post('/students/', json={"name": "John Doe"})
    assert response.status_code == 201
    assert b"Student added successfully" in response.data

def test_get_students(test_client):
    test_client.post('/students/', json={"name": "Jane Doe"})
    response = test_client.get('/students/')
    assert response.status_code == 200
    assert b"Jane Doe" in response.data

def test_delete_student(test_client):
    test_client.post('/students/', json={"name": "Mark Smith"})
    response = test_client.get('/students/')
    student_id = response.get_json()[0]["id"]

    delete_response = test_client.delete(f'/students/{student_id}')
    assert delete_response.status_code == 200
    assert b"Student deleted successfully" in delete_response.data
