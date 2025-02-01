from google.cloud import aiplatform
from google.cloud import storage
import os

# GCP-Setup
PROJECT_ID = "vertex2025"
BUCKET_NAME = "gochx_bucket"
GCS_MODEL_FOLDER = "models/my_model"
MODEL_FILE_NAME = "model.joblib"
GCS_MODEL_PATH = f"gs://{BUCKET_NAME}/{MODEL_FILE_NAME}"

# Modell lokal speichern
#model_path = "model.pkl"
#joblib.dump(model, model_path)
#print(f"Modell lokal gespeichert als {model_path}")

# Cloud Storage Client initialisieren
storage_client = storage.Client(project=PROJECT_ID)

# Datei in den Bucket hochladen
bucket = storage_client.bucket(BUCKET_NAME)
blob = bucket.blob(f"{GCS_MODEL_FOLDER}/model.joblib")
blob.upload_from_filename("model.joblib")

print(f"Modell erfolgreich nach Cloud Storage hochgeladen: {GCS_MODEL_PATH}")



