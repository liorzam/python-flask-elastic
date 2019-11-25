FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev python3

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENV FLASK_APP=run.py
ENV FLASK_DEBUG=True
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

#ENTRYPOINT "/usr/bin/python3"

CMD [ "flask", "run", "--host=0.0.0.0" ]