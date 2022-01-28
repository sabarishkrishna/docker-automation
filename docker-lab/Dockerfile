FROM ubuntu:18.04
ENV HOSTNAME myhostc
ENV DEBIAN_FRONTEND=noninteractive


RUN apt update && apt upgrade -y
RUN apt install wireguard curl figlet nano git net-tools iputils-ping iproute2 openssh-server -y

RUN bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"

RUN sed -i 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/' /etc/sysctl.conf 
RUN sysctl -p


COPY scripts/labs /etc/update-motd.d/
RUN chmod -x /etc/update-motd.d/*
RUN chmod +x /etc/update-motd.d/labs

RUN bash /etc/update-motd.d/labs

RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN service ssh start

RUN echo 'root:hacker' | chpasswd



WORKDIR /etc/wireguard
RUN umask 077


RUN wg genkey | tee privatekey | wg pubkey > publickey

RUN touch wg0.conf

EXPOSE 22 51820

CMD ["/usr/sbin/sshd", "-D"]
