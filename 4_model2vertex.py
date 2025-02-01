from google.cloud import aiplatform

# GCP-Setup
PROJECT_ID = "vertex2025"
BUCKET_NAME = "gochx_bucket"
GCS_MODEL_FOLDER = "models/my_model"

# Vertex AI-Setup
aiplatform.init(project=PROJECT_ID, location="us-central1")

# Modell hochladen
model = aiplatform.Model.upload(
    display_name="random_forest_model",
    artifact_uri=f"gs://{BUCKET_NAME}/{GCS_MODEL_FOLDER}/",
    serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-0:latest"
)

print("Modell erfolgreich hochgeladen:", model.resource_name)