# Web Component Change Log

---

## v0.0.8 (2022-08-20)

*Author: LinPeiCai

**Adapted Devices:**

- SensePassS7 *V1.0.8

**Add:**

- 接口  [POST] [GET] `/v1/event/subscribe` 新增第三方服务器推送配置
- 接口 [POST]  事件推送协议（HTTP/HTTPS）

**Fixed &Modify:**

- 接口 [WSS] `/v1/event/` 事件订阅 修改字段`TrackID` 为`deviceSN` 设备序列号

## v0.0.7

*Author: ChenYang*

**Adapted Devices:**

- SensePassS7 *V1.0.7*

**Add:**

- 接口 [GET] `/v1/device/info`
- 接口 [POST] [GET] `/v1/device/functions`新增`auth_mode`字段用于验证方式

**Fixed &Modify:**

- 接口 [POST] `/v1/device/door` 字段`open_mode`未定义的崩溃修复
- 接口 [PUT] `/v1/group/{id}` 忽略字段`type`
- 接口 [PUT] `/v1/user/{id}` 忽略字段`type`
- 接口 [POST] `/v1/rule` `/v1/rule/{id}` 中提交数据中的字段`special_period` 更名为`special_days`
- 接口 [POST] `/v1/rule` `/v1/rule/{id}` 中提交数据中的字段`onset_point``expire_point`限制到 4102415999000 *(2099-12-31 23:59:59)*
- 接口 [POST] `/v1/device/upgrade` 限制剩余空间必须不少于**600MB**


## v0.0.6
*Author: ChenYang*

**2022-08-08**

**Fixed & Modify:**

- 修复在GUI操作删除 user 未能同步删除已绑定的group记录
- 修复在GUI操作更新 user 后, avatar 内容丢失
- 各批量请求接口请求的`offset`值要求不大于 100000
- 接口 [WSS] `/v1/event` 识别记录类型中 `mode`字段值未能与接口 `/v1/device/functions`中的`mode`字段值同步
- 接口 [WSS] `/v1/event` 识别记录类型中 `rgbImg`字段值解除AES加密,现已为原始 jpeg 数据base64后的内容
- 接口 [WSS] `/v1/event` 多端连接崩溃修复, 并设置最大连接数量为3

## v0.0.5
*Author: ChenYang*

**2022-07-30**

**Fixed & Modify:**

- 统一错误响应code
- 接口 [POST] `/v1/auth/login` 移除 `username` 字段默认值admin，修复`password`字段未空时异常错误
- 接口 [POST]`/v1/user` name字段与avatar字段以及type字段为空时响应异常
- 接口 [POST] `/v1/user`在feature与avatar同时存在值时优先featrue,avatar作图片展示，feature若异常则将返回错误.
- 接口 [PUT] `/v1/group/id/{id}` 可保持name字段原值,但不可变更type字段
- 接口 [POST] `/v1/rule` 修复多个字段缺失导致的异常错误.
- 接口 [GET] `/v1/rule/id/{id}` 修复获取参数onset_point与expire_point未空
- group 与 rule 创建条数限制更新
- 接口 [WSS] `/v1/event` 更新 `rgbImg`字段由YUV图像转为Jpeg格式图.加入`user`字段，加入`pass`字段，加入`type`字段，加入`mode`字段


## v0.0.4
*Author: ChenYang*

**2022-07-25**

**Fixed & Modify:**

- 重构错误处理接口
- 添加所有接口入参检查,预防参数缺失或无效导致的异常情况
- 统一所有接口返回值格式
- 接口 [POST] `/v1/user/` 参数变更
- 接口 [PUT] `/v1/user/id/{id}` 参数变更
- 移除接口 [GET] `/v1/user/all`

**Add:**
- 接口 [POST] [GET] `/v1/device/access`
- 接口 [POST] [GET] `/v1/device/functions`
- 接口 [POST] [GET] `/v1/device/system`
- 接口 [POST] [GET] `/v1/device/custom`
- 接口 [POST] [GET] `/v1/device/time`
- 接口 [POST] `/v1/device/door`
- 接口 [POST] `/v1/group`
- 接口 [GET] [PUT] [DELETE] `/v1/group/id/{id}`
- 接口 [GET] `/v1/group/id/{id}/users`
- 接口 [GET] `/v1/group/offset/{offset}/limit/{limit}`
- 接口 [POST] `/v1/rule`
- 接口 [GET] [PUT] [DELETE] `/v1/rule/id/{id}`
- 接口 [GET] `/v1/rule/id/{id}/groups`
- 接口 [GET] `/v1/rule/offset/{offset}/limit/{limit}`



## v0.0.3

*Author: ChenYang*

**2022-06-25**

**Fixed & Modify:**

- 接口 [POST] `/v1/auth/login`完善 对 `username` 的校验
- 修复所有需提交 `id` 到 `URI`  的接口在`id`非整形数字时崩溃的现象

**Add:**

- 添加设置识别参数接口 [POST] `/v1/device/recognize`
- 添加获取识别参数接口 [GET] `/v1/device/recognize`
- 添加固件升级接口 [POST] `/v1/device/upgrade`


## v0.0.2

*Author: ChenYang*

**2022-05-22**

**Fixed & Modify:**

- 取消非单机模式启动

- 接口 `/v1/RegAuth/login` 变更为 `/v1/auth/login`

- 接口 [POST] `/v1/user`
  - 修复提交字段内容未初始化导致服务崩溃
  - 限制提交的内容,移除未使用的字段: `id`,`staff_type`,`position`,`gender`,`create_at`,`update_at

- 接口 [PUT] `/v1/user/id/{id}`
  - 由原PATCH方法变更为PUT
  - 修复提交字段内容未初始化导致服务崩溃
  - 限制提交的内容,移除未使用的字段: `id`,`staff_type`,`position`,`gender`,`create_at`,`update_at

- 接口 [GET] `/v1/user/id/{id}`
  - 修复获取的avatar字段内容未解密

- 接口 [GET] `/v1/user/offset/{offset/limit/{limit}`
  - 修复offset或limit为0时崩溃
  - 变更limit最大值为10,防止下发内容过大导致内存耗尽.

- 接口 [POST] `/v1/group`
  - 修复提交字段内容未初始化导致服务崩溃
  - 限制提交内容,移除未使用的字段: `id`,`create_at`,`update_at`

- 接口 [PUT] `/v1/group/id/{id}`
   - 修复提交字段内容未初始化导致服务崩溃
	- 限制提交内容,移除未使用的字段: `id`,`create_at`,`update_at`

---

## v0.0.1

*Author: ChenYang*

**2022-05-14**

**Add:**

- Initialization
