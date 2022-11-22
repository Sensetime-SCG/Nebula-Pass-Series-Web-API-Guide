# Create Group

Create group, max to 100 groups.

## Request address

> `/v1/group`

## Request method

> POST

- Body Type: `application/json`

## Request parameters: 

| Parameter name | Type   | Required | Description                                                  |
| -------------- | ------ | -------- | ------------------------------------------------------------ |
| type           | int    | N        | Group type，1:employees，2：visitors；Default：1  </n>Cannot be modified after creation |
| group_id       | int    | Y        | The unique identifier id set by the submitter, non-repeatable, greater than 0 and less than 999999. |
| name           | string | Y        | Group name, the length is 1\~128 bytes, non-repeatable, and cannot involve special characters. |
| rule_id        | int    | N        | The binding rule id, if it is 0, it will not be bound to any rule. |

```json
{
  "name": "员工组",
  "type": 1,
  "group_id": 1,
  "rule_id": 0
}
```
## Response example

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