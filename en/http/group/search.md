# Get information of a single group

Get the information of a single group.

## Request address

> `/v1/group/id/{id}`

## Request method

> GET

## Request parameters

| Parameter name | Type | Required | Description |
| -------------- | ---- | -------- | ----------- |
| None           | None | None     | None        |

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

     "msg": "OK"，
     
     "data": {

   ​    "name": "xd1ddx111",

   ​    "type": 1,

   ​    "group_id": 2,

   ​    "rule_id": 4,

   ​    "create_at": 1660040788500,

   ​    "update_at": 1660094508689

     }

   }
```



