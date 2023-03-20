FROM python:3.8-slim-buster

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -yq espeak ffmpeg libespeak1

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "main.py" ]
