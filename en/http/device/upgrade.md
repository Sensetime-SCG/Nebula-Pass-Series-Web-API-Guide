# Upgrade

Upload the file to the device and upgrade.

## Request address

https://HOST:PORT/v1/device/upgrade

## Request method

POST

## Request parameters

The request body adopts the form style, and the Content-Type parameter of the request header is set as follows:

Content-Type: multipart/form-data

In the request body, submit the firmware data:

firmware: firmware data;

| Parameter name | Type             | Required | Description                                                  |
| -------------- | ---------------- | -------- | ------------------------------------------------------------ |
| firmware       | firmware（file） | Y        | OTA upgrade package of the corresponding product (eg: SensePassS7_V1.0.5_20220801_update.tgz) |

![image-20220810112950439](C:\Users\linpeicai\AppData\Roaming\Typora\typora-user-images\image-20220810112950439.png)

## Response parameters

| Parameter name | Type | Description |
| -------------- | ---- | ----------- |
| None           | None | None        |

```json
{
    "data": null,
    "code": 200,
    "msg": "OK"
}
```