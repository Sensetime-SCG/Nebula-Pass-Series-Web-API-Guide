# 批量获取人员的信息

根据指定的`offset`与`limit`获取人员信息。要求 `offset`值范围是 0 到 100000；`limit`值范围是 0 到 10。

## 请求路径

> `/v1/user/offset/{offset}/limit/{limit}`

## 请求方式

> GET


## 响应参数

| 字段   | 类型         | 释义                   |
| ------ | ------------ | ---------------------- |
| offset | int          | 当前数据条目请求偏移量 |
| limit  | int          | 当前数据条目获取上限   |
| count  | int          | 当前获取数据条目数量   |
| total  | int          | 数据条目总量           |
| items  | object array | 数据条目               |

## 请求示例

获取起始偏移为0，当前获取数据条目上限为2，其中`count`字段表示为当前获取到的数据条目量，`total`字段表示数据库中的总条目数。

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
                "pin":"",
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
                "pin":"",
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