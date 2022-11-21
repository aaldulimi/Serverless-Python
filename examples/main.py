import requests
# from client.container import Container
# import client.image as Image 


# # Container(
# #     name="web_scraper",
# #     cpu=1, 
# #     ram=2,
# #     image=Image.PYTHON_3_8_SLIM,
# #     pip=["requests"],
# # )



url = 'http://127.0.0.1:8000/push/'
file = {'file': open('examples/test.gz', 'rb')}
response = requests.post(url=url, files=file) 
data = response.json()

print(data)