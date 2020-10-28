FROM python:3.8.3-slim-buster
# start from some image

ENV PYTHONUNBUFFERED 1

WORKDIR /app 

# install some packages
RUN apt-get update \
   && apt-get -y install netcat gcc \
   && apt-get clean                     

# run commands
RUN pip install --upgrade pip 

EXPOSE 8000

# copy files
COPY ./requirements.txt .

# install dependencies
RUN pip install -r requirements.txt 

# add default command, can be overwritten
CMD uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000