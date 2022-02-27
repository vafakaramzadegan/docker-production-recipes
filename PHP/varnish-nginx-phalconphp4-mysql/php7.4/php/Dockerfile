FROM php:7.4-fpm


WORKDIR /website

ARG DEBIAN_FRONTEND=noninteractive

# update package list and install GnuPG which
RUN apt update && apt install -y gnupg

# gd requires zlib1g-dev libzip-dev which are available on Dotdeb repo.
RUN echo "deb http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list \
    && echo "deb-src http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list \
    && curl -sS --insecure https://www.dotdeb.org/dotdeb.gpg | apt-key add -

# install gd, Imagick and their requirements
RUN apt install -y \
        curl \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        libmagickwand-dev --no-install-recommends \
        apt-utils \
        zlib1g-dev \
        libzip-dev \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) gd fileinfo gettext json zip mysqli pdo_mysql \
    && pecl channel-update pecl.php.net \
    && pecl install imagick && docker-php-ext-enable imagick \
    # this installs phalcon from PECL
    && pecl install phalcon-4.1.2

RUN echo "extension=psr.so" > /usr/local/etc/php/conf.d/19-psr.ini \
    && echo "extension=phalcon.so" > /usr/local/etc/php/conf.d/20-phalcon.ini

# setup composer and install project dependencies. this step is optional.
# if you don't use composer or a package manager, simply delete the following lines.
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
# since we're overriding the default entrypoint, the php-fpm must be invoked manually
CMD composer install && php-fpm