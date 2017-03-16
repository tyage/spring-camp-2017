FROM centos:latest
MAINTAINER tyage <namatyage@gmail.com>

RUN set -x && \
    yum update -y && \
    yum install -y squid python && \
    touch /var/log/squid/access.log && \
    chown squid /var/log/squid/access.log && \
    mkdir -p /usr/local/var/log/squid/ && \
    chown squid:squid /usr/local/var/log/squid/ && \
    mkdir /opt/gfw && \
    curl https://bootstrap.pypa.io/get-pip.py | python && \
    pip install pyicap

COPY squid.conf /etc/squid
COPY server.py /opt/gfw
COPY run.sh /opt/gfw

CMD sh /opt/gfw/run.sh && tail -10f /var/log/squid/access.log

EXPOSE 3128 3128
