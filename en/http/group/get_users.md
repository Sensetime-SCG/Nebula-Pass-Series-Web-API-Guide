# Get user list of group

Get user list of group.

## Request address

> `/v1/group/id/{id}/users`


## Request method

> GET

## Request parameters

Get all `user_id` which `group_id` is 1

> `/v1/group/id/1/users`

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

