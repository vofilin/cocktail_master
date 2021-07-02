FROM python:3.8.4-slim

# RUN groupadd -r cocktail && useradd --no-log-init -r -g cocktail cocktail
RUN mkdir /cocktail_master
COPY . /cocktail_master/
RUN pip install -r /cocktail_master/requirements.txt
RUN useradd -m cocktail
RUN chown -R cocktail:cocktail /cocktail_master
USER cocktail
WORKDIR /cocktail_master

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENTRYPOINT ["/cocktail_master/entrypoint.sh"]
