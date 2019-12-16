FROM alpine:3.7

COPY app /root/app
WORKDIR /root/app

RUN apk add --update python3 && \
	apk add --update py-pip && \
	apk add --update py3-setuptools

RUN pip3 install -r /root/app/requirements.txt

EXPOSE 5000 5050
ENV FLASK_APP=main.py
CMD python3 -m flask run --host=127.0.0.1