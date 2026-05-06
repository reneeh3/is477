import os
import hashlib
import requests


# Official MoMA dataset URLs
MOMA_ARTISTS_URL = "https://media.githubusercontent.com/media/MuseumofModernArt/collection/43399bad2fad626a0750ab6801ced6f1e83b0a41/Artists.csv"
MOMA_ARTWORKS_URL = "https://media.githubusercontent.com/media/MuseumofModernArt/collection/a46be68e826552737fce8152b002dcd603c0a300/Artworks.csv"

# Output paths used by Snakefile
ARTISTS_PATH = "data/moma_artists.csv"
ARTWORKS_PATH = "data/moma_artworks.csv"

# Saved SHA-256 checksums from verified download
EXPECTED_ARTISTS_HASH = "4e916f29676fc1ba11a1db86544f171566ffe2240976a52140e319f5ad127889"
EXPECTED_ARTWORKS_HASH = "6f009c14d75c0acdda5ff709bc6b05642a2a878c0b9bc44de7c7314bdea39e00"


def download_file(url, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(output_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)


def compute_sha256(file_path):
    """Compute the SHA-256 hash of a local file."""
    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            sha256_hash.update(chunk)

    return sha256_hash.hexdigest()


def verify_checksum(file_path, expected_hash):
    """Compare actual SHA-256 hash with expected SHA-256 hash."""
    actual_hash = compute_sha256(file_path)

    if actual_hash != expected_hash:
        raise ValueError(
            f"Checksum mismatch for {file_path}\n"
            f"Expected: {expected_hash}\n"
            f"Actual:   {actual_hash}"
        )

    print(f"Checksum verified for {file_path}")


def main():
    download_file(MOMA_ARTISTS_URL, ARTISTS_PATH)
    download_file(MOMA_ARTWORKS_URL, ARTWORKS_PATH)

    verify_checksum(ARTISTS_PATH, EXPECTED_ARTISTS_HASH)
    verify_checksum(ARTWORKS_PATH, EXPECTED_ARTWORKS_HASH)

    print("MoMA data acquisition complete.")


if __name__ == "__main__":
    main()
