FROM python:3.8-alpine as base

### First stage
FROM base as builder

# Envs
ENV PYTHONPATH /app/src/
ENV PATH /app/src/:$PATH
ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.0.10

# change workdir
WORKDIR /app

# install system dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev make postgresql-dev

# install poetry
RUN pip install --no-cache-dir poetry

# install packages
COPY ./poetry.lock /app/poetry.lock
COPY ./pyproject.toml /app/pyproject.toml
RUN python -m venv /env && . /env/bin/activate && poetry install

### Second stage
FROM base

# Envs
# ENV PYTHONPATH /app/src/
# ENV PATH /app/src/:$PATH

# change workdir
WORKDIR /app

# install system dependencies
RUN apk add --no-cache postgresql-libs

# copy build
COPY --from=builder /env /env
COPY . /app

EXPOSE 9000
ENTRYPOINT []
CMD ["/env/bin/uvicorn", "src.asgi:app", "--host", "0.0.0.0", "--port", "9000", "--workers", "4"]
