# 固件升级

## 请求路径

> `/v1/device/upgrade`

## 请求方式

> POST

- 请求体: `multipart/form-data`

| 字段     | 类型 | 必填 | 字段释义                                                     |
| -------- | ---- | ---- | ------------------------------------------------------------ |
| firmware | File | Y    | 固件数据,固件不可大于512MB,且设备剩余空间不应小于600MB<br>对应产品的OTA升级包 (如：SensePassS7_V1.0.5_20220801_update.tgz) |



### 返回示例

```json
{
    "data": null,
    "code": 200,
    "msg": "OK"
}
```