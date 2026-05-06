import requests
import hashlib
import os

ARTISTS_URL = "https://media.githubusercontent.com/media/MuseumofModernArt/collection/main/Artists.csv"
ARTWORKS_URL = "https://media.githubusercontent.com/media/MuseumofModernArt/collection/main/Artworks.csv"

ARTISTS_PATH = "data/moma_artists.csv"
ARTWORKS_PATH = "data/moma_artworks.csv"

ARTISTS_HASH_PATH = "data/moma_artists.sha256"
ARTWORKS_HASH_PATH = "data/moma_artworks.sha256"

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
os.makedirs("checksums", exist_ok=True)

download(ARTISTS_URL, ARTISTS_PATH)
download(ARTWORKS_URL, ARTWORKS_PATH)

artists_hash = sha256(ARTISTS_PATH)
artworks_hash = sha256(ARTWORKS_PATH)

# Artists checksum
if not os.path.exists(ARTISTS_HASH_PATH):
    with open(ARTISTS_HASH_PATH, "w") as f:
        f.write(artists_hash)
    print("Artists checksum file created")
else:
    with open(ARTISTS_HASH_PATH) as f:
        expected_hash = f.read().strip()
    if artists_hash == expected_hash:
        print("Artists integrity check passed")
    else:
        raise ValueError("Artists integrity check FAILED: dataset may have changed")

# Artworks checksum
if not os.path.exists(ARTWORKS_HASH_PATH):
    with open(ARTWORKS_HASH_PATH, "w") as f:
        f.write(artworks_hash)
    print("Artworks checksum file created")
else:
    with open(ARTWORKS_HASH_PATH) as f:
        expected_hash = f.read().strip()
    if artworks_hash == expected_hash:
        print("Artworks integrity check passed")
    else:
        raise ValueError("Artworks integrity check FAILED: dataset may have changed")

print("MoMA datasets downloaded")
print("Artists SHA256:", artists_hash)
print("Artworks SHA256:", artworks_hash)
