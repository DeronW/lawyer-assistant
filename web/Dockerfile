FROM python:3.11-alpine3.16

COPY . /srv

WORKDIR /srv

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]