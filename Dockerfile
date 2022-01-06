# Base Image
FROM alpine:latest

# App directory and setup
RUN mkdir -p /app/cogs
WORKDIR /app
ENV PYTHONUNBUFFERED=1
ENV TZ=Australia/Melbourne
COPY main.py options.json requirements.txt /app/
RUN apk add --update --no-cache ffmpeg python3 python3-dev musl-dev make libffi-dev gcc && ln -sf python3 /usr/bin/python && python3 -m ensurepip && pip3 install --no-cache --upgrade pip setuptools && pip3 install --no-cache-dir -r requirements.txt
COPY cogs/newworld.py cogs/debug.py /app/cogs/


# Startup
CMD python3 /app/main.py