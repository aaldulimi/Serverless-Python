# ignore authentication for now, any request will be accepted
from fastapi import FastAPI, UploadFile
import shutil
import gzip
import string
import random
import backend.helper as helper

app = FastAPI()


# gets the python file to containerize
@app.post("/push/")
def push(file: UploadFile):
    request_id = "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(8)
    )
    helper.create_dir(request_id)

    is_successful = True
    try:
        with gzip.open(file.file, "rb") as f_in:
            with open(f"{request_id}/{file.filename[:-3]}.py", "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)

    except Exception:
        is_successful = False
        helper.delete_dir(request_id)

    finally:
        file.file.close()

    return {
        "success": is_successful,
        "request_id": request_id,
    }

