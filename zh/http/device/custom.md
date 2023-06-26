# 设备自定义参数
客制化信息，如自定义提示语，logo，待机图等。

## 提交配置

提交并应用新的自定义参数

### 请求路径

> `​/v1​/device​/custom`

### 请求方式

> POST

- 请求体: `application/json`

| 字段                    | 类型    | 必填 | 字段释义                           |
| ----------------------- | ------- | ---- | ---------------------------------- |
| welcome_tip             | String  | N    | 主欢迎语（视频流界面）最大64字节   |
| verify_success_tip      | String  | N    | 提示语（验证成功）最大64字节       |
| verify_fault_tip        | String  | N    | 提示语（验证失败）最大64字节       |
| unauthorized_user_tip   | String  | N    | 重点人名单提示语 最大64字节        |
| show_custom_logo        | Int | N    |  0:展示默认logo，1：展示自定义logo，2：关闭 ；默认 ：2 |
| custom_picture_for_logo | String  | N    | 自定义logo图片(base64编码) 最大4MB |
| custom_screensavers | Object  | N    | 自定义待机屏保,仅支持JPG格式</br>默认使用系统待机屏保，</br>有自定义待机屏保，则使用自定义待机屏保图片|
| - interval | int  | N    | 轮播间隔，单位秒</br>1～255s设置，默认多张轮播时间间隔10s |
| - screensaver_list | Object  | N    | 屏保图片列表，最大5条 |
| --- picture_id | int  | N    | 图片索引值 1~5 。</br>根据图片索引可进行图片数据的增加，修改，删除。 |
| --- picture_data | String  | N    | 自定义待机图片(base64编码) 最大4MB |
| voice_broadcast         | Boolean | N    | 语音播报，false：关true：开        |

### 请求示例:

> `​/v1​/device​/custom`

```json
{
{
    "welcome_tip": "",
    "verify_success_tip": "",
    "verify_fault_tip": "XXXXXX",
    "unauthorized_user_tip": "",
    "show_custom_logo": 2,
    "custom_picture_for_logo": "",
    "custom_screensavers": {
        "interval": 10,
        "screensaver_list": [
            {
                "picture_id": 1,
                "picture_data": ""
            },
            {
                "picture_id": 2,
                "picture_data": ""
            }
        ]
    },
    "voice_broadcast": true
}
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
        "welcome_tip": "",
        "verify_success_tip": "",
        "verify_fault_tip": "",
        "unauthorized_user_tip": "",
        "show_custom_logo": 2,
        "custom_picture_for_logo": "",
        "custom_screensavers": {
            "interval": 10,
            "screensaver_list": []
        },
        "voice_broadcast": true
    },
    "code": 200,
    "msg": "OK"
}
```

