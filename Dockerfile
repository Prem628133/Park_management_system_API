FROM python:3.12-slim

WORKDIR /Myapp

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

EXPOSE 8001

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8001"]
