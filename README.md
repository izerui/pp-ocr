# ocr服务

# 环境要求
* python3.10

# 安装依赖(按顺序执行) 建议使用百度源: 
> 修改全局pip源到百度源: `pip config set global.index-url https://mirror.baidu.com/pypi/simple/`

依赖列表
* protobuf: `pip install protobuf==3.20.0`
* paddlepaddle 和 paddleocr: `pip install paddlepaddle paddleocr`
* pyside: `pip install pyside6`
* pyzbar(识别二维码): `pip install pyzbar`
* 打包pyinstaller: `pip install pyinstaller`
* ~~ocr模块,自编译(未尝试): `pip install git+https://github.com/izerui/PaddleOCR.git@2.6#egg=paddleocr`~~

# 打包
* win: build.bat

# 修复依赖错误
* ocr依赖的PyMuPDF==1.20.2版本问题：https://github.com/PaddlePaddle/PaddleOCR/pull/9340
  * 修复方式： 直接修改`site-packages/paddleocr/ppocr/utils/utility.py` line 96 源码，1. 将`pageCount`改为`page_count` 2. 将`getPixmap`改为`get_pixmap`

# 安装问题(mac arm)
* mac: 
  * 缺少cv2模块: `pip install opencv-python`
  * error: command 'swig' failed: No such file or directory: `brew install swig`
  * Unable to find zbar shared library: `brew install zbar`
* win:
  * `pip install opencv-python-headless`
  * zbar 需要安装微软官方 Visual C++ 2013 (x86、x64)位运行库 https://www.7down.com/soft/2155.html


# 更多模型
* https://github.com/izerui/PaddleOCR/blob/release/2.6/doc/doc_ch/quickstart.md#11