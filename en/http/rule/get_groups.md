# Query the group bound to the specified rule

Query the group bound to the specified rule.

## Request address

> `/v1/rule/id/{id}/groups`


## Request method

> GET

## Request parameters

| Parameter name | Type | Required | Description |
| -------------- | ---- | -------- | ----------- |
| None           | None | None     | None        |

## Response parameters

| Parameter name | Type  | Description |
| -------------- | ----- | ----------- |
| items          | array | ID list     |

> `/v1/rule/id/1/groups`

```json
{
    "data": {
        "items": [
            1,
            2
        ]
    },
    "code": 200,
    "msg": "OK"
}
```