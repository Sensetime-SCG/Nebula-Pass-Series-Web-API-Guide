# System Parameters


## Set device system parameters

Set device system parameters.

### Request address

> `​/v1​/device​/system`

### Request method

> POST

- Body Type: `application/json`

### Request parameters

| Parameter name       | Type    | Description                                                  |
| -------------------- | ------- | ------------------------------------------------------------ |
| language_type        | Int     | 1: Simplified Chinese 2：English，3：Traditional Chinese     |
| sound_volume         | Int     | System volume（0-100）                                       |
| screen_brightness    | Int     | Screen brightness（0-100）                                   |
| auto_reboot          | Boolean | Auto reboot switch, false: off true: on                      |
| reboot_time          | String  | Auto reboot time                                             |
| standby_open         | Boolean | Whether the standby is enabled, false-not enabled, true-enabled |
| standby_touch_wakeup | Boolean | Whether to enable standby touch wake-up, false-not enabled, true-enabled |
| wait_time            | Int     | Standby time (unit: minutes) value [1-10], default 1         |
| sleep_time           | Int     | Sleep time (unit: minutes) value [3-30], default 3           |
| touch_recognition    | Boolean | Touch recognition switch, false-not enabled, true-enabled    |
| return_time          | Int     | Touch recognition completion return time (s) Value [3-30], default 5 |
| timeout              | Int     | Touch recognition timeout time (s) Value [3-30], default 5   |
| short_exposure       | Int     | Anti-flicker, 0:None; 50:50hz; 60:60hz                       |

### Request example

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

### Response example

```json
{
    "data": null,
    "code": 200,
    "msg": "OK"
}
```

---


##  Get device system parameters

Get device system parameters.

### Request address

> `​/v1​/device​/system`

### Request method

> GET

### Response example

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
