# Use an official Python runtime as a parent image
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"
WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-dev

COPY . .
EXPOSE 8000

CMD ["poetry", "run", "python", "main.py"]

