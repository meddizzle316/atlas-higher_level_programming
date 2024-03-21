FROM ubuntu:20.04
ENV TZ=America/Chicago
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update --fix-missing && apt-get upgrade -y --fix-missing
RUN apt-get install -y git
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y python3-lxml
RUN apt-get install -y nodejs
RUN apt-get install -y node-fetch
RUN npm install semistandard --global
