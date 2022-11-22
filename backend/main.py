# ignore authentication for now, any request will be accepted
from fastapi import FastAPI, UploadFile
import shutil
import gzip
import string
import random
import helper as helper
from docker import Dockerfile, Image
from data import DockerData, ImageBuild


app = FastAPI()


# gets the python file to containerize
@app.post("/push/")
def push(file: UploadFile):
    request_id = "".join(
        random.choice(string.ascii_lowercase + string.digits) for _ in range(8)
    )
    helper.create_dir(request_id)

    is_successful = True
    py_file = f'{file.filename[:-3]}.py'
    try:

        with gzip.open(file.file, "rb") as f_in:
            with open(f"{request_id}/{py_file}", "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)

    except Exception:
        is_successful = False
        helper.delete_dir(request_id)

    finally:
        file.file.close()

    return {
        "success": is_successful,
        "request_id": request_id,
        "filename": py_file,
    }


@app.post('/container/')
def create_container(docker_data: DockerData):
    docker_data = docker_data.dict()
    dockerfile = Dockerfile(**docker_data)
    dockerfile.create()

    return {"success": True, "name": dockerfile.name}

@app.post('/image/')
def build_container(image_data: ImageBuild):
    image = Image(image_data.id, image_data.name)
    image.build()
    compressed_name = image.compress()
  
    return {"success": True, "name": compressed_name}

    # find which machine to deploy to 
    # send compressed image to deploy machine 
    # send containr name to deploy machine

