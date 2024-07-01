# Church Web Site with Auth
The aim is to develop a web site using VueJs, Python, Postgres, etc that all together is a good full stack.

# How to run

## Frontend

### NPM

Go to the frontend project.


```bash

cd ./web-app

```

Then, install the NPM packages.

```bash

npm install

```

Next, format the code.

```bash

npm run format

```

Final, run the serve.

```bash

npm run dev

```

### Container File

Here, we just need to go to web-app folder.

```bash

cd web-app

```

Then, build the image.

```bash

docker build -f Containerfile -t web-app:v1 .

```

Then, run it.


```bash

docker run -p 8082:80 web-app:v1

```

Next, just open the link http://localhost:8082.

## Backend

### Uvicorn

First, we should active the enviornment with the command:

```bash
poetry shell
```

Then, go to the web_api, and run the command.

```bash
uvicorn main:app --reload
```

Next, open the link http://127.0.0.1:8000/.

- http://127.0.0.1:8000/redoc - ReDoc
- http://127.0.0.1:8000/docs -> Swagger

If you want to deactivate, just write `exit` then click on enter.

```bash
exit
```

### Container File

Here, we just need to jump to web-api folder.

```bash

cd web-api

```

Then, build a new image.

```bash

docker build -f Containerfile -t web-api:v1 . 

```

Next, run it.

```bash

docker run -p 8000:8080 web-api:v1

```

Final, open the link http://localhost:8000/.

- http://localhost:8000/redoc - ReDoc
- http://localhost:8000/docs -> Swagger

## Compose

As an alternative, we can exeucte the compose to turn up all infrastructure.

In the root, just execute the command.

```bash

docker compose down && docker compose up --build

```

Here, we've been using nginx as reverse proxy of this system.

It will work to Docker and Podman with podman-compose.

### Plus

Check images.

```bash

docker images | grep auth

church-web-site-with-auth_backend         latest    d693235f4552   7 seconds ago    135MB
church-web-site-with-auth_frontend        latest    c030f08c0af2   21 seconds ago   44.4MB
church-web-site-with-auth_backend-proxy   latest    c5d1c77da304   41 seconds ago   43.2MB

```

Check containers.

```bash

docker ps       
                                
CONTAINER ID   IMAGE                                     COMMAND                  CREATED              STATUS              PORTS                                                                          NAMES
734498edd88b   church-web-site-with-auth_frontend        "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8082->80/tcp, :::8082->80/tcp                                          church-web-site-with-auth-frontend
e8bd90d3159a   church-web-site-with-auth_backend-proxy   "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:443->443/tcp, :::443->443/tcp, 0.0.0.0:8081->80/tcp, :::8081->80/tcp   church-web-site-with-auth-backend-proxy
c7c5afcce7db   church-web-site-with-auth_backend         "uvicorn main:app --…"   About a minute ago   Up About a minute   8080/tcp                                                                       church-web-site-with-auth-backend

```

# Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQL Alchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [VueJs](https://vuejs.org/)
- [Vue Router](https://router.vuejs.org/)
- [Pinia](https://pinia.vuejs.org/)
- [Axios](https://axios-http.com/docs/intro)
- [Bulma CSS V1](https://bulma.io/documentation/elements/button/)
- [Font Awesome V6.5.2](https://fontawesome.com/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Podman](https://podman.io/)
- [Podman Compose](https://docs.podman.io/en/latest/markdown/podman-compose.1.html)
- [nginx](https://nginx.org/en/)