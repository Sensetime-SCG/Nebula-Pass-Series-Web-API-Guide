# Custom Parameters


## Set device custom parameters

Set device custom parameters

### Request address

> `​/v1​/device​/custom`

### Request method

> POST

- Body Type: `application/json`

### Request parameters

| Parameter name          | Type    | Description                                                  | Remark |
| ----------------------- | ------- | ------------------------------------------------------------ | ------ |
| welcome_tip             | String  | Main welcome (video streaming interface), Upper limit 64 bytes |        |
| verify_success_tip      | String  | Prompt (verification successful), Upper limit 64 bytes       |        |
| verify_fault_tip        | String  | Prompt (verification failed), Upper limit 64 bytes           |        |
| unauthorized_user_tip   | String  | Unauthorized user tip, Upper limit 64 bytes                  |        |
| show_custom_logo        | Boolean | Whether to show logo                                         |        |
| custom_picture_for_logo | String  | Custom logo image (base64 encoding), Upper limit 4MB         |        |
| custom_picture_for_idle | String  | Custom standby image (base64 encoding) , Upper limit 4MB     |        |
| voice_broadcast         | Boolean | Voice broadcast, false: off true: on                         |        |

Request example

```json
{
        "welcome_tip": "welcome",
        "verify_success_tip": "",
        "verify_fault_tip": "",
        "unauthorized_user_tip": "",
        "show_custom_logo": true,
        "custom_picture_for_logo": "",
        "custom_picture_for_idle": "",
        "voice_broadcast": true
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

## Get device custom parameters

Get device custom parameters.

### Request address

> `​/v1​/device​/custom`

### Request method

> GET

### Response example

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

