# Upgrade

Upload the file to the device and upgrade.

## Request address

> `/v1/device/upgrade`

## Request method

> POST

- Body Type: `multipart/form-data`

## Request parameters

The request body adopts the form style, and the Content-Type parameter of the request header is set as follows:

Content-Type: multipart/form-data

In the request body, submit the firmware data:

firmware: firmware data;

| Parameter name | Type             | Required | Description                                                  |
| -------------- | ---------------- | -------- | ------------------------------------------------------------ |
| firmware       | File | Y        | OTA upgrade package of the corresponding product,the file size should be less than 600MB |


```json
{
    "data": null,
    "code": 200,
    "msg": "OK"
}
```