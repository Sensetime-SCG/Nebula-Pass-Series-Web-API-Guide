# Modify group information

Modify group information，`group_id` field and `type` field values cannot be modified。


## Request address

> `/v1/group/id/{id}`

## Request method

> PUT

- Body Type: `application/json`

## Request parameters

| Parameter name | Type   | Required | Description |
| -------------- | ------ | -------- | ----------- |
| name           | string | Y        | Group name  |
| rule_id        | int    | N        | Rule id     |

## 请求示例:

update group infomation which `group_id` is 3.

> `/v1/group/id/3`

```json
{
  "name": "员工组",
  "rule_id": 0
}
```