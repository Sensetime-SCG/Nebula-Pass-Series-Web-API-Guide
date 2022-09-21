# Query list of user information

Query list of user information.

## Request address

> `/v1/user/offset/{offset}/limit/{limit}`

## Request method

> GET

## 请求示例

The starting offset of acquisition is 0, and the upper limit of currently acquired data entries is 2, where the `count` field represents the number of currently acquired data items, and the `total` field represents the total number of entries in the database.

> `/v1/user/offset/0/limit/2`

## 返回示例

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