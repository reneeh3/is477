import requests
import os
import hashlib

MET_URL = "https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv"

DATA_PATH = "data/met_objects.csv"
HASH_PATH = "data/met_objects.sha256"

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
os.makedirs("checksums", exist_ok=True)

download(MET_URL, DATA_PATH)
actual_hash = sha256(DATA_PATH)

if not os.path.exists(HASH_PATH):
    with open(HASH_PATH, "w") as f:
        f.write(actual_hash)
    print("MET dataset downloaded")
    print("SHA256:", actual_hash)
    print("Checksum file created")
else:
    with open(HASH_PATH) as f:
        expected_hash = f.read().strip()
    print("MET dataset downloaded")
    print("Expected SHA256:", expected_hash)
    print("Actual SHA256:  ", actual_hash)
    if actual_hash == expected_hash:
        print("Integrity check passed")
    else:
        raise ValueError("Integrity check FAILED: dataset may have changed")
