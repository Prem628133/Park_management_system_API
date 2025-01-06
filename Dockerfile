FROM python:3.12-slim

WORKDIR /Myapp

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . . 

EXPOSE 8001

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
