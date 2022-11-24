FROM debian:bullseye

# default shell to bash
SHELL ["/bin/bash", "--login", "-c"]
ENV TERM=xterm

RUN apt-get update
# Debian dependencies
RUN apt-get install --yes sqlite3 python3 python3-pip
# Copy source code and python dependencies
RUN mkdir -p /usr/share/users-polls
RUN mkdir -p /opt
COPY ./src/* /usr/share/users-polls/
COPY ./requirements.txt /usr/share/users-polls/requirements.txt
COPY docker_entrypoint /opt/docker_entrypoint

RUN python3 -m pip install -r /usr/share/users-polls/requirements.txt

RUN chmod -R +x /usr/share/users-polls/
RUN chmod +x /opt/docker_entrypoint
EXPOSE 9999

ENTRYPOINT ["/opt/docker_entrypoint"]