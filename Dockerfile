FROM python:3.8.4-slim

RUN useradd -m cocktail
RUN mkdir /cocktail_master && chown cocktail:cocktail /cocktail_master
COPY --chown=cocktail:cocktail . /cocktail_master/
RUN pip install -r /cocktail_master/requirements.txt
USER cocktail
WORKDIR /cocktail_master

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENTRYPOINT ["/cocktail_master/entrypoint.sh"]
