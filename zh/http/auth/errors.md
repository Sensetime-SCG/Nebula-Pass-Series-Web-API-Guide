# 获取错误参照码

当前接口所有已记录的错误参照码

## 请求路径

> `/v1/auth/errors`

## 请求方式

> GET

## 请求参数

> 无

## 返回示例

```json
{
    "data": [
        {
            "code": 0,
            "msg": "Not define target code error message,please contact developer"
        },
        {
            "code": 200,
            "msg": "OK"
        },
        {
            "code": 401,
            "msg": "Unauthorized"
        },
        {
            "code": 404,
            "msg": "Not Found"
        },
        {
            "code": 500,
            "msg": "Internal Server Error"
        },
        {
            "code": 1000,
            "msg": "Account Not Exist"
        },
        {
            "code": 1001,
            "msg": "Password Wrong"
        }
    ],
    "code": 200,
    "msg": "OK"
}
```