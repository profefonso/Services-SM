FROM python:3.7.2-alpine

ENV LIBRARY_PATH=/lib:/usr/lib
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/

EXPOSE 8002

CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]