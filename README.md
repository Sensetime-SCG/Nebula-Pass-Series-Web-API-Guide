# Web Component Change Log

---
## v1.3.0 (2023-05-15)

*Author: JinPingMi & LPC*

**Adapted Devices:**

- SenseNebula Pass S7 *V1.3.0*
- SenseNebula Pass S8 *V1.3.0*

**重要提醒:**
- 人员管理：人员信息`user_id` 为 string 类型, 人员组`group_id`为 string 类型.
- 组管理:   组信息 `group_id` 为string 类型, 通行策略信息`rule_id` 为string 类型.
- 策略管理: 通行策略信息`rule_id`为string 类型.

**Add:**
- [POST]`推送配置` 记录事件字段属性中新增开门方式`entry_mode`字段,异常事件类型`abnormal_type`字段，开门密码`pin`字段,更新事件推送示例。
- [POST]`推送配置` 新增设备告警事件，事件类型字段 type =1 ，具体内容查看该接口描述.
- 接口 [POST]  [GET] `/v1/device/functions`   `auth_mode = 1` 本地认证+远程开门事件推送与远程服务器响应参数：
  - 新增二维码信息`qrcode_content`字段，识别精度分值`recognizeScore`字段,开门方式`entry_mode`字段；
  - 新增人员信息开门密码`pin`字段,user_id所在的组信息`groups`字段。
- 接口 [POST] `/v1/user`  ,`/v2/user` 创建/修改人员，字段` avatar` ，` feature` 为非必填项。支持无图片人员信息下发。当字段` avatar` ，` feature` 同时为空字符串或者为NULL时，清除人员特征数据。
- 接口 [POST] : `/v1/event/records/`  事件历史记录搜索：
  - 新增排序方式`sort`字段；
  - 返回字段新增开门方式`entry_mode`字段,异常事件类型`abnormal_type`字段.
- 接口 [GET] : `/v2/device/logs`, 获取设备系统日志,具体内容查看该接口描述.
- 接口 [POST]  [GET]  : `/v1/device/access/`  设备门禁参数中新增重复识别间隔`resign_interval`字段,串口开关`serial_port`字段，串口波特率`serial_port_baudrate`字段.<br>新增韦根通讯接口参数 `wiegand_settings` 对象， 刷卡设置接口参数 `rfid_settings`对象，具体内容查看该接口描述.
- 接口 [POST]  [GET]   : `/v1/device/custom/`  设备自定义参数中新增自定义待机屏保 `custom_screensavers` 对象，具体内容查看该接口描述.

**Modify:**

- 接口 [POST] `/v1/user`  ,`/v2/user` 创建/修改人员，人员类型字段: 黑名单由数值 `3` 修改为 `5`
- 接口 [POST] `/v1/group`  ,`/v2/group` 创建/修改人员组，人员类型字段: 黑名单由数值 `3` 修改为 `5`.
- 接口 [POST]  [GET]  : `/v1/device/access/`  设备门禁参数中修改开门方式 `open_door_type`字段。删除韦根输入口: `wigan_input`字段
- 接口 [POST]  [GET]   : `/v1/device/custom/`  设备自定义参数中修改是否展示logo `show_custom_logo`字段由Boolean 改为Int 类型，数值0:展示默认logo，1：展示自定义logo，2：关闭 ；默认 ：2  .<br>删除定义待机图片`custom_picture_for_idle`字段
- 接口 [POST]  [GET] `/v1/device/functions`  字段 `auth_mode` 认证类型值删除 2: 服务器认证 ，具体查看该接口描述和应用示例。

**Fix:**

- 修复通行策略设置例外时间段优先策略。

## v1.2.1 (2023-03-15)

*Author: JinPingMi & LPC*

**Adapted Devices:**

- SenseNebula Pass S7 *V1.2.3*
- SenseNebula Pass S8 *V1.2.3*

**重要提醒:**
- 人员管理：人员信息`user_id` 由 int 改为 string 类型, 人员组`group_id`由 int 改为 string 类型.
- 组管理:   组信息 `group_id` 由 int 改为string 类型, 通行策略信息`rule_id` 由int 改为string 类型.
- 策略管理: 通行策略信息`rule_id` 由 int 改为string 类型.

**Add:**

- 所有接口请求返回Header中新增设备型号`model`、设备SN号`sn`、时间戳`timestamp`、`account`信息.
- [POST]`推送配置` 记录事件主动推送的HTTPS请求Header中新增设备型号`model`、设备SN号`sn`、时间戳`timestamp`、`account`信息.
- [POST]`推送配置` 记录事件字段属性中新增记录id`uuid`字段,人员信息的`id_number`,`groups[]`字段.
- 支持设备广播, 使用 *mDNS* 协议, 广播周期3秒, 服务名称`sensetime`,  `text-record` 条目包括`sn`与`model`.
- 远程鉴权推送数据新增人员信息的`id_number`字段.
- 接口 [POST] : `/v1/event/records/`  事件历史记录搜索中新增记录id`uuid`字段,人员信息的`id_number`,`groups[]`字段.
- 接口 [GET] : `/v2/datasync/ping`, 设备心跳接口,该接口请求参数，无鉴权,具体内容查看该接口描述.
- 接口 [GET] : `/v2/datasync/info`, 获取设备所有人员，组，策略简要信息，如`id`、`update_at`, 具体内容查看该接口描述.
- 接口 [GET] : `/v2/datasync/clear`, 清除设备所有人员，组，策略数据,具体内容查看该接口描述.
- 接口 [POST]：`/v2/user`, 批量新增或者修改人员信息,具体内容查看该接口描述.
- 接口 [DELETE]：`/v2/user`, 批量删除人员信息,具体内容查看该接口描述.
- 接口 [POST]：`/v2/group`, 批量新增或者修改组信息,具体内容查看该接口描述.
- 接口 [DELETE]：`/v2/group`, 批量删除组信息,具体内容查看该接口描述.
- 接口 [POST]：`/v2/rule`, 批量新增或者修改策略信息,具体内容查看该接口描述.
- 接口 [DELETE]：`/v2/rule`, 批量删除策略信息,具体内容查看该接口描述.

**Modify:**

- 接口 [GET] `/v1/user/offset/{offset}/limit/{limit}`  人员管理分页搜索,limit值范围是 0 到 100.
- 接口 [GET] `/v1/group/offset/{offset}/limit/{limit}` 组管理分页搜索,limit值范围是 0 到 100.
- 接口 [GET] `/v1/rule/offset/{offset}/limit/{limit}`  策略管理分页搜索,limit值范围是 0 到 100.
- 接口 [POST] `/v1/event/records`  事件历史搜索 ,limit值默认100，最大值200,.
- 接口 [POST] `/v1/user` 支持创建和更新人员信息，如user_id不存在则创建人员信息，如user_id存在则更新人员信息.
- 接口 [POST] `/v1/group` 支持创建和更新组信息，如gourp_id不存在则创建组信息，如roup_id存在则更新组信息.
- 接口 [POST] `/v1/rule` 支持创建和更新策略信息，如rule_id不存在则创建策略信息，如rule_id存在则更新策略信息.
- 接口 [POST] `/v1/user`,`/v1/group`,`/v1/rule`, 新增更新时间`update_at`和创建时间`create_at`参数,默认由设备系统维护.
- 接口 [POST]  [GET] `/v1/device/functions`
  - 字段 `mode` 核验模式值支持添加 9：刷卡且输PIN ，具体释义查看该接口描述
  - 事件推送与远程服务器响应参数<br>人员信息`user_id` 由 int 改为 string 类型

**Fix:**
- 修复通行策略设置周日全天不可通行的缺陷
- 修复服务器认证返回值 --verify_code = 2 设备显示信息不正确的缺陷


## v1.2.0 (2022-11-30)

*Author: ChenYang*

**Adapted Devices:**

- SenseNebula Pass S7 *V1.2.1*

**Add:**

- 接口 [POST] : `/v1/user/search`, 支持使用`name`,`job_number`,`ic_number`字段搜索,具体内容查看该接口描述
- 接口 [POST] : `/v1/group/search`, 支持使用`name`字段搜索,具体内容查看该接口描述
- 接口 [POST] : `/v1/rule/search`, 支持使用`name`字段搜索,具体内容查看该接口描述
- 接口 [POST] [GET] : `/v1/device/functions` 新增`remote_auth_timeout_to_local_auth`字段，用以支持远程认证服务器不可达时自动切换回本地认证.
- 接口 [POST] : `/v1/event/records/` 支持事件历史记录搜索,具体内容查看该接口描述
- 接口 [POST]  [GET] [DELETE] : `/v1/auth/certificate` 支持 获取 / 配置 / 还原 Web服务的证书,具体内容查看该接口描述
- 支持设备广播, 使用 *mDNS* 协议, 广播周期3秒, 服务名称`sensetime`,  `text-record` 条目包括`sn`与`model`.

**Modify:**

- 接口 [POST] `/v1/group` 总数上限改为256。
- 接口 [POST] `/v1/rule` 字段 `period`相关字段的总数上限改为 12, 策略总数上限改为256.
- 接口 [PUT] `/v1/rule/id/{id}` 字段 `period`相关字段的总数上限改为 12.
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
