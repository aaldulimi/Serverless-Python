from pathlib import Path
import shutil
import os

def create_dir(dir_path):
    db_path = Path(dir_path)
    db_path.mkdir(parents=True, exist_ok=True)


def delete_dir(dir_path):
    path = Path(dir_path)
    shutil.rmtree(path, ignore_errors=True)

def build_image(id, image_name):
    os.system(f"docker build -t {image_name} {id}/")

def compress_image(id, image_name):
    compressed_name = f"{id}/{image_name}_compressed.tar.gz"
    os.system(f"docker save {image_name}:latest | gzip > {compressed_name}")

    return compressed_name