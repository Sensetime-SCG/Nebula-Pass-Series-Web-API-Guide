# 批量新建/修改人员

批量新建/修改人员,必填字段为`name`;`type`不填默认为**1(员工)**;`avatar`为**base64**后的图片数据,要求原图像为JPG或PNG格式；当同时填入`avatar`和`feature`字段时，`feature`字段值作为入库特征值，而`avatar`仅做为展示头像。

该接口同时支持创建和更新人员信息，如user_id不存在则创建人员信息，如user_id存在则更新人员信息.

## 请求路径

> `/v2/user`

## 请求方式

> POST

- 请求体: `application/json`

| 字段      | 类型         | 必填 | 字段释义     |
| --------- | ------------ | ---- | ------------ |
| user_list | Object array | N    | 人员信息列表 |



人员信息字段：

| 字段             | 类型      | 必填 | 字段释义                                                     |
| ---------------- | --------- | ---- | ------------------------------------------------------------ |
| user_id          | String  | Y    | 由提交端设置的唯一标识,不可重复, 长度上限128字节  |
| name             | String    | Y    | 人员名称,长度须大于0小于等于128                              |
| type             | Int       | N    | 人员类型,取值 1：员工 2：访客 3: 黑名单; 默认1,创建后不可修改 |
| avatar           | String    | N    | 人员头像,要求base64编码,上限10MB;存在feature时,该字段可不填  |
| feature          | String    | N    | 人员特征值,上限10KB,存在avatar时,该字段可不填,avatar与feature同时有值优先feature |
| ic_number        | String    | N    | IC卡号,上限128字节                                           |
| id_number        | String    | N    | 身份证号,上限128字节                                         |
| job_number       | String    | N    | 工号,上限128字节                                             |
| pin       | String    | N    | pin code,上限128字节                                             |
| guest_time_start | Int       | N    | 访客开始时间，毫秒级Unix时间戳                               |
| guest_time_end   | Int       | N    | 访客结束时间，毫秒级Unix时间戳                               |
| groups           | String array | N    | 绑定人员组的列表, 绑定的组类型不可互斥                       |
| is_admin         | boolean   | N    | 是否启用管理员权限，用于设备管理界面的刷脸认证,默认false     |
| remark           | String    | N    | 备注,上限256字节                                             |
| create_at | Int | N | 数据创建时间，服务端下发,请勿填写 |
| update_at | Int | N | 数据修改时间，服务端下发,请勿填写 |

## 请求示例:

添加两个人员，`user_id`设置为 `3`，`name`设置为*张三*，`type`设置为 1(员工组),且绑定通行组的*1*和*2*。`user_id`设置为 4，`name`设置为*李四*，`type`设置为 1(员工组),且绑定通行组的3和*4*。

> `/v2/user`

```json
{
    "user_list": [
        {
            "user_id": "3",
            "name": "张三",
            "type": 1,
            "avatar": "/9j/4AAQSkZJRgABAQAAAQABAA",
            "feature": "EqQAAAAAAAAMBAAAgYAAPIGAAL6ZmBg+gY",
            "ic_number": "1234",
            "id_number": "",
            "job_number": "",
            "pin": "",
            "groups": [
                "1","2"
            ],
            "is_admin": false,
            "remark": ""
        },
        {
            "user_id": "4",
            "name": "李四",
            "type": 1,
            "avatar": "/9j/4AAQSkZJRgABAQAAAQABAAD/",
            "feature": "",
            "ic_number": "1234",
            "id_number": "",
            "job_number": "2338",
            "pin": "",
            "groups": [
                "3",
                "4"
            ],
            "is_admin": true,
            "remark": ""
        }
    ]
}
}
```

## 返回示例

```json
{
    "data": {
        "errors": []
    },
    "code": 200,
    "msg": "OK"
}
```