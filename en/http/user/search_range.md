# Query list of user information

Query list of user information.

## Request address

> `/v1/user/offset/{offset}/limit/{limit}`

## Request method

> GET

## Request parameters

| Parameter name | Type | Required | Description                                                  |
| -------------- | ---- | -------- | ------------------------------------------------------------ |
| offset         | int  | Y        | The data offset of the current page, which must be greater than or equal to 0 and less than 100000 |
| limit          | int  | Y        | The data item limit of the current page must be greater than 0 and less than or equal to 10 |

## Response parameters

| Parameter name | Type  | Description                                                |
| -------------- | ----- | ---------------------------------------------------------- |
| items          | Array | List of user information retrieved from request parameters |

**Description of each element field in items**

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

Response example：

```json
{
    "data": {
        "offset": 0,
        "limit": 2,
        "count": 2,
        "total": 10,
        "items": [
            {
                "user_id": 2,
                "name": "张三",
                "type": 1,
                "avatar": "xxxxxxxx",
                "ic_number": "",
                "id_number": "",
                "job_number": "",
                "guest_time_start": 0,
                "guest_time_end": 0,
                "groups": [],
                "is_admin": false,
                "remark": "",
                "create_at": 1660222970940,
                "update_at": 1660222971252
            },
            {
                "user_id": 1,
                "name": "管理员",
                "type": 1,
                "avatar": "xxxxxxxx",
                "ic_number": "",
                "id_number": "",
                "job_number": "",
                "guest_time_start": 0,
                "guest_time_end": 0,
                "groups": [],
                "is_admin": true,
                "remark": "",
                "create_at": 1660222080940,
                "update_at": 1660222192202
            }
        ]
    },
    "code": 200,
    "msg": "OK"
}

```