FROM python:3.13
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD exec gunicorn --bind 0.0.0.0:$PORT app:app

