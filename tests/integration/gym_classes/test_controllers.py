from bson.objectid import ObjectId
from fastapi import status
from fastapi.testclient import TestClient


def test_can_create_gym_class(test_client: TestClient) -> None:
    # given
    payload = {
        "name": "Pilates",
        "day": "Monday",
        "time": "10:30-11:30",
        "coach": "Simon W.",
        "description": "Try pilates in our gym",
    }

    # when
    response = test_client.post("/classes", json=payload)

    # then
    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.json()


def test_can_get_gym_class(test_client: TestClient, seed_db: list[dict[str, str]]) -> None:
    # when
    gym_class_id = seed_db[0]["id"]
    response = test_client.get(f"/classes/{gym_class_id}")

    # then
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == seed_db[0]
