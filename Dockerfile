#
# This Dockerfile is meant for testing only.
#
FROM python:3.6

EXPOSE 80
WORKDIR /app
ENV DJANGO_SETTINGS_MODULE=nanites.settings
RUN pip install --upgrade pip && \
    pip install 'Django>2.1,<3' && \
    pip install requests && \
    pip install mysqlclient && \
    pip install nose && \
    pip install six && \
    pip install python_dateutil && \
    pip install urllib3 && \
    pip install django-nose && \
    pip install Sphinx>2 && \
    pip install sphinx-py3doc-enhanced-theme>=2.4.0 && \
    pip install recommonmark==0.5.0

CMD ./wait-for-it.sh -t 120 nanites:80 && ./manage.py test -v 2
