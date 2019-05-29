FROM python:3.7.2-alpine

RUN apk add --update --no-cache g++ gcc libxslt-dev libxml2-dev libxslt-dev python-dev


ENV LIBRARY_PATH=/lib:/usr/lib
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

ADD . /code/

EXPOSE 8001

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]