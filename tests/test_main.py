import time
from fastapi.testclient import TestClient
from src.main import app
import unittest

client = TestClient(app)

class TestFastAPIApp(unittest.TestCase):

    def test_read_root(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("current_time", response.json())

    def test_query_performance(self):
        start_time = time.time()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)

        elapsed_time = time.time() - start_time
        self.assertTrue(elapsed_time < 0.200)

    def test_creating_jwt_token() -> None:
        token = create_jwt_token(
        jwt_content={"content": "payload"},
        secret_key="secret",
        expires_delta=timedelta(minutes=1),
    )
    parsed_payload = jwt.decode(token, "secret", algorithms=[ALGORITHM])

    assert parsed_payload["content"] == "payload"