# 设备系统参数

## 提交配置


### 请求路径

> `​/v1​/device​/system`

### 请求方式

> POST

- 请求体: `application/json`

| 字段                          | 类型    | 必填 | 字段释义                                            |
| ----------------------------- | ------- | ---- | --------------------------------------------------- |
| language_type                 | Int     | N    | 多语言，1：简体中文2：英文，3,繁体中文              |
| sound_volume                  | Int     | N    | 系统音量，范围：0~100; 默认: 80                     |
| screen_brightness             | Int     | N    | 屏幕亮度，范围：0~100; 默认: 80                     |
| auto_reboot                   | Boolean | N    | 自动重启，false：关true：开; 默认: true             |
| reboot_time                   | String  | N    | 自动重启时间; 默认: "02:00:00"                      |
| standby_open                  | Boolean | N    | 是否开启待机，false:关闭,true:开启; 默认：true      |
| standby_touch_wakeup          | Boolean | N    | 待机触摸唤醒, false:关闭,true:开启; 默认：false     |
| wait_time                     | Int     | N    | 待机时间,单位：分钟,范围：1~10; 默认: 1             |
| sleep_time                    | Int     | N    | 休眠时间,单位：分钟,范围：3~30; 默认: 3             |
| touch_recognition             | Boolean | N    | 触摸识别开关，false:关闭，true:开启; 默认: false    |
| touch_recognition_return_time | Int     | N    | 触摸识别完成返回时间，单位：秒，范围：3~30；默认: 5 |
| touch_recognition_timeout     | Int     | N    | 触摸识别超时时间，单位：秒，范围：3~30; 默认: 5     |
| short_exposure                | Int     | N    | 防闪烁， 0:无;  50:50hz;  60:60hz; 默认：0          |

### 请求示例:

> `​/v1​/device​/system`

```json
{
    "language_type": 1,
    "sound_volume": 80,
    "screen_brightness": 80,
    "auto_reboot": true,
    "reboot_time": "02:00:00",
    "standby_open": true,
    "standby_touch_wakeup": false,
    "wait_time": 1,
    "sleep_time": 3,
    "touch_recognition": false,
    "touch_recognition_return_time": 5,
    "touch_recognition_timeout": 5,
    "short_exposure": 0
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

> `​/v1​/device​/system`

### 请求方式

> GET

### 请求示例

> `​/v1​/device​/system`

### 返回示例

```json
{
    "data": {
        "language_type": 1,
        "sound_volume": 80,
        "screen_brightness": 80,
        "auto_reboot": true,
        "reboot_time": "02:00:00",
        "standby_open": true,
        "standby_touch_wakeup": false,
        "wait_time": 1,
        "sleep_time": 3,
        "touch_recognition": false,
        "touch_recognition_return_time": 5,
        "touch_recognition_timeout": 5,
        "short_exposure": 0
    },
    "code": 200,
    "msg": "OK"
}
```

