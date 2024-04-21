FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY . /app
WORKDIR /app

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD celery -A upload_file_api worker -l INFO