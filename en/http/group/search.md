# Get information of a single group

Get the information of a single group.

## Request address

> `/v1/group/id/{id}`

## Request method

> GET

## Request example

Get access group information for which `group_id` is 1.

> `/v1/group/id/1`

## Response examples

```json
{
    "data": {
        "name": "员工组",
        "type": 1,
        "group_id": 1,
        "rule_id": 0,
        "create_at": 1660284813955,
        "update_at": 1660284813955
    },
    "code": 200,
    "msg": "OK"
}
```