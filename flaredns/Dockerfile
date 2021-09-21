#ARG BUILD_FROM
#FROM ${BUILD_FROM}
FROM homeassistant/armv7-base-python:latest

ENV LANG C.UTF-8

# Setup base
RUN pip3 install cloudflare

# Copy data
COPY data/*.sh /
COPY data/dyndns.py /dyndns.py

RUN chmod a+x /run.sh

CMD ["/run.sh"]
