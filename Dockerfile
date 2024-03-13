FROM python:latest

ENV PYTHONUNBUFFERED 1

WORKDIR /testsite

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]