from app.routes.task_1 import router as r_1
from fastapi import status
from fastapi.testclient import TestClient

# from fastapi import FastAPI


# app = FastAPI()
client = TestClient(r_1)


def test_calculate_sum():
    response = client.post(
        "/find_in_different_registers",
        json={["Мама", "МАМА", "Мама", "папа", "ПАПА", "Мама", "ДЯдя", "брАт", "Дядя", "Дядя", "Дядя"]},
    )
    assert response.status_code == 200
    assert response.json() == {[
        "брат",
        "папа"
    ]}
