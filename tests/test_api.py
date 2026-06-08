from fastapi.testclient import TestClient
import main 

client = TestClient(main.app)

def test_health():
  response = client.get("/health")
  
  assert response.status_code == 200
  
def test_stats_endpoint():
  response = client.get("/data/stats")
  assert response.status_code == 200
  
def test_ai_endpoint_without_dataset():
  response = client.post("/ai/ask", json={"question": "test"})
  assert response.status_code == 200