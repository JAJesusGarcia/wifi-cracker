# docker/Dockerfile
FROM kalilinux/kali-rolling

RUN apt-get update && apt-get install -y \
    aircrack-ng \
    python3 \
    python3-pip \
    tcpdump \
    iproute2 \
    macchanger \
    git \
    && apt-get clean

WORKDIR /app
COPY . /app
RUN ls -l /app/wordlist # Añadimos este comando para listar el contenido de la carpeta