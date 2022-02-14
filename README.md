# Docker Production Recipes

Deploying big applications in a production environment can be a tough grind, as far as installing specific packages like a Web Server, Reverse Proxy, Database Engine, etc. And On top of that, replicating the same stack on multiple machines also takes extra time and energy.

**Docker** facilitates the whole process. It's a container-based open platform for developing, deploying, and running applications.
Thanks to its Containerization technology, Docker makes it possible to deploy multiple applications with totally different supporting software and ecosystem on the same machine without causing conflicts.

There are many methods and conventions for structuring your application as well as Dockerfiles and other configurations.

This repository contains several boilerplates especially curated for production environments. They can be easily tweaked and deployed.

## Boilerplates

### Python
- [varnish-nginx-flask-celery-postgres](https://github.com/vafakaramzadegan/docker-production-recipes/tree/main/Python/varnish-nginx-gunicorn-flask-celery-postgres)

## How To Use

Using a boilerplate is easy. **Docker** and **docker-compose** must be installed on your machine.
- Download/Clone the repo.
- Open a terminal.
- `cd` to the directory of the boilerplate you want.
- invoke `docker-compose up -d --build`. this builds the image and `-d` tells Docker to run the containers in the background (Detached mode). The first time you build the image may take a while, however consecutive builds will become much faster.
- use `docker-compose down` to stop and remove containers. you may use `--volume` to remove named volumes declared in the Compose file.

## Contributing

Any contributions are greatly appreciated. 
- If you have suggestions, feel free to open an issue to discuss it.
- If you want to improve boilerplates or add a new one, you can fork this project, implement your code and open a pull request.