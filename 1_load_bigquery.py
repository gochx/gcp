from google.cloud import bigquery
import pandas as pd

# GCP-Projekt & BigQuery Dataset
PROJECT_ID = "vertex2025"
DATASET_ID = "gochx_data"
TABLE_ID = "gochx_table"

# Erstelle einen BigQuery-Client
client = bigquery.Client(project=PROJECT_ID)


## Dataset erstellen

# Dataset-Referenz
dataset_ref = client.dataset(DATASET_ID)

# Prüfen, ob Dataset existiert, sonst erstellen
try:
    client.get_dataset(dataset_ref)
    print(f"Dataset {DATASET_ID} existiert bereits.")
except:
    dataset = bigquery.Dataset(dataset_ref)
    dataset.location = "US"
    dataset = client.create_dataset(dataset)
    print(f"Dataset {DATASET_ID} wurde erstellt.")

## Tabelle erstellen
# Tabelle definieren
schema = [
    bigquery.SchemaField("feature1", "FLOAT"),
    bigquery.SchemaField("feature2", "FLOAT"),
    bigquery.SchemaField("label", "INTEGER"),
]

table_ref = client.dataset(DATASET_ID).table(TABLE_ID)

# Prüfen, ob Tabelle existiert, sonst erstellen
try:
    client.get_table(table_ref)
    print(f"Tabelle {TABLE_ID} existiert bereits.")
except:
    table = bigquery.Table(table_ref, schema=schema)
    table = client.create_table(table)
    print(f"Tabelle {TABLE_ID} wurde erstellt.")


# Dummy-Daten als Pandas DataFrame
data = pd.DataFrame({
    "feature1": [1.2, 2.4, 3.1, 4.8, 5.0],
    "feature2": [3.5, 1.2, 7.8, 3.2, 5.5],
    "label": [0, 1, 1, 0, 1]
})

# Lade Daten nach BigQuery hoch
table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
job = client.load_table_from_dataframe(data, table_ref)
job.result()  # Warte auf Abschluss

print(f"Daten in BigQuery hochgeladen: {table_ref}")
