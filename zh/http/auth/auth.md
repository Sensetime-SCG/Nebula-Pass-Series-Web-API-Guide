# 认证接口

## 获取Token

使用 `JWT` 认证方式请求业务接口，需先通过此接口获取 token 值。

- 请求路径

> `/v1/auth/login`

- 请求方式

> POST

- 请求体: `application/json`

| 字段      | 类型   | 必填 | 字段释义                                                    |
| --------- | ------ | ---- | ----------------------------------------------------------- |
| username  | string | Y    | 后台管理账号                                                      |
| password  | string | Y    | 密码                                                        |
| validTime | int    | N    | token有效期,单位分钟, 范围： 大于 0 小于等于 1440，默认5 |


- 请求示例:

```json
{
  "username": "user",
  "password": "pwd",
  "validTime": 5
}
```

- 返回示例

```json
{
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXUyJ9.eyJleHAiOjE2NjAyMTkwMDcsImlhdCI6MTY2MDIxODcwNywiaXNzIjoiU2Vuc2VUaW1lIiwidXNlcklkIjoiYWRtaW4ifQ.-sRDf6dA6MXW72Ofb-2zGq9NJr0FXoszwWWueWssN70"
  },
  "code": 200,
  "msg": "OK"
}
```