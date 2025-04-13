FROM python:3.11-slim

WORKDIR /app

COPY web /app/web
COPY password_generator.py /app/
COPY requirements.txt /app/

ENV PYTHONPATH=/app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "web/app.py"]

