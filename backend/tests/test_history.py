def test_get_history(test_client):
    test_client.post('/students/', json={"name": "Alice"})
    test_client.post('/students/', json={"name": "Bob"})
    test_client.post('/pairing/')

    response = test_client.get('/history/')
    assert response.status_code == 200
    assert len(response.get_json()) > 0
