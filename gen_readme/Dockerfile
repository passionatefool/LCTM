FROM python:alpine3.13
RUN apk add --no-cache make
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENTRYPOINT ["make"]
