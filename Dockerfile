FROM python:3.6

EXPOSE 80
WORKDIR /app
ENV DJANGO_SETTINGS_MODULE=nanites.settings
RUN pip install --upgrade pip && \
    pip install Django>2.1 && \
    pip install requests && \
    pip install mysqlclient && \
    pip install nose && \
    pip install six && \
    pip install python_dateutil && \
    pip install urllib3 && \
    pip install django-nose

CMD ./wait4db.py && ./manage.py test -v 2
