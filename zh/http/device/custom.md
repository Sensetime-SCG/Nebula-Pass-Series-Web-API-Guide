# 设备自定义配置

## 提交配置

提交并应用新的自定义参数

### 请求路径

> `​/v1​/device​/custom`

### 请求方式

> POST

- 请求体: `application/json`

| 字段                    | 类型    | 必填 | 字段释义                    |
| ----------------------- | ------- | ---- | --------------------------- |
| welcome_tip             | String  | N    | 主欢迎语（视频流界面）      |
| verify_success_tip      | String  | N    | 提示语（验证成功）          |
| verify_fault_tip        | String  | N    | 提示语（验证失败）          |
| unauthorized_user_tip   | String  | N    | 重点人名单提示语            |
| show_custom_logo        | Boolean | N    | 是否展示logo                |
| custom_picture_for_logo | String  | N    | 自定义logo图片(base64编码)  |
| custom_picture_for_idle | String  | N    | 自定义待机图片(base64编码)  |
| voice_broadcast         | Boolean | N    | 语音播报，false：关true：开 |

### 请求示例:

> `​/v1​/device​/custom`

```json
{
    "welcome_tip": "你好",
    "verify_success_tip": "",
    "verify_fault_tip": "",
    "unauthorized_user_tip": "",
    "show_custom_logo": true,
    "custom_picture_for_logo": "",
    "custom_picture_for_idle": "",
    "voice_broadcast": true
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

获取设备自定义参数。

### 请求路径

> `​/v1​/device​/custom`

### 请求方式

> GET

### 请求示例

> `​/v1​/device​/custom`

### 返回示例

```json
{
    "data": {
        "welcome_tip": "你好",
        "verify_success_tip": "",
        "verify_fault_tip": "",
        "unauthorized_user_tip": "",
        "show_custom_logo": true,
        "custom_picture_for_logo": "",
        "custom_picture_for_idle": "",
        "voice_broadcast": true
    },
    "code": 200,
    "msg": "OK"
}
```

