FROM centos/systemd


# install requirements
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
    http://rpms.remirepo.net/enterprise/remi-release-7.rpm \
    yum-utils pcre-devel httpd

# install php5.6 from remi repository
RUN yum-config-manager --enable remi-php56 \
    && yum install -y php php-mcrypt php-cli php-gd php-curl php-mysql \
    php-ldap php-zip php-fileinfo php-mbstring php-pdo php56u-pdo php56u-common

# install PhalconPHP
RUN curl -s https://packagecloud.io/install/repositories/phalcon/stable/script.rpm.sh | bash
RUN yum update -y && yum install -y php-phalcon3

# start httpd
ADD run-httpd.sh /run-httpd.sh
RUN chmod -v +x /run-httpd.sh
CMD ["/run-httpd.sh"]