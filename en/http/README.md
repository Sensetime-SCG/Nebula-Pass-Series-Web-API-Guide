
# HTTP API Calling Rules

## Instructions for Use

The full functionality of the API is only available when the device is in **stand-alone mode.**



## API Type Description

The API is called by HTTP Restful request. The specific entry address is as follows:

https://HOST:PORT/  （The port number is [8000] by default.）

Format of request and return parameters (if no special instructions are given, the request and return parameters are in the following formats; for special interfaces, additional instructions will be given):

Content-type: application/json



## Request Authentication Description

When accessing the business interface, you need to put the authentication parameters in the header. Currently, two authentication methods, JWT and Basic Auth, are supported. JWT authentication is recommended.

### JWT  Authentication

Request the **/v1/auth/login** interface. If the account and password authentication is passed, the token can be obtained. In subsequent business requests, it will be placed in the Authorization field of the Header in the format Bearer \<token\> , which is similar to the following format:

> Authorization: Bearer xxx.xxx.xxx

### Basic Auth Authentication

In order to facilitate the quick debugging of the command line, this authentication method can be used, that is, the username and password after Base64 are added to the Header and placed in the Authorization field, the format is Basic \<token\> , which is similar to the following format:

> Authorization: Basic xxxxxxxxxxx

Curl command quick debugging example:

curl -k -X GET -u username:password https://1.2.3.4:8000/v1/user/id/123



## Response Description

All responses contain the following three parts (the specific response parameters of the interface are all sub-fields under the data field, and the content of the specific fields in data depends on the corresponding interface and can be null):

| **Parameter name** | **Type** | **Required** | **Description**                       |
| ------------------ | -------- | ------------ | ------------------------------------- |
| code               | int      | Y            | Response code, normally 200           |
| msg                | string   | Y            | Detailed description, normally OK     |
| data               | object   | N            | Response message body, in json format |

Example of successful return:

```
{  
	"code": 200,  
	"msg": "OK",  
	"data": null 
} 
```



## Security Mechanism

-   The device-side web service is forced to use HTTPS TLS/1.3 encryption to ensure that each requested data is not eavesdropped and tampered with.
-   For business API requests, you need to put the relevant authentication parameters in the HTTP header.

