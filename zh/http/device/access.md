# 设备门禁参数
设备门禁配置，可配置开门方式，GPIO口（两进一出），告警开关，门磁状态等。
## 提交配置

提交并应用新的门禁参数。

### 请求路径

> `​/v1​/device​/access`

### 请求方式

> POST

- 请求体: `application/json`

| 字段                    | 类型    | 必填 | 字段释义                                                     |
| ----------------------- | ------- | ---- | ------------------------------------------------------------ |
| open_door_type          | Int     | Y    | 开门方式:<br/>0:本地继电器 <br/>1:网络继电器 <br/>2:韦根输出 <br/>默认 0 |
| keep_door_open_duration | Int     | Y    | 保持开门状态的时长，即从发出开门命令到发出关门命令的时间间隔（单位：秒）<br/>取值范围：【1，30】<br/>默认6 |
| gpio_a                  | Int     | N    | GPIO A-输出口，1:无，2:门铃，3:报警器                        |
| gpio_b                  | Int     | N    | GPIO B-输入口，1:无，2:门磁，3:出门按钮，4:消防信号          |
| gpio_c                  | Int     | N    | GPIO C-输入口，1:无，2:门磁，3:出门按钮，4:消防信号          |
| wiegand_settings                  | object | N    | 韦根通讯接口参数                      |
| --mode             | Int     | N    | 使用模式: <br/>0:无 <br/>1:韦根输入<br/>2:韦根输出<br/>默认 0 |
| --type             | Int     | N    | 韦根格式: <br/>0:韦根26 (24bit ID) <br/>1:韦根26(8+16bit ID)<br/>2:韦根32<br/>3:韦根34<br/>默认 0 |
| --card_number             | String     | N    | 默认开号: 12345678 |
| --pulse_width             | Int     | N    | 脉冲宽度: 取值范围：【50，1000】<br/>默认 180 us ;韦根输出有效 |
| --pulse_cycle             | Int     | N    | 脉冲周期: 取值范围：【500，10000】<br/>默认 2000 uS ;韦根输出有效 |
| --reverse_card_number             | boolean     | N    | 大小端返序: 默认关 |
| tamper                  | Boolean | Y    | 设备防拆报警开关，false：关，true：开                        |
| force_open              | Boolean | Y    | 强制开门告警开关，false：关，true：开                      |
| network_relay_address   | String  | Y    | 网络继电器ip地址                                             |
| door_sensor_timeout     | Int     | Y    | 门磁超时时长(单位s)                                          |
| resign_interval | Int     | Y    | 重复识别间隔,相同User id再次能通行的间隔（单位：秒）<br/>取值范围：【0，1800】<br/>默认0 ,关闭该功能|
| rfid_settings     | object     | N    | 刷卡设置接口参数，屏下刷卡模块|
| --type     | Int     | N    | 刷卡格式: <br/>0:26 (24bit ID) <br/>1:26(8+16bit ID)<br/>2:32<br/>3:34<br/>4:35<br/>默认 0 |
| serial_port             | Int     | N    | 0-关，1-保留，2-保留 ，3-透传字段,；默认 0                   |
| serial_port_baudrate    | Int     | N    | 波特率，如：115200                                           |

### 请求示例:

> `​/v1​/device​/access`

```json
{
    "open_door_type": 0,
    "keep_door_open_duration": 6,
    "resign_interval": 0,
    "gpio_a": 2,
    "gpio_b": 1,
    "gpio_c": 1,
    "wiegand_settings": {
        "mode": 0,
        "type": 0,
        "card_number": "12345678",
        "pulse_width": 180,
        "pulse_cycle": 2000,
        "reverse_card_number": 0
    },
    "rfid_settings": {
        "type": 0
    },
    "tamper": true,
    "force_open": true,
    "network_relay_address": "127.0.0.1",
    "door_sensor_timeout": 3,
    "serial_port": 0,
    "serial_port_baudrate": 115200
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
        "open_door_type": 2,
        "keep_door_open_duration": 6,
        "resign_interval": 0,
        "gpio_a": 2,
        "gpio_b": 1,
        "gpio_c": 1,
        "wiegand_settings": {
            "mode": 2,
            "type": 0,
            "card_number": "12345678",
            "pulse_width": 180,
            "pulse_cycle": 2000,
            "reverse_card_number": 0
        },
        "rfid_settings": {
            "type": 0
        },
        "tamper": true,
        "force_open": true,
        "network_relay_address": "127.0.0.1",
        "door_sensor_timeout": 3,
        "serial_port": 3,
        "serial_port_baudrate": 115200
    },
    "code": 200,
    "msg": "OK"
}
```

