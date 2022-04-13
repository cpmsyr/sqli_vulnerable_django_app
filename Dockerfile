FROM python:3.9.5-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN  pip install -r requirements.txt
COPY . .
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
