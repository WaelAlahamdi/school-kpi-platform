def test_home():
    from kpi_app import app
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"School KPI" in response.data

def test_indicators():
    from kpi_app import app
    client = app.test_client()
    response = client.get('/indicators')
    assert response.status_code == 200
    data = response.get_json()
    assert "schools" in data
    assert isinstance(data["schools"], list)
