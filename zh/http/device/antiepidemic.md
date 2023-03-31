# 防疫测温参数（停止维护）
防疫测温配置。(当前支持SenseNebula Pass S8测温防疫一体机)<br>
健康码接口实现文档请参考《08-商汤科技健康码接口协议-V1.8》
## 提交配置


### 请求路径

> `/v1/device/antiepidemic`

### 请求方式

> POST

- 请求体: `application/json`

| 字段           | 类型    | 是否必须 | 说明                                                         |
| -------------- | ------- | -------- | ------------------------------------------------------------ |
| temperature_detect     | bool   | Y        | 是否开启测温，默认关                                         |
| fever_temperature      | float  | Y        | 通行依据，体温小于多少度允许通行，默认37.3；范围36.0°C - 40.0°C |
| fast_measurement       | bool   | N        | 是否开启快速测温，默认关;启动快速测试则只进行测温检测                                     |
| measurement_range      | int    | N        | 测温环境 0 : 常用 ， 1：夏季                                 |
| health_code_mode       | bool   | Y        | 健康码模式，是否开启健康码，默认关                           |
| health_code_fast_check | bool   | N        | 是否启动健康码快速通行模式，刷码/刷证调用核验健康码 |
| health_code_server_url | String | Y        | 健康核验数据平台地址                                         |
| health_code_timeout    | int    | Y        | 健康码请求超时时间2-30 秒，默认15秒                          |
| show_nuclein           | bool   | N        | 结果显示，是否显示核酸：默认是                               |
| show_id_number         | bool   | N        | 结果显示，显示身份证：默认是                                 |
| show_vaccine           | bool   | N        | 结果显示，是否显示疫苗：默认是                               |
| show_antigen           | bool   | N        | 结果显示，是否显示抗原：默认是                               |
| identify_popup_timeout | int    | N        | 结果显示保留时间2-15 秒，默认2秒                             |
| show_mode_button      | bool   | N        | 按钮展示，是否允许快速通行模式切换                           |
| nuclein_strategy       | int    | N        | 通行依据，核酸检测多少小时阴性允许通行：<br>0：无(不检测核酸有效期 )，1：24小时内有效，2：48小时内有效，3：72:小时内有效。|


### 请求示例:

> `/v1/device/antiepidemic`

```json
{
        "temperature_detect": true,
        "fever_temperature": 37.3,
        "fast_measurement": false,
        "measurement_range": 0,
        "health_code_mode": false,
        "health_code_fast_check": true,
        "health_code_server_url": "http://10.198.21.206:9015",
        "health_code_timeout": 15,
        "show_nuclein": true,
        "show_id_number": true,
        "show_vaccine": true,
        "show_antigen": true,
        "identify_popup_timeout": 2,
        "show_mode_button": true,
        "nuclein_strategy": 0
}
```
### 返回示例

```json
{
    "data": null,
    "code": 200,
    "msg": "OK"
}
```

---

## 获取配置

### 请求路径

> `/v1/device/antiepidemic`

### 请求方式

> GET

### 请求示例

> `​/v1​/device​/antiepidemic`

### 返回示例

```json
{
    "data": {
        "temperature_detect": true,
        "fever_temperature": 37.29999923706055,
        "fast_measurement": false,
        "measurement_range": 0,
        "health_code_mode": false,
        "health_code_fast_check": true,
        "health_code_server_url": "http://10.198.21.206:9015",
        "health_code_timeout": 15,
        "show_nuclein": true,
        "show_id_number": true,
        "show_vaccine": true,
        "show_antigen": true,
        "identify_popup_timeout": 2,
        "show_mode_button": true,
        "nuclein_strategy": 0
    },
    "code": 200,
    "msg": "OK"
}
```

