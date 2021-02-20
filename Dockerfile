FROM python:3

WORKDIR /app

# copy files needed by docker
COPY ["./app/apartment-notifyer.py", "docker-entrypoint.sh", "./app/requirements.txt", "docker-entrypoint.sh", "./"]

# install python modules
RUN pip3 install --no-cache-dir -r requirements.txt

# environment variables
ENV PUSHOVER_TOKEN=""
ENV PUSHOVER_KEY=""
ENV UPDATE_INTERVAL="60"

# run script to set up default config if non existing, then start
CMD [ "/bin/bash", "/app/docker-entrypoint.sh" ]
