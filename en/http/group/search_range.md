# Get all group information

Get group list.

## Request address

> `/v1/group/offset/{offset}/limit/{limit}`

## Request method

> GET


## Request example

The starting offset of acquisition is 0, and the upper limit of currently acquired data items is 10, where the `count` field represents the number of currently acquired data items, and the `total` field represents the total number of entries in the database.

> `/v1/group/offset/0/limit/10`

## Response example

```json
{
    "data": {
        "offset": 0,
        "limit": 10,
        "count": 1,
        "total": 1,
        "items": [
            {
                "name": "员工组",
                "type": 1,
                "group_id": 1,
                "rule_id": 0,
                "create_at": 1660284813955,
                "update_at": 1660284813955
            }
        ]
    },
    "code": 200,
    "msg": "OK"
}
```