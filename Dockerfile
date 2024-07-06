# Dockerfile reference: https://docs.docker.com/reference/dockerfile/#from

FROM python:3.12 AS base 

LABEL maintainer="Maks Svid, <Telegram: mak_sjr>"

ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}

RUN useradd -m -u $UID docker_user 