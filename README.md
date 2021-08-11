# README

## 环境需求

* Python：3.8
* 已根据requirements.txt安装依赖库

## utils
**工具类**
* check: 封装allure校验类
* db: 数据库类
* log: 日志类
* rd: 随机类
* UtilsPyTest: pytest运行类
* UtilsRandom: 随机数类
* UtilsRedis: 缓存数据库类
* UtilsReport: 测试报告类
* request: 封装接口请求类
* response: 解析接口返回类
* rsa: rsa密码类
* run: 运行类
* time: 时间类
* yaml: yaml文件类


## 示例
* 普通模式

```
*\work>python config.py -v V1.0 -p /demo
```

* Jenkins模式
* 在项目配置中构建 Execute Windows batch command
```
*\work>python config.py -v Jenkins -p /demo
```