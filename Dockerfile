FROM python:3.7
WORKDIR .
ADD . .
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
CMD python manage.py runserver 0.0.0.0:$PORT
