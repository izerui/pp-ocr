# ocr服务

# 环境要求
* python3.10

# 安装依赖(按顺序执行) 建议使用百度源: 
> 修改全局pip源到百度源: `pip config set global.index-url https://mirror.baidu.com/pypi/simple/`

依赖列表
* protobuf: `pip install protobuf==3.20.0`
* paddlepaddle 和 paddleocr: `pip install paddlepaddle paddleocr`
* pyside: `pip install pyside6`
* ~~ocr模块,自编译(未尝试): `pip install git+https://github.com/izerui/PaddleOCR.git@2.6#egg=paddleocr`~~


# 修复依赖错误
* ocr依赖的PyMuPDF==1.20.2版本问题：https://github.com/PaddlePaddle/PaddleOCR/pull/9340
  * 修复方式： 直接修改`site-packages/paddleocr/ppocr/utils/utility.py` line 96 源码，1. 将`pageCount`改为`page_count` 2. 将`getPixmap`改为`get_pixmap`

# 安装问题(mac arm)
* 缺少cv2模块: `pip install opencv-python -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`
* error: command 'swig' failed: No such file or directory: `brew install swig`

# 更多模型
* https://github.com/izerui/PaddleOCR/blob/release/2.6/doc/doc_ch/quickstart.md#11