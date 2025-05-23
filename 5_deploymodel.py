from google.cloud import aiplatform

'''
Creating Model
Create Model backing LRO: projects/1024410131179/locations/us-central1/models/7522010833778376704/operations/7785503194737541120
Model created. Resource name: projects/1024410131179/locations/us-central1/models/7522010833778376704@1
To use this Model in another session:
model = aiplatform.Model('projects/1024410131179/locations/us-central1/models/7522010833778376704@1')
Modell erfolgreich hochgeladen: projects/1024410131179/locations/us-central1/models/7522010833778376704
'''

# GCP-Setup
PROJECT_ID = "vertex2025"
LOCATION = "us-central1"
MODEL_ID = "5844419972582866944"  # Deine Modell-ID
ENDPOINT_NAME = "random_forest_endpoint"

# Vertex AI initialisieren
aiplatform.init(project=PROJECT_ID, location=LOCATION)

# Modell aus der Vertex AI Model Registry abrufen 
model = aiplatform.Model(f"projects/{PROJECT_ID}/locations/{LOCATION}/models/{MODEL_ID}")

# Endpunkt erstellen
endpoint = aiplatform.Endpoint.create(display_name=ENDPOINT_NAME)
print(f"Endpunkt erstellt: {endpoint.resource_name}")

# Modell zum Endpunkt deployen (also mit dem Endpunkt verbinden)
deployed_model = endpoint.deploy(
    model=model,  
    machine_type="n1-standard-4",
    traffic_split={"0": 100}  # Alle Anfragen an dieses Modell leiten
)

print(f"Modell erfolgreich als API bereitgestellt: {endpoint.resource_name}")
print(f"Dein REST API Endpoint ist: {endpoint.predict}")