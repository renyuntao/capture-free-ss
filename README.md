# 简介       
该程序运行于VPS之上，用于抓取 [IShadowsocks](http://www.ishadowsocks.com) 上的免费Shadowsocks帐号，并将抓取的免费Shadowsocks帐号通过E-mail发送给在文件 **UserAddr.txt** 中保存的邮箱中。         
参见: [免费SS帐号分享](http://user.qzone.qq.com/498266085/blog/1457402662)
    
# 原理说明            
通过Linux系统中的 **Cron** 服务定时运行程序 **GetSs.py** 来抓取 **IShadowsocks** 上的免费Shadowsocks帐号,抓取到的Shadowsocks帐号信息会以 **JSON** 格式保存到文件 **ssinfo.txt** 文件中去，之后 **GetSs.py** 程序中会调用 **SendMail.sh** Shell 脚本来向 **UserAddr.txt** 文件中保存的邮箱发送抓取到的免费 Shadowsocks帐号信息。
            
文件 **ssadd.txt** 用于保存额外的Shadowsocks帐号信息，这些Shadowsocks帐号信息并非来自于 **IShadowsocks**.通过将 **GetSs.py** 中第60行的如下语句:   
    
```python
additional = False
```
修改为     
  
```python
additional = True
```
即可向 **UserAddr.txt** 保存的邮箱中同时发送该文件中的Shadowsocks帐号信息.                   


