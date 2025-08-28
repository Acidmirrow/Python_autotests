import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com"  # пример API

def test_get_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    data = response.json()
    print(json.dumps(data, indent=4, ensure_ascii=False))
    assert data["id"] == 1
    assert "title" in data
    