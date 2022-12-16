# Web Component Change Log

---

## v1.2.0 (2022-11-30)

*Author: LinPeicai, ChenYang*

**Adapted Devices:**

- SenseNebula Pass S7 *V1.2.1*

**Add:**

- 接口 [POST] : `/v1/user/search`, 支持使用`name`,`job_number`,`ic_number`字段搜索.
- 接口 [POST] : `/v1/group/search`, 支持使用`name`字段搜索
- 接口 [POST] : `/v1/rule/search`, 支持使用`name`字段搜索
- 接口 [POST] [GET] : `/v1/device/functions` 新增`remote_auth_timeout_to_local_auth`字段，用以支持远程认证服务器不可达时自动切换回本地认证.
- 接口 [POST] : `/v1/event/records/` 支持事件历史记录搜索.
- 接口 [POST]  [GET] : `/v1/auth/certificate` 支持获取与配置Web服务的证书.
- 支持设备广播, 使用 *mDNS* 协议, 广播周期3秒, 服务名称`sensetime`,  `text-record` 条目包括`sn`与`model`.

**Modify:**

- 接口 [POST] `/v1/group` 总数上限改为256。
- 接口 [POST] `/v1/rule` 字段 `period`相关字段的上限改为 12, 策略总数上限改为256.
- 接口 [PUT] `/v1/rule/id/{id}` 字段 `period`相关字段的上限改为 12.
- 接口 [POST]  `/v1/user` 字段`name`,`ic_number`,`id_number`,`job_number`长度限制改为128字节, 即最长42个中文字符, `remark`字段长度限制改为256字节.
- 接口 [POST] `/v1/group` 字段`name`长度限制改为128字节, 即最长42个中文字符.
- 接口 [POST] `/v1/rule` 字段`name`长度限制改为128字节, 即最长42个中文字符.
- 接口 [PUT]  `/v1/user/id/{id}` 字段`name`,`ic_number`,`id_number`,`job_number`长度限制改为128字节, 即最长42个中文字符, `remark`字段长度限制改为256字节.
- 接口 [PUT]  `/v1/group/id/{id}` 字段`name`长度限制改为128字节, 即最长42个中文字符.
- 接口 [PUT]  `/v1/rule/id/{id}` 字段`name`长度限制改为128字节, 即最长42个中文字符.
- 接口 [WSS] `v1/event` 以及事件订阅接口新增`ic_number`,`job_number`字段.
- 接口 [POST] `/v1/device/custom` 字段`welcome_tip`,`verify_success_tip`,`verify_fault_tip`,`unauthorized_user_tip`添加64字节上限检查, `custom_picture_for_logo`,`custom_picture_for_idle`添加4MB大小上限检查.
- 远程服务器认证推送数据新增`recognizeScore`,`ic_number`,`job_number`,`remark`,`guest_time_start`,`guest_time_end`字段.
- 设备配置相关接口错误返回值规范化.

**Fix:**

- 接口 [POST] `/v1/device/functions` 字段`mode` 7 与 8 模式设置未生效
- 策略接口中对 `year`字段处理错误的修正.
- 远程开门常闭模式语音播报错误修复.

## v1.1.0 (2022-10-10)

*Author: ChenYang*

**Adapted Devices:**

- SenseNebula Pass S7 *V1.1.0*
- SenseNebula Pass S8 *V1.1.2*

**Add:**

- 接口 [POST] `/v1/ai/recognitionquality` ，具体内容查看该接口描述
- 接口 [POST] `/v1/ai/feature` ，具体内容查看该接口描述
- 接口 [POST] `/v1/device/antiepidemic` ，具体内容查看该接口描述
- 接口 [GET] `/v1/auth/errors` ，获取错误码信息表

**Fixed & Modify:**

- 接口 [POST]  [GET] `/v1/device/functions`
  - 字段 `auth_mode` 值支持添加 2 和 3 ，具体释义查看该接口描述
  - 新增 `remote_authentication_address` : 当 `auth_mode` 取值非 0 时，则该地址不可空，且作为服务器识别对象
  - 新增事件推送与远程服务器响应参数与示例
  - 字段 `mode` 核验模式文档修改：2：刷脸且刷卡 3：刷脸或刷卡或刷二维码
  
- 接口 [POST]  [GET] `/v1/event/subscribe` 该接口的功能可用于识别记录上传功能，当接收服务器断开，网络异常或者没收到请求应答，设备将缓存该记录，待网络状态恢复后上传识别记录
- 接口 [WSS] `/v1/event` & [POST]`第三方服务器推送配置` 识别记录事件中<br>新增体温`bodyTemperature`字段,消息类型`recognitionType`字段，<br>删除活体精度分值`livenessScore`字段，识别状态`recognizeStatus`字段

- 接口 [POST] `/v1/user` user_id max调整为99999999 （8个9）
- 接口 [POST] `/v1/user` 人员类型新增黑名单类型 type 为 3
- 接口 [POST] `/v1/group` 人员组类型新增黑名单组类型 type 为 3
- 接口 [POST] `/v1/group` group_id max调整为99999999 （8个9）
- 接口 [POST] `/v1/rule`  rule_id max调整为99999999 （8个9）
- 接口 [GET] `/v1​/device​/info` 获取设备基本信息`api_ver`，`model_ver`字段
  
- 修复首次启动后设置单机模式下， Web 功能未启用

- 添加事件主动推送的HTTP请求Header中对Body类型描述为`json`
  
  

## V1.0.0 (2022-09-08)

*Author: WuYi*

**Adapted Devices:**

- SenseNebula Pass S7 *V1.0.8*
- SensePass CS  *V3.3.6*

**Add:**

- 新增英文接口文档

**Fixed & Modify:**

- 

## v0.0.8 (2022-08-20)

*Author: LinPeiCai*

**Adapted Devices:**

- SensePassS7 *V1.0.8

**Add:**

- 接口  [POST]  [GET] `/v1/event/subscribe` 新增第三方服务器推送配置
- 接口 [POST]  事件推送协议（HTTP/HTTPS）

**Fixed & Modify:**

- 接口 [WSS] `/v1/event/` 事件订阅 修改字段`TrackID` 为`deviceSN` 设备序列号

## v0.0.7

*Author: ChenYang*

**Adapted Devices:**

- SensePassS7 *V1.0.7*

**Add:**

- 接口 [GET] `/v1/device/info`
- 接口 [POST]  [GET] `/v1/device/functions`新增`auth_mode`字段用于验证方式

**Fixed & Modify:**

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
- 接口 [POST]  [GET] `/v1/device/access`
- 接口 [POST]  [GET] `/v1/device/functions`
- 接口 [POST]  [GET] `/v1/device/system`
- 接口 [POST]  [GET] `/v1/device/custom`
- 接口 [POST]  [GET] `/v1/device/time`
- 接口 [POST] `/v1/device/door`
- 接口 [POST] `/v1/group`
- 接口 [GET]  [PUT]  [DELETE] `/v1/group/id/{id}`
- 接口 [GET] `/v1/group/id/{id}/users`
- 接口 [GET] `/v1/group/offset/{offset}/limit/{limit}`
- 接口 [POST] `/v1/rule`
- 接口 [GET]  [PUT]  [DELETE] `/v1/rule/id/{id}`
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
