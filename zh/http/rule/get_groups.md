# 获取指定策略下绑定的通行组

获取所有已绑定该`rule_id`通行组的`group_id`。

## 请求路径

> `/v1/rule/id/{id}/groups`


## 请求方式

> GET

## 请求示例

获取所有绑定`rule_id`为 1 的人员的`group_id`。

> `/v1/rule/id/1/groups`

```json
{
    "data": {
        "items": [
            "1",
            "2"
        ]
    },
    "code": 200,
    "msg": "OK"
}
```