# Web服务证书配置

可以获取当前服务的公钥与上传自有证书的公钥和私钥，用以配置 Web 服务的 HTTPS 的证书加密通信数据，使得交互数据私密可靠。

## 提交证书配置

可信SSL证书需要自行去相关机构购买，如阿里云或腾讯云等云厂商购买，也可以直接向沃通等认证公司购买。

如果是自用或测试，可以通过该地址的脚本生成自签名证书:  [gen_ssl_key.sh](https://gist.github.com/idoop/f1f2e9725cd1934ec7eb6602f7b0bd61)

提交成功后，须重启设备新证书才会应用生效。

### 请求路径

> `/v1/auth/certificate`

### 请求方式

> POST


### 返回示例

```json
{
    "data": null,
    "code": 200,
    "msg": "OK"
}
```

- 请求体: `multipart/form-data`

| 字段 | 类型 | 必填 | 字段释义 |
| ---- | ---- | ---- | -------- |
| crt  | File | Y    | 公钥     |
| key  | File | Y    | 私钥     |

## 获取当前公钥

### 请求路径

> `/v1/auth/certificate`

### 请求方式

> GET 

### 返回示例

```json
{
    "data": {
        "crt": "-----BEGIN CERTIFICATE-----\nMIIDnDCCAoSgAwIBAgIUfxQiqTnx5fvKoYXB94I4Xgudud8wDQYJKoZIhvcNAQEL\nBQAweDELMAkGA1UEBhMCWFgxDDAKBgNVBAgMA04vQTEMMAoGA1UEBwwDTi9BMSAw\nHgYDVQQKDBdTZWxmLXNpZ25lZCBjZXJ0aWZpY2F0ZTErMCkGA1UEAwwiMTIwLjAu\nMC4xOiBTZWxmLXNpZ25lZCBjZXJ0aWZpY2F0ZTAeFw0yMjExMzAxNjUyNDRaFw0y\nMzExMzAxNjUyNDRaMHgxCzAJBgNVBAYTAlhYMQwwCgYDVQQIDANOL0ExDDAKBgNV\nBAcMA04vQTEgMB4GA1UECgwXU2VsZi1zaWduZWQgY2VydGlmaWNhdGUxKzApBgNV\nBAMMIjEyMC4wLjAuMTogU2VsZi1zaWduZWQgY2VydGlmaWNhdGUwggEiMA0GCSqG\nSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDIsaCt8EtnICPUVSu/0/Pp6/5apsjIttp+\nGReHBa9Pmc8f6ib/cEe460eK+6Vvqmif8tu6SoOnRw3CRWhUkH9i+5x2GsJAK+zH\njIWmE777sdCoNNUOGoVqfc7x3FZxpcIOVkiNB38qYz79so7NoYCk2Nv/71vTO3aR\nyVD/pd7NMN2QiNcZtX4Hz2Ci08J/Dkj1H4+S1FzglPM6fSZ57u1ZNAMHlF2b/lxO\n8vPnKBzS9IIm2tlRmApQTjcDN0Tk2qyQoEUILupnSRlwZnxvvYYkox9sFi9GG5FH\nwddEyV0QTEGHhBYZw1L7xsnEKYmWkFtLryqNeqi7rgbJqQKQDeY7AgMBAAGjHjAc\nMBoGA1UdEQQTMBGCCWxvY2FsaG9zdIcEfwAAATANBgkqhkiG9w0BAQsFAAOCAQEA\no12hG+LNEqD4WYzuv5gtVQxlSx6iuU6AjZnivyFUTN2tN7BrRhl2p14QVt4rYTs2\npbQ9fSOwnjsUKTTlyW6CUIrTBfUnDploqNiuNrtDIMTdU+Ekh18EC77sfFX5tGNX\n/WfW+OvOofUScbYsiuTKo15EwvV16g0GuSazRiH9DA/Avd4kv+yp8swn8oRYxIuR\nUwpD2pSzfHQB1OR4zXfZq0RMrnAeXwrG7odVIJMVOwsYQIJE8bPJphQt9KuyTZ7q\nyl6o7VNgROCsd4Wk1swTKzNOKde+z9+qvV4EcRcihxqaeEoSkjVNs2eOxOIIO5YT\ny7dpDXo/oPYIRU2fdQ27zQ==\n-----END CERTIFICATE-----\n"
    },
    "code": 200,
    "msg": "OK"
}
```
