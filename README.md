## 介绍

**铁虎 API**

[官方文档](https://www.showdoc.com.cn/1735808258920310/9467753400037587)

## 软件架构

~python 3.*

## 安装教程

```shell
pip install guolei-py3-tiehu
```

## 目录说明

### Parking Api 示例

```python
from guolei_py3_tiehu.parking import Api as GuoleiPy3TiehuParkingApi

# 使用前联系铁虎运维给所在服务器ip添加白名单
guolei_py3_tiehu_parking_api = GuoleiPy3TiehuParkingApi(
    base_url="your base url",
    parking_id="your parking id",
    app_key="your app key"
)
# 调用 guolei_py3_tiehu_parking_api.方法
```
