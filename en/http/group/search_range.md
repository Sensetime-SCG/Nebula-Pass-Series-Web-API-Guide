# Get all group information

Get group list.

## Request address

> `/v1/group/offset/{offset}/limit/{limit}`

## Request method

> GET

## Request parameters

| Parameter name | Type | Required | Description                                                  |
| -------------- | ---- | -------- | ------------------------------------------------------------ |
| offset         | int  | Y        | The data offset of the current page, which must be greater than or equal to 0 and less than 100000 |
| limit          | int  | Y        | The data item limit of the current page must be greater than 0 and less than or equal to 10 |

Request address：

https://HOST:PORT/v1/group/offset/0/limit/3

## Response parameters

| Parameter name | Type  | Description                     |
| -------------- | ----- | ------------------------------- |
| offset         | int   | The current offset              |
| limit          | int   | The current data item limit     |
| total          | int   | The total item number           |
| items          | array | The currently fetched data item |

items data structure

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

"limit": 2,

“offset”: 0

“total”: 100

“items”:[

{

“group_id”:1,

"name": "Defaultgroup",

"type": 1,

“rule_id”:1,

"create_at": "1658471422626 ",

"update_at": "1658471422626 ",

},
{

“group_id”:2,

"name": "GroupB",

"type": 1,

“rule_id”:2,

"create_at": "1658471422626 ",

"update_at": "1658471422626 "

}

]

}

}
```



