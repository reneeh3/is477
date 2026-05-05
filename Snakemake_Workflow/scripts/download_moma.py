import requests
import hashlib
import os

ARTISTS_URL = "https://media.githubusercontent.com/media/MuseumofModernArt/collection/main/Artists.csv"
ARTWORKS_URL = "https://media.githubusercontent.com/media/MuseumofModernArt/collection/main/Artworks.csv"

def download(url, path):
    r = requests.get(url)
    r.raise_for_status()
    with open(path, "wb") as f:
        f.write(r.content)

def sha256(file_path):
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

os.makedirs("data", exist_ok=True)

download(ARTISTS_URL, "data/moma_artists.csv")
download(ARTWORKS_URL, "data/moma_artworks.csv")

print("MoMA datasets downloaded")
