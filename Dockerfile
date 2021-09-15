FROM python:3.7

ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}

ENV PYTHONUNBUFFERED 1

RUN pip install pipenv

# Adds our application code to the image
COPY . code
WORKDIR code

RUN pipenv install --system --deploy

EXPOSE 8000

RUN chown -R ${APP_USER} /code
USER ${APP_USER}:${APP_USER}

# Migrates the database, uploads staticfiles, and runs the production server
CMD ./manage.py migrate && \
    ./manage.py collectstatic --noinput && \
    newrelic-admin run-program gunicorn --bind 0.0.0.0:8000 --access-logfile - backend.wsgi:application
