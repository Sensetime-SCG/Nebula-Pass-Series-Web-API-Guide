# Authentication Management

## /v1/auth/login Log in

1.  Function description

Get JWT token.

The account password is the login password of the stand-alone mode.

2. Request address

https://HOST:PORT/v1/auth/login

3. Request method

POST

4. Request parameters

| Parameter Name | Type   | Required | Description                                                  |
| -------------- | ------ | -------- | ------------------------------------------------------------ |
| username       | string | Y        | Account name                                                 |
| password       | string | Y        | Password                                                     |
| validTime      | int    | N        | Token validity period, in minutes, the valid value is greater than 0 and less than 1440, the default value is 5 minutes |

Request example：

```
{
"username": "admin",
"password": "string",
"validTime": 5
}
```

5.  Response parameters

| Parameter Name | Type   | Description                                                  |
| -------------- | ------ | ------------------------------------------------------------ |
| token          | string | The session id, in the form of: "7a4280edd410cc367526e2687d3458ed" This parameter will be used as the AUTH-TOKEN authentication parameter for other subsequent requests. |

Response example：

```
{
"code":200,
"msg":"OK",
"data":{
	"token":"3eddec1c45d3158e805a172409c881b8"
}
}
```

