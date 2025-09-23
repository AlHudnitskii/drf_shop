FROM python:3.11-slim
WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN mkdir -p /app/databases

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Для каждого сервиса измените:
# API Gateway: EXPOSE 8000, CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Product Service: EXPOSE 8001, CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]  
# Cart Service: EXPOSE 8002, CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]
# Order Service: EXPOSE 8003, CMD ["python", "manage.py", "runserver", "0.0.0.0:8003"]
# User Service: EXPOSE 8004, CMD ["python", "manage.py", "runserver", "0.0.0.0:8004"]