FROM python:3.8-alpine
WORKDIR /app
COPY requirements.txt . 
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["/usr/local/bin/python", "app.py"]

