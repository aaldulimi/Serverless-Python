from client.container import Container
import client.image as Image 


Container(
    name="web_scraper",
    cpu=1,
    ram=2,
    image=Image.PYTHON_3_8_SLIM,
    pip=["requests"],
)


