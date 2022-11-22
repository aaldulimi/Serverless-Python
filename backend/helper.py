from pathlib import Path
import shutil

def create_dir(dir_path):
    db_path = Path(dir_path)
    db_path.mkdir(parents=True, exist_ok=True)


def delete_dir(dir_path):
    path = Path(dir_path)
    shutil.rmtree(path, ignore_errors=True)
   