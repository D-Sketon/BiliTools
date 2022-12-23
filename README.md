# BiliTools

ECNU 2021Python课程项目 **仅用于学习用途！**  
BiliTools基于Python编写，包含了视频筛选，收藏排序，视频下载，识别BGM等功能  
 
### Dependencies
 
项目使用了requests库用作爬虫，Pyqt5库用作GUI，aira2用作下载
 
```
pip install requests
pip install pyqt5
```
如果遇到版本问题造成的报错，可以参考本人的版本号：

```
PyQt5                             5.15.4
pyqt5-plugins                     5.15.4.2.2
PyQt5-Qt5                         5.15.2
PyQt5-sip                         12.9.0
pyqt5-tools                       5.15.4.3.2
PyQtWebEngine                     5.15.5
PyQtWebEngine-Qt5                 5.15.2
```
 
关于识别BGM使用了ACRCloud，请事先注册账号获得`access_key`和`access_secret`，并填入`/Parse/musicRecognize.py`中
### Installing
 
直接运行main.py即可

正常运行后控制台会输出如下信息

```
libpng warning: iCCP: known incorrect sRGB profile
QPainter::begin: Painter already active
js: A cookie associated with a cross-site resource at http://api.geetest.com/ was set without the `SameSite` attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with `SameSite=None` and `S
ecure`. You can review cookies in developer tools under Application>Storage>Cookies and see more details at https://www.chromestatus.com/feature/5088147346030592 and https://www.chromestatus.com/feature/5633521622188032.
```
