# main.py
from fastapi import FastAPI, HTTPException, UploadFile
import os
import pyclamd

app = FastAPI()

# Get ClamAV connection details from environment variables
CLAMAV_HOST = os.getenv("CLAMAV_HOST", "127.0.0.1")
CLAMAV_PORT = int(os.getenv("CLAMAV_PORT", 3310))

# Initialize ClamAV
cd = pyclamd.ClamdNetworkSocket(host=CLAMAV_HOST, port=CLAMAV_PORT)

@app.on_event("startup")
def verify_clamav_connection():
    if not cd.ping():
        raise RuntimeError(f"Unable to connect to ClamAV at {CLAMAV_HOST}:{CLAMAV_PORT}")

@app.post("/scan/file")
async def scan_file(file: UploadFile):
    content = await file.read()
    result = cd.scan_stream(content)
    if not result:
        return {"status": "clean"}
    return {"status": "infected", "details": result}

@app.post("/scan/path")
async def scan_file_path(path: str):
    if not os.path.exists(path):
        raise HTTPException(status_code=400, detail="File path does not exist")
    result = cd.scan_file(path)
    if not result:
        return {"status": "clean"}
    return {"status": "infected", "details": result}
