# Varnish-Httpd-PhalconPHP3-Mysql

This stack is all you need to deploy your PhalconPHP applications in a production environment.
[INVO Application](https://github.com/phalcon/invo) is used for demonstration.

- **Varnish Cache Server** which is a powerful, high-performance HTTP accelerator designed for speeding up the website by up to 1000 percent by caching (or storing) a copy of a webpage the first time a user visits.
- **HTTPD** is an HTTP server daemon produced by the Apache Foundation.
- **Phalcon** is an open source full stack framework for PHP, written as a C-extension. Phalcon is optimized for high performance. Its unique architecture allows the framework to always be memory resident, offering its functionality whenever it’s needed, without expensive file stats and file reads that traditional PHP frameworks employ.
- **MySQL** Database Service is a fully managed database service to deploy cloud-native applications.

**DON'T FORGET** to **ENABLE** and **CONFIGURE** the Firewall on the host machine.

## Default values

Default values are stored in the `.env` file. remember to **CHANGE** the username and password!