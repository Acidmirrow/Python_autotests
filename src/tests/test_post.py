

def test_get_all_posts(client):
    """Проверяем, что GET /posts возвращает список из 100 объектов."""
    resp = client.get("/posts")
    assert resp.status_code == 200
    data = resp.json()
    print(data)
    assert isinstance(data, list)
    assert len(data) == 100
