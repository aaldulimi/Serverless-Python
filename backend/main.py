# ignore authentication for now, any request will be accepted
from fastapi import FastAPI, UploadFile
import shutil, gzip

app = FastAPI()

# gets the python file to containerize
@app.post("/push/")
def push(file: UploadFile):
    try:
        with gzip.open(file.file, 'rb') as f_in:
            with open('test_uncompressed.py', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        return {"status": "success"}

    except Exception as e:
        return {"message": f"Error reading file. Error: {e}"}
    
    finally:
        file.file.close()
        
