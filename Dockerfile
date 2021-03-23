FROM python:3.8.4-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /cocktail_master
WORKDIR /cocktail_master
COPY . /cocktail_master/
RUN pip install -r requirements.txt
ENTRYPOINT ["/cocktail_master/entrypoint.sh"]
