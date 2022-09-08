# 查询用户的信息

根据指定的`user_id`获取该人员信息

## 请求路径

> `/v1/user/id/{id}`

## 请求方式

> GET


## 请求示例

获取`user_id`为*3*的人员信息。

> `/v1/user/id/3`

## 返回示例

```json
{
  "data": {
        "user_id":3,
        "name": "张三",
        "avatar": "/9j/2wCEAAoHBwgHBgoICAgLCgoLDhgQDg0NDh0VFhEYIx8lJCIfIiEmKzcvJik0KSEiMEExNDk7Pj4",
        "type": 1,
        "ic_number":"",
        "job_number":"",
        "id_number":"",
        "groups": [1,2],
        "is_admin":false,
        "remark":"",
        "create_at": 1660222970940,
        "update_at": 1660222970940
  },
  "code": 200,
  "msg": "OK"
}
```