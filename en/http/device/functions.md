# 设备功能参数配置

## 提交配置

### 请求路径

> `​/v1​/device​/functions`

### 请求方式

> POST

- 请求体: `application/json`

| 字段            | 类型    | 必填 | 字段释义                                                                                                              |
| --------------- | ------- | ---- | --------------------------------------------------------------------------------------------------------------------- |
| device_run_type | Int     | N    | 设备运行状态配置， 1：运行；2：停机                                                                                   |
| mode            | Int     | Y    | 核验模式: 0：刷脸 1：刷脸或刷卡 2：刷脸或刷卡或刷二维码 3：刷脸且刷卡 4：刷身份证 5：刷脸或刷身份证 6：刷脸且刷身份证 | 默认 0 |
| strong_hint     | Boolean | N    | 炫酷模式开关，false：关；true：开                                                                                     |
| avatar_status   | Int     | Y    | 展示头像 0：不展示头像 1：展示头像 2.展示个性化头像 ；默认 1                                                          |
| name_status     | Int     | Y    | 展示姓名： 0：不展示姓名 1：展示姓名 2：展示加密姓名 ； 默认 1                                                        |
| record          | Boolean | Y    | 事件记录存储开关，false：关；true：开                                                                                 |
| record_image    | Boolean | Y    | 事件记录图片存储开关，false：关；true：开                                                                             |
| alarm_record    | Boolean | Y    | 告警记录存储开关，false：关；true：开                                                                                 |
| auth_mode       | Int     | Y    | 认证类型：0：本地认证 1：本地认证+远程开门                                                                            |

### 请求示例:

> `​/v1​/device​/functions`

```json
{
    "device_run_type": 1,
    "mode": 0,
    "strong_hint": true,
    "avatar_status": 1,
    "name_status": 1,
    "record": true,
    "record_image": true,
    "alarm_record": true,
    "auth_mode: 0,
}
```
### 返回示例

```json
{
    "data": null,
    "code": 200,
    "msg": "OK"
}
```

---

## 获取配置

### 请求路径

> `​/v1​/device​/functions`

### 请求方式

> GET

### 请求示例

> `​/v1​/device​/functions`

### 返回示例

```json
{
    "data": {
        "device_run_type": 1,
        "mode": 0,
        "strong_hint": true,
        "avatar_status": 1,
        "name_status": 1,
        "record": true,
        "record_image": true,
        "alarm_record": true,
        "auth_mode": 0
    },
    "code": 200,
    "msg": "OK"
}
```

