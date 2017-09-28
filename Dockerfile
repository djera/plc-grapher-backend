FROM python:2.7
ENV PYTHONBUFFERED 0

RUN mkdir /code
ADD requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
ADD . /code
RUN python manage.py collectstatic --noinput
