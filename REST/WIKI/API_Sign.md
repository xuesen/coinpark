运用REST API进行交易、查询资产等操作，需要先申请apikey。

限速策略：api请求 6次/秒。

### 申请apikey ###
* 登陆 https://www.coinpark.cc/
* 个人中心 -> API管理
* 根据提示生成 key 和 secret，请秘密保存

### 设置apikey操作权限 ###

* 登陆 https://www.coinpark.cc/
* 个人中心 -> API管理 -> 编辑
* 设置 apikey 权限

### 应用apikey ###
* 构建请求参数
```
PATH: apipath
METHOD: POST
PARAMS:
{
	"cmds": "[{\"cmd\":\"user/userInfo\",\"body\":{}}]",
	"apikey":"52135958969bedca0809ac10b9caba758022b0a6",
	"sign":"6a21e39e3f68b6fc2227c4074c7e6a6c"
}
```
```
说明：
	apipath: api请求路径。如：https://api.coinpark.cc/v1/user
	cmds: 请求的 api 参数信息
		cmd: 请求具体的api路径参数，参考下面的 cmd 列表
		body: cmd 对应的参数，参考下面的 cmd 列表
	apikey: 系统生成的 apikey
	sign: 通过 secret 对 cmds 进行 md5 转换后的结果，作为签名
```

* 生成 sign 方法

```
// node.js
	var CryptoJS = require("crypto-js");
	var secret = '7b58254791ada6c0194e6341953f862aff9a91b5';
	var cmds = '[{"cmd":"user/userInfo","body":{}}]';
	var sign = CryptoJS.HmacMD5(cmds, secret).toString();//6a21e39e3f68b6fc2227c4074c7e6a6c
```