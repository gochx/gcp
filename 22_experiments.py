from google.cloud import aiplatform
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from google.cloud import bigquery
import pandas as pd
import joblib
import os
import tempfile


PROJECT_ID = "vertex2025"
REGION = "us-central1"
EXPERIMENT_NAME = "rf-experiment-05"
RUN_NAME = "run1"

# Init
aiplatform.init(experiment=EXPERIMENT_NAME, project=PROJECT_ID, location=REGION)
aiplatform.start_run(run=RUN_NAME)

# Daten aus BigQuery
client = bigquery.Client(project=PROJECT_ID)
df = client.query("SELECT * FROM `vertex2025.gochx_data.gochx_table`").to_dataframe()

X = df.drop(columns=["label"]).values
y = df["label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelltraining
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Logs
aiplatform.log_params({"n_estimators": 100, "random_state": 42})
aiplatform.log_metrics({"accuracy": accuracy})

''' MUSS NOCH AKTUALISIERT WERDEN
Siehe: https://cloud.google.com/vertex-ai/docs/experiments/track-executions-artifacts?hl=de
# Save and log the model as artifact
with tempfile.TemporaryDirectory() as tmpdir:
    model_path = os.path.join(tmpdir, "model.joblib")
    joblib.dump(model, model_path)
    aiplatform.log_artifact(model_path, artifact_id="rf_model")

# log output predictions
results_df = pd.DataFrame({
    "y_true": y_test,
    "y_pred": y_pred
})
with tempfile.TemporaryDirectory() as tmpdir:
    results_path = os.path.join(tmpdir, "predictions.csv")
    results_df.to_csv(results_path, index=False)
    aiplatform.log_artifact(results_path, artifact_id="predictions")
'''

aiplatform.end_run()
