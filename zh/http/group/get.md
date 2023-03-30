# 查询通行组的信息

根据指定的`group_id`获取该通行组信息

## 请求路径

> `/v1/group/id/{id}`

## 请求方式

> GET


## 请求示例

获取`group_id`为 1 的通行组信息。

> `/v1/group/id/1`

## 返回示例

```json
{
    "data": {
        "name": "员工组",
        "type": 1,
        "group_id": "1",
        "rule_id": "",
        "create_at": 1660284813955,
        "update_at": 1660284813955
    },
    "code": 200,
    "msg": "OK"
}
```