# 批量获取通行组的信息

根据指定的`offset`与`limit`获取通行组信息。要求 `offset`值范围是 0 到 100000；`limit`值范围是 0 到 100。

## 请求路径

> `/v1/group/offset/{offset}/limit/{limit}`

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

获取起始偏移为0，当前获取数据条目上限为10，其中`count`字段表示为当前获取到的数据条目量，`total`字段表示数据库中的总条目数。

> `/v1/group/offset/0/limit/10`

## 返回示例

```json
{
    "data": {
        "offset": 0,
        "limit": 10,
        "count": 1,
        "total": 1,
        "items": [
            {
                "name": "员工组",
                "type": 1,
                "group_id": "1",
                "rule_id": "",
                "create_at": 1660284813955,
                "update_at": 1660284813955
            }
        ]
    },
    "code": 200,
    "msg": "OK"
}
```