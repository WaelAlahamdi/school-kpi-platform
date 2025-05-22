def test_home():
    from kpi_app import app
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
