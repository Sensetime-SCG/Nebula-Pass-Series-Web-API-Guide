# Access Parameters

##  Set device access parameters

Get device access Parameters.

### Request address

> `​/v1​/device​/access`


### Request method

> POST

- Body Type: `application/json`


### Request parameters

| Parameter name          | Type    | Description                                                  | Remark     |
| ----------------------- | ------- | ------------------------------------------------------------ | ---------- |
| open_door_type          | Int     | Door opening mode, 0: Local relay, 1: Network relay, 2: Wiegand port 26(24) 3: Wiegand port 26(8+16), 4: Wiegand port 32, 5: Wiegand port 34, 6: Local relay + Wiegand port 34 |            |
| keep_door_open_duration | Int     | The duration of keeping the door open, that is, the time interval from issuing the door opening command to issuing the door closing command (unit: s) Value range: [1, 30], default 6s |            |
| gpio_a                  | Int     | GPIO A-output port, 1-None, 2-Doorbell, 3-Alarm              |            |
| gpio_b                  | Int     | GPIO B-input port, 1-None, 2-Door sensor, 3-Exit button, 4-Fire signal |            |
| gpio_c                  | Int     | GPIO C-input port, 1-None, 2-Door sensor, 3-Exit button, 4-Fire signal |            |
| wigan_input             | Int     | Wiegand input port, 1-None, 2: Wiegand 26 (8+16bit ID); 3: Wiegand 26 (24bit ID); 4: Wiegand 32; 5: Wiegand 34; |            |
| tamper                  | Boolean | Device tamper alarm switch, false: off, true: on             |            |
| force_open              | Boolean | Forced door open alarm switch                                |            |
| network_relay_address   | String  | Network delay IP address                                     |            |
| door_sensor_timeout     | Int     | Door sensor timeout duration (unit: s)                       | Default：3 |

Request example

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
### Response example

```json
{
    "data": null,
    "code": 200,
    "msg": "OK"
}
```

---

## Get device access parameters

Get device access control configuration.

### Request address

> `​/v1​/device​/access`

### Request method

> GET

### Response example

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



