# Modify group information

Modify group information，`group_id` field and `type` field values cannot be modified。


## Request address

> `/v1/group/id/{id}`

## Request method

> PUT

## Request parameters

| Parameter name | Type   | Required | Description |
| -------------- | ------ | -------- | ----------- |
| name           | string | Y        | Group name  |
| rule_id        | int    | N        | Rule id     |

## Response parameters

| Parameter name | Type   | Description                                         |
| -------------- | ------ | --------------------------------------------------- |
| group_id       | int    | Group ID                                            |
| name           | string | Group name                                          |
| type           | int    | Group type                                          |
| rule_id        | int    | Rule id                                             |
| create_at      | int    | Create time (format is Unix, millisecond timestamp) |
| update_at      | string | Update time(format is Unix, millisecond timestamp)  |

```
{

"code": 200,

"msg": "OK",

"data": {

“name”:”A”,

“type”:1,

"group_id": 2,

“rule_id”: 1,

"create_at": "1658471422626 ",

"update_at": "1658471422626 "

}

}
```

