FROM python:3.8-alpine as base

### First stage
FROM base as builder

# change workdir
WORKDIR /src

# install system dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev make postgresql-dev

# install poetry
RUN pip install --no-cache-dir poetry==1.0.9

# install packages
COPY ./poetry.lock /src/poetry.lock
COPY ./pyproject.toml /src/pyproject.toml
RUN python -m venv /env && . /env/bin/activate && poetry install

# copy application code
RUN rm /src/poetry.lock 
RUN rm /src/pyproject.toml

### Second stage
FROM base

# change workdir
WORKDIR /src

# install system dependencies
RUN apk add --no-cache postgresql-libs

# copy build
COPY --from=builder /env /env
COPY /src /src

EXPOSE 9000
ENTRYPOINT []
CMD ["/env/bin/uvicorn", "asgi:app", "--host", "0.0.0.0", "--port", "9000", "--workers", "4"]
