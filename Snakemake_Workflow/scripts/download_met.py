import requests
import os
import hashlib

MET_URL = "https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv"

def download(url, path):
    r = requests.get(url, stream=True)
    r.raise_for_status()
    with open(path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

def sha256(file_path):
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

os.makedirs("data", exist_ok=True)

download(MET_URL, "data/met_objects.csv")

print("MET dataset downloaded")
print("SHA256:", sha256("data/met_objects.csv"))
