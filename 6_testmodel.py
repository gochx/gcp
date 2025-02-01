import requests
import json
from google.oauth2 import service_account
from google.auth.transport.requests import Request

# Das hier vorher in der Google Cloud Shell ausführen
# gcloud auth application-default login

# 🔹 GCP-Projekt & Endpoint-ID (ohne Komma!)
PROJECT_ID = "1024410131179"
ENDPOINT_ID = "7557384321867186176"

# 🔹 Endpunkt-URL
ENDPOINT_URL = f"https://us-central1-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/us-central1/endpoints/{ENDPOINT_ID}:predict"

# 🔹 Testdaten (müssen die gleichen Features wie das Modell haben!)
test_instance = {
    "instances": [
        {"feature1": 2.5, "feature2": 3.1}
    ]
}

# 🔹 OAuth 2.0 Token explizit generieren
from google.auth import default
credentials, _ = default()
credentials.refresh(Request())  # Aktualisiere das Token

# 🔹 Header mit gültigem Access Token
headers = {
    "Authorization": f"Bearer {credentials.token}",
    "Content-Type": "application/json"
}

# 🔹 API-Request senden
response = requests.post(ENDPOINT_URL, headers=headers, json=test_instance)
print("API Antwort:", response.json())
