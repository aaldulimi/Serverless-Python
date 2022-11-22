# ignore authentication for now, any request will be accepted
from fastapi import FastAPI, UploadFile
import shutil
import gzip
import string
import random
import helper as helper
from pydantic import BaseModel
from container import Container

app = FastAPI()

class ContainerCreation(BaseModel):
    id: str
    filename: str
    name: str
    cpu: int
    ram: int
    image: str
    pip: list

class ImageBuild(BaseModel):
    id: str
    name: str


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
def create_container(container_data: ContainerCreation):
    container_data = container_data.dict()
    container = Container(**container_data)
    container.create_dockerfile()

    return {"success": True}

    # send container details to server

@app.post('/image/')
def build_container(image: ImageBuild):
    helper.build_image(image.id, image.name)
    # helper.compress_image(image.id, image.name)
    return {"success": True}

    # compress and save somewhere to send to deploy machine?
    # the deploy machine is different than the one running this microservice 
    