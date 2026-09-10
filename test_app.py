from app import app

def test_accueil():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "Bonjour" in response.get_data(as_text=True)
