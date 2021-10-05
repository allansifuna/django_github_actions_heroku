FROM python:3.7
WORKDIR .
ADD . .
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
CMD gunicorn django_project.wsgi:application --bind 0.0.0.0:5000
