FROM python:3.11-slim
WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN mkdir -p /app/databases


EXPOSE 8001
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]


# User Service: EXPOSE 8004, CMD ["python", "manage.py", "runserver", "0.0.0.0:8004"]