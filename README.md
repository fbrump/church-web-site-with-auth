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

## Container File

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

It will work to Docker and Podman with podman-compose.

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