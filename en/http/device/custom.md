# Custom Parameters

## Get device custom parameters

Get device custom parameters.

### Request address

https://HOST:PORT/v1/device/custom

### Request method

GET

### Request parameters

| Parameter name | Type | Required | Description |
| -------------- | ---- | -------- | ----------- |
| None           | None | None     | None        |

### Response parameters

| Parameter name          | Type    | Description                              | Remark |
| ----------------------- | ------- | ---------------------------------------- | ------ |
| welcome_tip             | String  | Main welcome (video streaming interface) |        |
| verify_success_tip      | String  | Prompt (verification successful)         |        |
| verify_fault_tip        | String  | Prompt (verification failed)             |        |
| unauthorized_user_tip   | String  | Unauthorized user tip                    |        |
| show_custom_logo        | Boolean | Whether to show logo                     |        |
| custom_picture_for_logo | String  | Custom logo image (base64 encoding)      |        |
| custom_picture_for_idle | String  | Custom standby image (base64 encoding)   |        |
| voice_broadcast         | Boolean | Voice broadcast, false: off true: on     |        |

Response parameters

```
{

  "code": 200,

  "msg": "OK"，
  "data": {

​    "welcome_tip": "",

​    "verify_success_tip": "",

​    "verify_fault_tip": "",

​    "unauthorized_user_tip": "",

​    "show_custom_logo": **true**,

​    "custom_picture_for_logo": "",

​    "custom_picture_for_idle": "",

​    "voice_broadcast": **true**

  }

}
```



## Set device custom parameters

Set device custom parameters

### Request address

https://HOST:PORT/v1/device/custom

### Request method

POST

### Request parameters

| Parameter name          | Type    | Description                              | Remark |
| ----------------------- | ------- | ---------------------------------------- | ------ |
| welcome_tip             | String  | Main welcome (video streaming interface) |        |
| verify_success_tip      | String  | Prompt (verification successful)         |        |
| verify_fault_tip        | String  | Prompt (verification failed)             |        |
| unauthorized_user_tip   | String  | Unauthorized user tip                    |        |
| show_custom_logo        | Boolean | Whether to show logo                     |        |
| custom_picture_for_logo | String  | Custom logo image (base64 encoding)      |        |
| custom_picture_for_idle | String  | Custom standby image (base64 encoding)   |        |
| voice_broadcast         | Boolean | Voice broadcast, false: off true: on     |        |

Request example

```
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

### Response parameters

| Parameter name | Type | Required | Description |
| -------------- | ---- | -------- | ----------- |
| None           | None | None     | None        |

