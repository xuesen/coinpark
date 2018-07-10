POST API支持批量请求，参数规范如下。
### 参数规范    def multi_sign_cmd(self, cmds ,api_url ='orderpending'):
* 请求格式

```
{
	cmds: [
		{
			cmd: 'v1/user',
			body: {
                            "name": "xxxx"
			}
		},
		{
			cmd: 'name2',
			body: {
				//params2
			}
		}，
		......
	]，
	apikey:"**************",
	sign:"**************"
}
```
```
说明：
	cmds: api请求列表，支持批量请求（注意：必须是string类型）
        cmd: 某个请求api名称
	body: 某个api请求具体参数
        apikey: CoinPark官网申请的apikey
        sign: 签名
```

* 请求失败返回格式
```
{
	error: {
		code: '1000',
		msg: 'something error'
	}
}
```
```
说明：
	code: 错误码
	msg: 错误描述
```

* 请求成功返回格式

```
{
	result: [
		{
			cmd: 'name2',//like user/userInfo
			result: result2 //any type data
		},
		{
			cmd: 'name1',//like user/userInfo
			result: result1 //any type data
		},
		......
	]
}
```

```
说明：
	result: 数组里的数据对应请求的数组 cmds，不保证顺序一致性
	数组中的每一项单独有对应的 result，数据类型是对应 cmd 请求的返回类型
```