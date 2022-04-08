# Dockerfile
FROM python:3.7-stretch
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN cd databaseApi 
RUN pip install -r requirements.txt
RUN cd ..
ENTRYPOINT ["python"]
CMD ["run.py"]
