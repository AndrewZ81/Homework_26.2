FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
#CMD flask run -h 0.0.0.0 -p 80
CMD gunicorn -b 0.0.0.0:80 -w 4 main:app
