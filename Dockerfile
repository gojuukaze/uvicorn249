FROM python:3.7

COPY ./requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

ADD . /app/uvicorn249

WORKDIR /app/uvicorn249

CMD uvicorn uvicorn249.asgi:application --host 0.0.0.0 --port 8000 --ws wsproto --debug