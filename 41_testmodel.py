# Optional: Auszuführen nach 4_model2vertex.py, um das Modell als Batch Prediction zu testen.
#
# Vorher ausführen um die JSON Datei in den Bucket zu laden:
# gsutil cp test_instances.jsonl gs://gochx_bucket/test_instances.jsonl


from google.cloud import aiplatform

# GCP-Setup
PROJECT_ID = "vertex2025"
LOCATION = "us-central1"
MODEL_ID = "5844419972582866944"  # Deine Modell-ID aus 4 model2vetex.py
GCS_INPUT_URI = "gs://gochx_bucket/test_instances.jsonl"
GCS_OUTPUT_URI = "gs://gochx_bucket/batch_predictions/"

# Vertex AI initialisieren
aiplatform.init(project=PROJECT_ID, location=LOCATION)

# Modell laden
model = aiplatform.Model(model_name=f"projects/{PROJECT_ID}/locations/{LOCATION}/models/{MODEL_ID}")

# Batch Prediction ausführen
batch_prediction_job = model.batch_predict(
    job_display_name="random_forest_batch_prediction",
    gcs_source=GCS_INPUT_URI,
    gcs_destination_prefix=GCS_OUTPUT_URI,
    machine_type="n1-standard-4",
)

batch_prediction_job.wait()  # Warten, bis das Batch-Job abgeschlossen ist

print(f"Batch Prediction abgeschlossen! Ergebnisse unter: {GCS_OUTPUT_URI}")
