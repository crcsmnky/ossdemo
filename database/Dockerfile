FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get install -y software-properties-common

# add keys for galera and xtrabackup
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 BC19DDBA
RUN apt-key adv --recv-keys --keyserver keys.gnupg.net 1C4CBDCDCD2EFD2A

# add repositories for galera and xtrabackup
RUN add-apt-repository 'deb http://releases.galeracluster.com/ubuntu trusty main'
RUN add-apt-repository --enable-source 'deb http://repo.percona.com/apt trusty main'

# update apt
RUN apt-get update

# install galera, xtrabackup, etc.
RUN apt-get install -y galera-3 galera-arbitrator-3 mysql-wsrep-5.6 rsync lsof nano percona-xtrabackup

ADD my.cnf /etc/mysql/my.cnf
ADD add_user.sql /scripts/

EXPOSE 3306 4444 4567 4568

CMD service mysql start --wsrep-cluster-address=gcomm:// && tail -F /var/log/mysql/error.log
