FROM python:3
ENV PYTHONUNBUFFERED=1
RUN pip install psycopg2

WORKDIR /app

COPY ./requirement.txt .
RUN pip install -r requirement.txt

COPY ./cook_book .
COPY .env .

#RUN python3 manage.py runserver 0.0.0.0:8000
