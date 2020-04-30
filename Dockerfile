FROM python:3-alpine
RUN mkdir /code
COPY . /code/
WORKDIR /code
RUN pip3 install -r requirements.txt
EXPOSE 8000
STOPSIGNAL SIGTERM
CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]
