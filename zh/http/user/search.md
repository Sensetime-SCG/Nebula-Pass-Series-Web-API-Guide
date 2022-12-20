# 查询人员

根据指定的字段搜索相关对象的`id`列表.

## 请求路径

> `/v1/user/search`

## 请求方式

> POST

| 字段       | 类型   | 必填 | 字段释义               |
| ---------- | ------ | ---- | ---------------------- |
| name       | String | N    | 根据该字段搜索相关对象,支持模糊匹配 |
| ic_number  | String | N    | 根据该字段搜索相关对象,仅支持全量匹配 |
| job_number | String | N    | 根据该字段搜索相关对象,仅支持全量匹配 |

> 注: 不支持`name`,`ic_number`,`job_number`同时填值搜索,若存在两者及以上的值,则按照此优先级取过滤条件 : `name` > `ic_number` > `job_number`

## 请求示例

获取`name`包含*A*的 id 列表。

> `/v1/user/search`

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