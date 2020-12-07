FROM python:3.7.3-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /code/
WORKDIR /code/

ADD requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

ADD . /code/
#RUN export $(cat ./.env | xargs)
EXPOSE 80
CMD exec python3 manage.py runserver 0.0.0.0:80