# 更新通行组信息

更新通行组信息，其中`group_id`字段值和`type`字段值不可修改。


## 请求路径

> `/v1/group/id/{id}`

## 请求方式

> PUT

- 请求体: `application/json`

| 字段    | 类型   | 必填 | 字段释义                                                |
| ------- | ------ | ---- | ------------------------------------------------------- |
| name    | String | Y    | 组名称，内容长度1~128字节，不可重                       |
| rule_id | String | N    | 绑定的通行规则id,若该字段不存在或值为空则不绑定通行规则 |

## 请求示例:

更新`group_id`为 3 的通信组信息，`name`设置为*员工组*；`rule_id`设置为 空 ，即取消绑定。

> `/v1/group/id/3`

```json
{
  "name": "员工组",
  "rule_id": ""
}
```
