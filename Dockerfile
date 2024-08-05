FROM ubuntu:latest
RUN mkdir /home/ubuntu/cacao_linux
COPY /cacao_linux /home/ubuntu/cacao_linux/.
RUN mkdir /home/ubuntu/website
COPY /website /home/ubuntu/website/.

RUN ls /home/ubuntu/cacao_linux
RUN ls /home/ubuntu
RUN cd /home/ubuntu/cacao_linux && ls && bash install.sh
