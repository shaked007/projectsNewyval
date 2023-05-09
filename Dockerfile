FROM quay.service.idf/ubi7/python-38
ENV PYTHONUNBUFFERED 1 
ENV PYTHONDONTWRITEBYTECODE 1
# RUN mkdir /code
ADD . /code/
WORKDIR /code
RUN pip config set global.index https://repo.cloud.idf/repository/pip
RUN pip config set global.index-url https://repo.cloud.idf/repository/pip/simple
RUN pip config set global.trusted-host repo.cloud.idf
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000

# # FROM quay.service.idf/rhel8/postgresql-13
# FROM quay.service.idf/rhel8/postgresql-12
# ENV POSTGRESQL_USER=newval 
# ENV POSTGRESQL_PASSWORD=admin
# ENV POSTGRESQL_DATABASE=dohamal