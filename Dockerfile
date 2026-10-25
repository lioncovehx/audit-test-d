FROM python:latest
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app ./app
ENV API_SIGNING_SECRET=9f8e7d6c5b4a39281706f5e4d3c2b1a0
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
