FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt && python manage.py migrate --run-syncdb && python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "--host", "0.0.0.0"]
