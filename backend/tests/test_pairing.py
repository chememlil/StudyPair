def test_pair_students(test_client):
    test_client.post('/students/', json={"name": "Alice"})
    test_client.post('/students/', json={"name": "Bob"})
    test_client.post('/students/', json={"name": "Charlie"})
    test_client.post('/students/', json={"name": "Daisy"})

    response = test_client.post('/pairing/')
    assert response.status_code == 200
    assert b"Pairs generated successfully" in response.data
