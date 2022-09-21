# Query user information

Query user information.

## Request address

> `/v1/user/id/{id}`

## Request method

> GET


## Request example

get a user infomation which `user_id` is 3

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