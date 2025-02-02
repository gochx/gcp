import joblib
import json
import numpy as np

# Modell laden
model_filename = "model.joblib"
model = joblib.load(model_filename)

# JSON-Datei laden
test_file = "test_instances.jsonl"
instances = []

# JSON-Datei Zeile für Zeile einlesen
with open(test_file, "r") as f:
    for line in f:
        data = json.loads(line)  # Jede Zeile als JSON laden
        instances.append(data["instances"][0])  # Werte extrahieren

# In ein NumPy-Array umwandeln (Vertex AI erwartet 2D-Array)
instances = np.array(instances)

# Vorhersagen treffen
predictions = model.predict(instances)

print("Vorhersagen:", predictions)
