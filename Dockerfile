FROM python:3.10.4

RUN mkdir app

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "main:app", "--bind=0.0.0.0:8000"]
