#
# This Dockerfile is meant for testing only.
#
FROM python:3.10-bullseye

EXPOSE 80
WORKDIR /app
ENV DJANGO_SETTINGS_MODULE=nanites.settings
RUN pip install --upgrade pip && \
    pip install 'Django>3,<4' && \
    pip install requests && \
    pip install mysqlclient && \
    pip install six && \
    pip install python_dateutil && \
    pip install urllib3 && \
    pip install Sphinx>2 && \
    pip install sphinx-py3doc-enhanced-theme>=2.4.0 && \
    pip install recommonmark==0.5.0

CMD ./wait-for-it.sh -t 120 nanites:80 && ./manage.py test -v 2
