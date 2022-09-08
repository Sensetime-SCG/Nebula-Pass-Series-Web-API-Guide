
# HTTP API调用规则

HTTP API接口只有在设备使用**单机模式**时才能使用全部功能。

## 接口风格及数据类型说明

Web服务接口采用HTTP Restful风格，具体入口地址形式为`https://HOST:PORT/`，其中HOST为设备IP，PORT 当前默认为**8000**

请求体和返回体数据格式（如不作特殊说明，请求和返回参数采用以下格式；特殊接口，将做额外的说明）: `Content-type: application/json`



## 请求认证说明

访问业务接口时，需要将认证参数放入 Header 中。目前支持 **JWT** 与 **Basic Auth** 两种认证方式，推荐使用 **JWT** 认证.

### JWT 认证

使用**JSON Web Token**[<sup>RFC 7519</sup>](https://datatracker.ietf.org/doc/html/rfc7519)，须先请求 `/v1/auth/login` 接口获取认证，若账户与密码认证通过则可获取到 *token* ，在后续的业务请求将其放入 Header 的 *Authorization* 字段，格式为 `Bearer token` ，即类似以下格式：

>  Authorization: Bearer xxx.xxx.xxx

### Basic Authentication

为方便命令行快速调试，亦可使用**Basic Authentication**[<sup>RFC 7617</sup>](https://datatracker.ietf.org/doc/html/rfc7617)认证方式，但不推荐业务使用该认证，后续该方式默认将置为未启用状态。



## 响应说明

所有响应均包含以下3部分（接口具体响应参数，均为`data`字段的值，且字段内容视对应接口而定，亦可为`null`）：

| **参数名称** | **类型** | **是否必须** | **说明**                 |
|--------------|----------|--------------|--------------------------|
| code         | int      | 是           | 响应码，正常为200        |
| msg          | string   | 是           | 详细描述，正常为OK；     |
| data         | object   | 否           | 响应消息主体，为json格式 |

成功返回示例：

``` json
{  
	"code": 200,  
	"msg": "OK",  
	"data": null 
} 
```



## 安全机制

-   设备端Web服务强制使用 HTTPS TLS/1.3加密，保证每次请求数据不会在传输过错中被窃听与篡改。
-   业务API请求需要把相关认证参数放入HTTP的 Header 中。
