# Dockerfile reference: https://docs.docker.com/reference/dockerfile/#from

FROM python:3.12 AS base 

LABEL maintainer="Maks Svid, <Telegram: mak_sjr>"

ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}

RUN useradd -m -u $UID docker_user 

USER docker_user

WORKDIR /home/docker_user/app

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt ./
RUN pip install -r requirements.txt 

COPY . .

CMD ["python 3", "-m", "bot.main"] 