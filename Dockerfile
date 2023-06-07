FROM debian:9

RUN apt-get update -yq \
&& apt-get dist-upgrade -yq \
&& apt-get upgrade -yq \
&& apt-get install curl gnupg -yq \
&& apt-get install python3 -yq \
&& apt-get install pip -yq \
&& apt-get install make -yq \
&& apt-get clean -y \
&& apt-get autoremove -y \
&& apt-get autoclean -y

ADD . .

RUN make prepare
RUN make build

EXPOSE 80

CMD make tests_run
