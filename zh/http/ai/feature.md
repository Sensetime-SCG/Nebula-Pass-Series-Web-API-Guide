# 获取图片中人脸的特征值

获取图片中人脸的特征值
注: 不可提交存在多人脸的图像,否则大概率返回失败

## 请求路径

> `/v1/ai/feature`

## 请求方式

> POST

- 请求体: `multipart/form-data`

| 字段  | 类型 | 必填 | 字段释义                    |
| ----- | ---- | ---- | --------------------------- |
| image | File | Y    | JPEG 图像,文件不可大于 4 MB |

### 响应参数

```json
{
    "data": "2KQAAAAAAAAMBAAAsMuIvQMvq7z/bG89cpssdcfAtj3L8V+9tDUAPX3P9j3efhS9tpMMPbsmZz0Qa2c9Rh8ZvTmLmL1Cs/e94uLovXXQe31uCq99LlUkvSX6aj2EcOY9S7gWPXwkFz55vcO7HjQRO/vbYz1zeBE9J4knvb8TML1flUK9TOccPnT5OD2BOxg9i2dwvSUAjj2zJ2s+51KDPM16+bxXSJ49cXCfPAjzNT1XF+68/I27vJRsDzz1lrG8Y60YvYNulzwU2wE+o4f/O4xEVT1eEKI902+0vHPOKz3frZo9exvQPTMZL7wdgrk9wqEXvoRw5jzMzkQ8U4ZiPThW77xqnn893ffJvCwiJTw4XJK9JoYDPpuOJjsyY949ozFlvCtFwL1JVGc9ooWwvAmljbwZamO9r0S+Pcyjtzx/2+E9NqbBPYm3wr3hMru8y/eCvZSXHLsvXRa9sPaVvVCkCj4oYpM96VzEPQY95T065gC+XrhdvYyW9r38Yq68FQTlvJtddj3MzkQ8y/cCvP0Uhr19Ts+8/2xvPRFIzDxd4Rs9YvtAvWbkEL67+9k8PRp6vVaWxr0rnC++UPnPvdsYFr38DBQ6GfICPll1ej0KfM88i22TPXJH4bxdCrg9SFaRPd3NET4nXho9dt4Pvf1k/TrDpDu99uxLPJFgpD1qoKm9j9eaPbQE0DxL36q9BxZRPeq4AT0+zFE9flZBPWv6PLwnXPC956gdPG41rjx7TIC8gApovdgIMr31wb48iQlkvba+Gb1xany9qlP8PJoyaT3ddqK8UlmGPcSBID2QMR49/eNVvA2Iur1MZMs8/RQGPWL7QL1PSSK8Qdw1vC3OWTtJ/sy5FIO9veEyOzznonq9SFIYve71QbyxH3k7e0yAPKcerj2Q24M90uhpvYs847w6Ebm6wUavvaj1771V6pE75RlhPbr5irz3yTA9asu2Pe0egLoxNNi8yRT7vEFbjjrTb7S9/Q5jvWTYpTwRoJC9sfqOvX1Oz7x6Pmu8np6KvLjGCz0/9169zU/sOvgjxL1wvse9dSy4PdxLlTz4phW9eOaBvZWZ673k7tM8+wZxPa/HDzxkWc08I80OPWJ0dr21tqc9zCaJPblyQD3ddqI8yD25vE+bwz2N9qy8WSWDPJlbJ72m6668BNtfPMNOIT3ErQK+l/2avPy4SLwjzQ69zwm2PL4LPjzGrvw7gF6zu3m9wzvxr4u8sMuIPWRZzTymbgA+CaWNPJ3sMr3fgo09uPEYvQSw0rsteL87oCckvYEO4b3URvY7LaPMPOGI1bqJCWQ9gF6zO0FbDj270My8Aq4DPRz9mL1se+S7LPcXvICJQLzof187NMXjObDyHLyGqQi6dSw4PQ=",
    "code": 200,
    "msg": "OK"
}
```