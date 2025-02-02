# Wichtig: Man brauch Version 1.5: pip install -U scikit-learn==1.5.2

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from google.cloud import bigquery
import pandas as pd

# GCP-Projekt & BigQuery Dataset
PROJECT_ID = "vertex2025"
DATASET_ID = "gochx_data"
TABLE_ID = "gochx_table"

# Erstelle einen BigQuery-Client
client = bigquery.Client(project=PROJECT_ID)

def load_data_from_bigquery():
    query = f"SELECT * FROM `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}`"
    df = client.query(query).to_dataframe()
    return df

df = load_data_from_bigquery()
print("Daten geladen:", df.head())



# Daten vorbereiten
X = df.drop(columns=["label"]).values
y = df["label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modell trainieren
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Modell speichern (richtiges Format für Vertex AI)
model_filename = "model.joblib"
joblib.dump(model, model_filename)
print("Modell gespeichert als model.joblib")