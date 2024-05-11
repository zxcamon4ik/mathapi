FROM python:3.12

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/wd
ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip \
    pip install --requirement requirements.txt

COPY --chown=${USER}:555 ./docker/service/entrypoint.sh /entrypoint.sh
COPY --chown=${USER}:555 ./docker/service/start.sh /start.sh

COPY --chown=${USER} ./Makefile Makefile
COPY --chown=${USER} ./manage.py manage.py
COPY --chown=${USER} ./core core
COPY --chown=${USEr} ./apps apps

USER ${USER}

RUN chmod +x /entrypoint.sh
RUN chmod +x /start.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/start.sh"]