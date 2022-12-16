# Search

Search the 'id' list of related objects according to the specified fields

## 请求路径

> `/v1/group/search`

## 请求方式

> POST

| 字段     | 类型   | 必填 | 字段释义                                                 |
| -------- | ------ | ---- | -------------------------------------------------------- |
| name  | String    | N    | 根据该字段搜索相关对象 |


## 请求示例

获取`name`起始为*A*的 id 列表。

> `/v1/group/search`

```json
{
    "name":"A"
}
```

## 返回示例

```json
{
    "data": {
        "items": [
            2,
            55,
            117
        ]
    },
    "code": 200,
    "msg": "OK"
}
```