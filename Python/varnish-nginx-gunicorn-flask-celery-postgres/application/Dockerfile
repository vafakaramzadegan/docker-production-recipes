FROM python:3.8

RUN apt update \
&& apt install -y \
# used to examine and control the state of services
systemctl \
# a tool to provide digital encryption and signing services
gnupg2 \
# process management system
supervisor

WORKDIR /application

COPY ./flaskr/requirements.txt flaskr/requirements.txt

RUN pip install \
# offers the advantage of not recompiling packages during every build process
wheel \
# make sure gunicorn will be installed even if it's not included in requirements.txt
gunicorn \
&& pip install -r ./flaskr/requirements.txt

COPY . .

# start nginx and supervisor, then start application based on
# env: "production" or "development"
WORKDIR ./flaskr
RUN chmod +x /application/entrypoint.sh
ENTRYPOINT ["/bin/bash", "/application/entrypoint.sh"]
