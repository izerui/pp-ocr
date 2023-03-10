# ocr服务

# 环境要求
* python3.10

# 安装依赖(按顺序执行)
* 飞浆: `pip install paddlepaddle -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`
* ocr模块,自编译: `pip install git+https://github.com/izerui/PaddleOCR.git@2.6#egg=paddleocr`
* ocr模块: `pip install paddleocr -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`
  > 卸载protobuf `pip uninstall protobuf`，安装指定protobuf版本: `pip install protobuf==3.20.0 --no-deps -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`
* pyside: `pip install pyside -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`

# 修复依赖错误
* ocr依赖的PyMuPDF==1.20.2版本问题：https://github.com/PaddlePaddle/PaddleOCR/pull/9340
  * 修复方式： 直接修改`site-packages/paddleocr/ppocr/utils/utility.py` line 96 源码，1. 将`pageCount`改为`page_count` 2. 将`getPixmap`改为`get_pixmap`

# 安装问题(mac arm)
* 缺少cv2模块: `pip install opencv-python -i http://pypi.douban.com/simple --trusted-host pypi.douban.com`
* error: command 'swig' failed: No such file or directory: `brew install swig`

# 更多模型
* https://github.com/izerui/PaddleOCR/blob/release/2.6/doc/doc_ch/quickstart.md#11