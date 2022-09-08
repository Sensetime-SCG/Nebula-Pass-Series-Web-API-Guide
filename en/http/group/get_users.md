# Get user list of group

Get user list of group.

## Request address

> `/v1/group/id/{id}/users`


## Request method

> GET

## Request parameters

| Parameter name | Type | Required | Description |
| -------------- | ---- | -------- | ----------- |
| id             | int  | Y        | Group id    |

## Response parameters

| Parameter name | Type  | Description |
| -------------- | ----- | ----------- |
| items          | array | ID list     |

```
{

"code": 200,

"msg": "OK",

"data": {

"items":[

110399,

110400

]

}

}
```

