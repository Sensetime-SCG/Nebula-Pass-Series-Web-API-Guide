# Create Group

Create group, max to 100 groups.

## Request address

> `/v1/group`

## Request method

> POST

## Request parameters: 

| Parameter name | Type   | Required | Description                                                  |
| -------------- | ------ | -------- | ------------------------------------------------------------ |
| type           | int    | N        | Group type，1:employees，2：visitors；Default：1  </n>Cannot be modified after creation |
| group_id       | int    | Y        | The unique identifier id set by the submitter, non-repeatable, greater than 0 and less than 999999. |
| name           | string | Y        | Group name, the length is 1\~32 bytes, non-repeatable, and cannot involve special characters. |
| rule_id        | int    | N        | The binding rule id, if it is 0, it will not be bound to any rule. |

```
{

“group_id”:1,
"type": 1,
"name": "GroupA",
“rule_id”: 1
}
```

## Response parameters

| Parameter name | Type   | Description                                         |
| -------------- | ------ | --------------------------------------------------- |
| group_id       | int    | Group id                                            |
| type           | int    |                                                     |
| name           | string |                                                     |
| rule_id        | int    |                                                     |
| create_at      | int    | Create time (format is Unix, millisecond timestamp) |
| update_at      | string | Update time(format is Unix, millisecond timestamp)  |

```
{

"code": 200,
"msg": "OK",
"data": {
"group_id": 2,
"type": 1,
"name": "GroupA"
"rule_id": 1,
"create_at": "1658471422626 ",
"update_at": "1658471422626 ",
}
}
```

