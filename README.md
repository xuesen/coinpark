# coinpark

采用同时进行买卖操作
例如：用户拥有usdt200，用户进行ETH_USDT来进行对冲，需要将ETH和usdt各持仓一半，也就是买入100usdt的ETH
然后建议将mount设置<=100usdt

Key：coinpark交易平台上你自己申请的API的key值

secret：API的secret值

mount USDT单次交易数量

symbol 交易对，仅提供与usdt的交易对,例如：symbol=ETH_USDT

order_sleep为订单交易等待时间

trading_Strategy 交易策略

交易策略为两种
等于2代表平价策略(买一卖一取中间值，有千一价差，特点是最容易成交快速买卖)
等于1代表差价策略买一卖一(低买高卖)
建议使用平价

代码有问题可以加微信说，互相交朋友：jianbingguozi1995

代码提供源码，可以自行检查是否有后门，如果老哥们用的好的话给点饭钱就行，在这里给各位老铁抱拳了

USDT地址(非ERC20)：1PSybg27pQ7y9FSo1uKjNmWRrCzgew7tHe

后续会慢慢做量化交易，希望能从小白的道路上走向财务自由

作者：煎饼果子+小矿工

开源倡导者

特此鸣谢大佬https://github.com/nogo6260/coinpark










