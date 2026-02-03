import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture
def client(base_url):
    """Простой HTTP‑клиент, который автоматически добавляет базовый URL."""

    class APIClient:
        def __init__(self, base):
            self.base = base

        def get(self, path, **kwargs):
            url = f"{self.base}{path}"
            return requests.get(url, **kwargs)

        # можно добавить post/put/delete при необходимости

    return APIClient(base_url)