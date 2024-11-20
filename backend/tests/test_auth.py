def test_register(test_client):
    # Test user registration
    response = test_client.post('/auth/register', json={
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "password123"
    })
    assert response.status_code == 201
    assert b"User registered successfully" in response.data

def test_register_duplicate_email(test_client):
    # Test duplicate email registration
    test_client.post('/auth/register', json={
        "username": "user1",
        "email": "duplicate@example.com",
        "password": "password123"
    })
    response = test_client.post('/auth/register', json={
        "username": "user2",
        "email": "duplicate@example.com",
        "password": "password456"
    })
    assert response.status_code == 400
    assert b"Email already registered" in response.data

def test_login_successful(test_client):
    # Test successful login
    test_client.post('/auth/register', json={
        "username": "loginuser",
        "email": "loginuser@example.com",
        "password": "password123"
    })
    response = test_client.post('/auth/login', json={
        "email": "loginuser@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert b"token" in response.data

def test_login_invalid_credentials(test_client):
    # Test login with invalid credentials
    response = test_client.post('/auth/login', json={
        "email": "invalid@example.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert b"Invalid credentials" in response.data
