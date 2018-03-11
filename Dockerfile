FROM python:3.5-onbuild
RUN mkdir -p /opt/dot/
COPY requirements.txt /opt/dot/
WORKDIR /opt/dot/
RUN pip install -r requirements.txt
COPY . /opt/dot/
EXPOSE 8000
CMD ./manage.py runserver 0.0.0.0doc:8000
