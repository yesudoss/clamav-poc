py -m venv env

env\scripts\activate.bat

pip install fastapi uvicorn python-multipart

pip install pyclamd

uvicorn fastapi_clamav:app --reload

create clamd.conf file and paste it in C:\Program Files\ClamAV

<!-- ------------ -->
Pull the official or community ClamAV Docker image:
docker pull clamav/clamav

Start a ClamAV container with network mode and port mapping:
docker run -d --name clamav -p 3310:3310 clamav/clamav

Confirm the container is running:
docker ps
