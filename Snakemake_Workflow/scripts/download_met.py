import os
import hashlib
import requests


# Official MET Open Access dataset URL
MET_URL = "https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv"

# Output path used by Snakefile
MET_PATH = "data/met_objects.csv"

# Verified SHA-256 checksum
EXPECTED_MET_HASH = "de617b9c947458e426111207f81a65bd1379a151c0077d3ce29cfc22fc0b9183"


def download_file(url, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(output_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)


def compute_sha256(file_path):
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
    download_file(MET_URL, MET_PATH)

    verify_checksum(MET_PATH, EXPECTED_MET_HASH)

    print("MET data acquisition complete.")


if __name__ == "__main__":
    main()
