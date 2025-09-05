FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --na-cache-der -r requirements.txt

COPY app/ ./app

EXPOSE 8080

CMD ["python", "-m", "app.main"]
