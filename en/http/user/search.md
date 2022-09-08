# Query user information

Query user information.

## Request address

> `/v1/user/id/{id}`

## Request method

> GET

## Request parameters

| Parameter name | Type | Required | Description |
| -------------- | ---- | -------- | ----------- |
| None           | None | None     | None        |

## Response parameters

| Parameter name   | Type    | Description                                        |
| ---------------- | ------- | -------------------------------------------------- |
| name             | string  | User name                                          |
| user_id          | int     | The unique id set by the commit side               |
| type             | int     | 1：employee 2：visitor                             |
| avatar           | string  | Person avatar, basemap                             |
| feature          | string  | Feature value                                      |
| ic_number        | string  | IC number                                          |
| id_number        | string  | ID number                                          |
| job_number       | string  | Job number                                         |
| guest_time_start | int     | Visit start time, Unix, timestamp in milliseconds. |
| guest_time_end   | int     | Visit end time, Unix, timestamp in milliseconds.   |
| groups           | int []  | List of binding groups                             |
| is_admin         | boolean | Whether to enable administrator privileges         |
| remark           | string  | Remark                                             |
| create_at        |         |                                                    |
| update_at        |         |                                                    |

Example of successful return：

```
{

"code": 200,

"msg": "OK",

"data": {

“user_id”:1,

"avatar": "",

"feature": "",

"type": 1,

"remark": "",

"name": "",

"ic_number": "",

"id_number": "",

"guest_time_start": 1606123080000,

"guest_time_end": 1606123099000,

"groups": [],

" is_admin ": false,

“create_at”:”1658471422626”,

“update_at”:”1658471422626”

}

}
```



