FROM python:3.11-alpine
LABEL authors="TravisW"

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -Ur requirements.txt

COPY app.py /app/app.py

ENTRYPOINT ["python", "/app/app.py"]