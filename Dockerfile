FROM python:3.6

COPY . /usr/src/app/
WORKDIR /usr/src/app/

RUN pip install -e .