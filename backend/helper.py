from pathlib import Path
import shutil
import os

def create_dir(dir_path):
    db_path = Path(dir_path)
    db_path.mkdir(parents=True, exist_ok=True)


def delete_dir(dir_path):
    path = Path(dir_path)
    shutil.rmtree(path, ignore_errors=True)

def build_image(id, name):
    os.system(f"docker build -t {id}_{name} {id}/")

def compress_image(id, name):
    os.system(f"docker save {id}_{name}:latest | gzip > {id}/{name}_compressed.tar.gz")
    