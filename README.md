GTT（Global Travel Trace）
---
全球差旅跟踪系统(GTT)

简介
===
	通过微信企业公众帐号上报个人位置.


Checkout the project:
===
	git clone https://github.com/toontong/weixin-GTT
    git submodule init
	git submodule update
    cd deps/
    git checkout develop
	

Run the project
===
	create the cfg.tmol file on the some dir whit file index.py

> ServerDomain="your.domain.com"
>
> [wiexin]
> AppID="your.appid"
>
> AppSecret="9b*************d"
> 
> ServerUrl="/werobot"
>
> Token="you.token"
> 
> EncodingAESKey="************"

	python index.py

