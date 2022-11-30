# 更新人员信息

更新人员信息，其中`user_id`字段值和`type`字段值不可修改。

## 请求路径

> `/v1/user/id/{id}`

## 请求方式

> PUT

- 请求体: `application/json`

| 字段             | 类型      | 必填 | 字段释义                                                     |
| ---------------- | --------- | ---- | ------------------------------------------------------------ |
| name             | String    | Y    | 人员名称,内容长度1~128字节，不可重                           |
| avatar           | String    | N    | 人员头像,要求base64编码,上限10MB;存在feature时,该字段可不填  |
| feature          | String    | N    | 人员特征值,上限10KB,存在avatar时,该字段可不填,avatar与feature同时有值优先feature |
| ic_number        | String    | N    | IC卡号,上限128字节                                           |
| id_number        | String    | N    | 身份证号,上限128字节                                         |
| job_number       | String    | N    | 工号,上限128字节                                             |
| pin       | String    | N    | pin code,上限128字节                                             |
| guest_time_start | Int       | N    | 访客开始时间，毫秒级Unix时间戳                               |
| guest_time_end   | Int       | N    | 访客结束时间，毫秒级Unix时间戳                               |
| groups           | Int array | N    | 绑定人员组的列表, 绑定的组类型不可互斥                       |
| is_admin         | boolean   | N    | 是否启用管理员权限，用于设备管理界面的刷脸认证,默认false     |
| remark           | String    | N    | 备注,上限256字节                                             |

## 请求示例:

更新`user_id`为*3*的人员信息。

> `/v1/user/id/3`

```json
{
  "name": "张三",
  "avatar": "/9j/2wCEAAoHBwgHBgoICAgLCgoLDhgQDg0NDh0VFhEYIx8lJCIfIiEmKzcvJik0KSEiMEExNDk7Pj4",
  "groups": [1],
  "is_admin":true
}
```

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
        "pin":"",
        "groups": [1],
        "is_admin":true,
        "remark":"",
        "create_at": 1660222970940,
        "update_at": 1660222970940
  },
  "code": 200,
  "msg": "OK"
}
```