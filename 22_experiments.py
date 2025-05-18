from google.cloud import aiplatform
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from google.cloud import bigquery
import pandas as pd
import joblib


# Init
aiplatform.init(experiment="rf-experiment-04", project="vertex2025", location="us-central1")
aiplatform.start_run(run="run1")

# Daten aus BigQuery
client = bigquery.Client(project="vertex2025")
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

aiplatform.end_run()
