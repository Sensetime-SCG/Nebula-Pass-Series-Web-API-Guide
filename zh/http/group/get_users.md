# 获取指定通行组下绑定的人员

获取所有已绑定该`group_id`人员的`user_id`。

## 请求路径

> `/v1/group/id/{id}/users`


## 请求方式

> GET

## 请求示例

获取所有绑定`group_id`为 1 的人员的`user_id`。

> `/v1/group/id/1/users`

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