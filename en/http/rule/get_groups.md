# Query the group bound to the specified rule

Query the group bound to the specified rule.

## Request address

> `/v1/rule/id/{id}/groups`


## Request method

> GET

## Response example

get all group which bind `rule_id` is 1

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