from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import pyclamd
import os

app = FastAPI()

# Initialize ClamAV
try:
    cd = pyclamd.ClamdUnixSocket()
    cd.ping()
except pyclamd.ConnectionError:
    cd = pyclamd.ClamdNetworkSocket()
    if not cd.ping():
        raise RuntimeError("Unable to connect to ClamAV")

# Define a model for local file path input
class FilePath(BaseModel):
    path: str

@app.post("/scan/file")
async def scan_uploaded_file(file: UploadFile = File(...)):
    print("1111111111111")
    
    """
    Endpoint to scan an uploaded file.
    """
    try:
        print("222222222222", file)
        contents = await file.read()
        result = cd.instream(contents)
        if result:
            return {"status": "infected", "details": result}
        return {"status": "clean"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error scanning file: {str(e)}")

@app.post("/scan/path")
async def scan_file_path(file_path: FilePath):
    """
    Endpoint to scan a file by local path.
    """
    if not os.path.isfile(file_path.path):
        raise HTTPException(status_code=400, detail="File does not exist")
    
    try:
        print("11111111111111111111")
        result = cd.scan_file(file_path.path)
        print("22222222222222222222222")
        if result:
            print("3333333333333333")
            return {"status": "infected", "details": result}
        return {"status": "clean"}
    except Exception as e:
        print("****************")
        raise HTTPException(status_code=500, detail=f"Error scanning file: {str(e)}")

@app.get("/")
async def root():
    return {"message": "ClamAV File Scanner is running!"}
@app.get("/test")
async def root():
    return {"message": "ClamAV File Scanner is running!"}
