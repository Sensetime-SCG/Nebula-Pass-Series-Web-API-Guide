# 远程开门

调用接口，可以进行实现远程开门等应用。


## 请求路径

> `​/v1​/device​/door`

## 请求方式

> POST

- 请求体: `application/json`

| 字段        | 类型   | 必填 | 字段释义                                          |
|-------------|--------|------|-----------------------------------------------|
| open_mode   | Int    | Y    | mode 0:开门后正常延时关闭； 1：常开； 2：常关 |
| card_number | String | N    | 开门卡号                                      |

## 请求示例

> `​/v1​/device​/door`

```json
{
    "open_mode":0,
    "card_number":""
}
```

## 返回示例

```json
{
    "data": null,
    "code": 200,
    "msg": "OK"
}
```