from pydantic import BaseModel

class DockerData(BaseModel):
    id: str
    name: str
    filename: str
    image: str
    pip: list

class ImageBuild(BaseModel):
    id: str
    name: str