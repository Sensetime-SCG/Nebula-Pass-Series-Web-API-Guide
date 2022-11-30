# Web服务证书配置

Can upload public certificate and private key, or get the current public certificate.

## Upload Certificate

### Request address

> `/v1/auth/certificate`

### Request method

> POST


### Response example

```json
{
    "data": null,
    "code": 200,
    "msg": "OK"
}
```

- Request Type : `multipart/form-data`

| Parameter name  | Type | Required | Description                    |
| ---- | ---- | ---- | -------- |
| crt  | File | Y    | public certificate     |
| key  | File | Y    | private key     |

## Get Certificate

### Request address

> `/v1/auth/certificate`

### Request method

> GET 

### Response example

```json
{
    "data": {
        "crt": "-----BEGIN CERTIFICATE-----\nMIIDnDCCAoSgAwIBAgIUfxQiqTnx5fvKoYXB94I4Xgudud8wDQYJKoZIhvcNAQEL\nBQAweDELMAkGA1UEBhMCWFgxDDAKBgNVBAgMA04vQTEMMAoGA1UEBwwDTi9BMSAw\nHgYDVQQKDBdTZWxmLXNpZ25lZCBjZXJ0aWZpY2F0ZTErMCkGA1UEAwwiMTIwLjAu\nMC4xOiBTZWxmLXNpZ25lZCBjZXJ0aWZpY2F0ZTAeFw0yMjExMzAxNjUyNDRaFw0y\nMzExMzAxNjUyNDRaMHgxCzAJBgNVBAYTAlhYMQwwCgYDVQQIDANOL0ExDDAKBgNV\nBAcMA04vQTEgMB4GA1UECgwXU2VsZi1zaWduZWQgY2VydGlmaWNhdGUxKzApBgNV\nBAMMIjEyMC4wLjAuMTogU2VsZi1zaWduZWQgY2VydGlmaWNhdGUwggEiMA0GCSqG\nSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDIsaCt8EtnICPUVSu/0/Pp6/5apsjIttp+\nGReHBa9Pmc8f6ib/cEe460eK+6Vvqmif8tu6SoOnRw3CRWhUkH9i+5x2GsJAK+zH\njIWmE777sdCoNNUOGoVqfc7x3FZxpcIOVkiNB38qYz79so7NoYCk2Nv/71vTO3aR\nyVD/pd7NMN2QiNcZtX4Hz2Ci08J/Dkj1H4+S1FzglPM6fSZ57u1ZNAMHlF2b/lxO\n8vPnKBzS9IIm2tlRmApQTjcDN0Tk2qyQoEUILupnSRlwZnxvvYYkox9sFi9GG5FH\nwddEyV0QTEGHhBYZw1L7xsnEKYmWkFtLryqNeqi7rgbJqQKQDeY7AgMBAAGjHjAc\nMBoGA1UdEQQTMBGCCWxvY2FsaG9zdIcEfwAAATANBgkqhkiG9w0BAQsFAAOCAQEA\no12hG+LNEqD4WYzuv5gtVQxlSx6iuU6AjZnivyFUTN2tN7BrRhl2p14QVt4rYTs2\npbQ9fSOwnjsUKTTlyW6CUIrTBfUnDploqNiuNrtDIMTdU+Ekh18EC77sfFX5tGNX\n/WfW+OvOofUScbYsiuTKo15EwvV16g0GuSazRiH9DA/Avd4kv+yp8swn8oRYxIuR\nUwpD2pSzfHQB1OR4zXfZq0RMrnAeXwrG7odVIJMVOwsYQIJE8bPJphQt9KuyTZ7q\nyl6o7VNgROCsd4Wk1swTKzNOKde+z9+qvV4EcRcihxqaeEoSkjVNs2eOxOIIO5YT\ny7dpDXo/oPYIRU2fdQ27zQ==\n-----END CERTIFICATE-----\n"
    },
    "code": 200,
    "msg": "OK"
}
```