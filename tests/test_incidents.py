import requests

BASE_URL = "http://127.0.0.1:8000"


def test_create_incident():
    payload = {
        "site": "Port Hedland",
        "incident_type": "vehicle",
        "severity": "medium",
        "description": "Near-miss between haul truck and light vehicle",
        "date_reported": "2026-08-30",
    }
    response = requests.post(f"{BASE_URL}/incidents", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert body["site"] == "Port Hedland"
    assert body["status"] == "open"
    assert "id" in body


def test_get_all_incidents():
    response = requests.get(f"{BASE_URL}/incidents")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_nonexistent_incident_returns_404():
    response = requests.get(f"{BASE_URL}/incidents/999999")
    assert response.status_code == 404


def test_update_incident_status():
    create_response = requests.post(f"{BASE_URL}/incidents", json={
        "site": "Newman",
        "incident_type": "equipment",
        "severity": "low",
        "date_reported": "2026-08-29",
    })
    incident_id = create_response.json()["id"]

    update_response = requests.put(f"{BASE_URL}/incidents/{incident_id}", json={"status": "resolved"})
    assert update_response.status_code == 200
    assert update_response.json()["status"] == "resolved"


def test_delete_incident():
    create_response = requests.post(f"{BASE_URL}/incidents", json={
        "site": "Kalgoorlie",
        "incident_type": "environmental",
        "severity": "low",
        "date_reported": "2026-08-28",
    })
    incident_id = create_response.json()["id"]

    delete_response = requests.delete(f"{BASE_URL}/incidents/{incident_id}")
    assert delete_response.status_code == 200

    get_response = requests.get(f"{BASE_URL}/incidents/{incident_id}")
    assert get_response.status_code == 404