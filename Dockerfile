FROM python:3.8.4-slim

# RUN groupadd -r cocktail && useradd --no-log-init -r -g cocktail cocktail
RUN mkdir /cocktail_master
WORKDIR /cocktail_master
COPY . /cocktail_master/
RUN pip install -r requirements.txt
RUN useradd -m cocktail
USER cocktail

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENTRYPOINT ["/cocktail_master/entrypoint.sh"]
