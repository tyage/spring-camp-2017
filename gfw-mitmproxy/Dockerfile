FROM mitmproxy/mitmproxy
MAINTAINER tyage <namatyage@gmail.com>

RUN set -x && \
    mkdir -p /opt/gfw

COPY gfw.py /opt/gfw

CMD mitmdump -s /opt/gfw/gfw.py --no-http2

EXPOSE 8080 8080
