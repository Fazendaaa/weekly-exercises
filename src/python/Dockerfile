FROM python:3.13.0-alpine3.20
LABEL author="fazenda"
LABEL project="weekly-exercises-py"

# https://stackoverflow.com/a/49955098/7092954
RUN [ "addgroup", "-S", "appgroup" ]
RUN [ "adduser", "-S", "appuser", "-G", "appgroup" ]

USER root

RUN [ "apk", "add", "--no-cache", \
  "gcc", \
  "linux-headers", \
  "mariadb-connector-c-dev", \
  "musl-dev", \
  "mysql-client", \
  "pkgconf", \
  "python3-dev", \
  "rust" \
  ]

RUN [ "pip3", "install", "poetry" ]

WORKDIR /usr/src/

#USER appuser

COPY poetry.lock .
COPY pyproject.toml .

RUN [ "poetry", "install", "--no-root", "--no-interaction", "--no-ansi" ]

COPY tests/ tests/
COPY src/ src/
