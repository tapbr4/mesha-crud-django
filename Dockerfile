FROM python:3.10

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt
COPY . /opt/app

ADD . / ./

CMD python manage.py runserver 0.0.0.0:8000

#docker run -p 8001:8000 -it --rm mesha-image 
#localhost:8001