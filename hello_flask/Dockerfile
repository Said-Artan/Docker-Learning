
# Stage 1: Build Stage
FROM python:3.8-slim AS build
WORKDIR /app
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config

COPY . .

RUN pip3 install flask mysqlclient

# Stage 2: Production Stage 
FROM python:3.8-slim
WORKDIR /app
COPY --from=build /app /app
EXPOSE 5002
CMD ["python", "app.py"]


