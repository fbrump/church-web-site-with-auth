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

### 

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


# Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [VueJs](https://vuejs.org/)
- [Bulma CSS V1](https://bulma.io/documentation/elements/button/)
- [Font Awesome V6.5.2](https://fontawesome.com/)