import pytest
from flask import Flask
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_ip_remote_addr(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == '127.0.0.1'

def test_get_ip_cf_connecting_ip(client):
    response = client.get('/', headers={'CF-Connecting-IP': '203.0.113.1'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == '203.0.113.1'

def test_get_ip_x_forwarded_for(client):
    response = client.get('/', headers={'X-Forwarded-For': '203.0.113.1, 198.51.100.2'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == '203.0.113.1'

def test_get_ip_invalid_cf_connecting_ip(client):
    response = client.get('/', headers={'CF-Connecting-IP': 'invalid-ip'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == '127.0.0.1'

def test_get_ip_invalid_x_forwarded_for(client):
    response = client.get('/', headers={'X-Forwarded-For': 'invalid-ip, 198.51.100.2'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == '198.51.100.2'
