# Get Error Reference Code

All recorded error reference codes of the current interface

## Request address

> `/v1/auth/errors`

## Request method

> GET

## Request parameters

> None

## Response example

```json
{
    "data": [
        {
            "code": 0,
            "msg": "Not define target code error message,please contact developer"
        },
        {
            "code": 200,
            "msg": "OK"
        },
        {
            "code": 401,
            "msg": "Unauthorized"
        },
        {
            "code": 404,
            "msg": "Not Found"
        },
        {
            "code": 500,
            "msg": "Internal Server Error"
        },
        {
            "code": 1000,
            "msg": "Account Not Exist"
        },
        {
            "code": 1001,
            "msg": "Password Wrong"
        }
    ],
    "code": 200,
    "msg": "OK"
}
```