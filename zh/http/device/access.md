# 设备门禁配置

## 提交配置

提交并应用新的门禁参数。

### 请求路径

> `​/v1​/device​/access`

### 请求方式

> POST

- 请求体: `application/json`

| 字段                    | 类型    | 必填 | 字段释义                                                                                                                      |
| ----------------------- | ------- | ---- | ----------------------------------------------------------------------------------------------------------------------------- |
| open_door_type          | Int     | Y    | 开门方式,0:本地继电器,1:网络继电器,2：韦根接口26(24), 3:韦根接口26(8+16), 4:韦根接口32, 5:韦根接口34, 6:本地继电器+韦根接口34 |
| keep_door_open_duration | Int     | N    | 保持开门状态的时长，即从发出开门命令到发出关门命令的时间间隔（单位：s）取值范围：【1，30】，默认6s                            |
| gpio_a                  | Int     | N    | GPIO A-输出口，1-无，2-门铃，3-报警器                                                                                         |
| gpio_b                  | Int     | Y    | GPIO B-输入口，1-无，2-门磁，3-出门按钮，4-消防信号                                                                           |
| gpio_c                  | Int     | Y    | GPIO C-输入口，1-无，2-门磁，3-出门按钮，4-消防信号                                                                           |
| wigan_input             | Int     | Y    | 韦根输入口， 1-无，2：韦根26(8+16bit ID）；3：韦根26 （24bit ID）;4：韦根32；5：韦根34；                                      |
| tamper                  | Boolean | Y    | 设备防拆报警开关，false：关，true：开                                                                                         |
| force_open              | Boolean | Y    | 强制开门告警开关                                                                                                              |
| network_relay_address   | String  | Y    | 网络继电器ip地址                                                                                                              |
| door_sensor_timeout     | Int     | Y    | 门磁超时时长(单位s)                                                                                                           |

### 请求示例:

> `​/v1​/device​/access`

```json
{
    "open_door_type": 0,
    "keep_door_open_duration": 6,
    "gpio_a": 1,
    "gpio_b": 1,
    "gpio_c": 1,
    "wigan_input": 4,
    "tamper": true,
    "force_open": true,
    "network_relay_address": "127.0.0.1",
    "door_sensor_timeout": 3
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

获取设备门禁参数。

### 请求路径

> `​/v1​/device​/access`

### 请求方式

> GET

### 请求示例

> `​/v1​/device​/access`

### 返回示例

```json
{
    "data": {
        "open_door_type": 0,
        "keep_door_open_duration": 6,
        "gpio_a": 1,
        "gpio_b": 1,
        "gpio_c": 1,
        "wigan_input": 4,
        "tamper": true,
        "force_open": true,
        "network_relay_address": "127.0.0.1",
        "door_sensor_timeout": 3
    },
    "code": 200,
    "msg": "OK"
}
```

