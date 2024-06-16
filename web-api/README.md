# Backend API

## Auth

First of all, we should register a new user.

```json

{
  "username": "admin",
  "email": "admin@site.com",
  "full_name": "Admin System",
  "disabled": false,
  "scopes": [
    "account:read",
    "account:write",
    "small-group:read",
    "small-group:write",
    "address:read"
  ],
  "password": "Admin@1234"
}

```

Or, when we want to provide access an application.

```json

{
  "username": "ui-vuejs",
  "email": "ui-vue@site.com",
  "full_name": "UI VueJs System",
  "disabled": false,
  "scopes": [
    "account:read",
    "small-group:read",
    "address:read"
  ],
  "client_id": "ui-vuejs",
  "client_secret": "0019c6d7dc039eef82af1add60e9e6bb40dcbe5f1a65a10248cec793eacb379c",
  "password": "Admin@1234"
}

```

Then, we should update their scopes (permissions).

```json
{
  "scopes": [
    "account:read",
    "account:write",
    "small-group:read",
    "small-group:write",
    "address:read"
  ]
}
```