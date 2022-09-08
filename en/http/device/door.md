#  Open the door remotely

Open the door remotely.

## Request address

https://HOST:PORT/v1/device/door

## Request method

POST

## Request parameters

| Parameter name | Type   | Required | Description                                                  |
| -------------- | ------ | -------- | ------------------------------------------------------------ |
| open_mode      | Int    | Y        | mode 0: normal delay closing after opening the door; 1: normally open; 2: normally closed |
| card_number    | String | N        | Card number                                                  |

Request example

```
{
    "open_mode" : 0,
    "card_number" :""
}
```

##  Response parameters

| Parameter name | Type | Description |
| -------------- | ---- | ----------- |
| None           | None | None        |

Response example：

```json
{
    "data": null,
    "code": 200,
    "msg": "OK"
}
```