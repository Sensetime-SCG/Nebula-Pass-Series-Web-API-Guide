# Search

Search the 'id' list of related objects according to the specified fields.


## Request address

> `/v1/rule/search`

## Request method

> POST

- Body Type: `application/json`

## Request parameters
|  Parameter name       | Type   | Required | Description               |
| ---------- | ------ | ---- | ---------------------- |
| name       | String | N    | Search related objects according to this field |


## Request example:


> `/v1/rule/search`

```json
{
    "name":"A"
}
```


## Response example

```json
{
    "data": {
        "items": [
            2,
            55,
            117
        ]
    },
    "code": 200,
    "msg": "OK"
}
```