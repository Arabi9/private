# Basierend auf Alpine für minimale Größe
FROM alpine:3.18

# Installiere Abhängigkeiten
RUN apk add --no-cache python3 py3-pip tor openssl docker-cli

# Konfiguriere Tor
COPY config/torrc /etc/tor/torrc
RUN mkdir /var/lib/tor && chown -R tor /var/lib/tor

# Python-Setup
WORKDIR /app
COPY c2_server/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Kopiere App-Code
COPY c2_server/app /app

# Startskript
COPY c2_server/start_c2.sh /start_c2.sh
RUN chmod +x /start_c2.sh

EXPOSE 80 9050
CMD ["/start_c2.sh"]
