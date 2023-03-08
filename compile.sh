#!/bin/bash
pwd

echo '开始编译资源文件...'
for i in *.qrc;
do ./venv/bin/pyside6-rcc "$i" -o "$(basename $i .qrc)_rc.py"
done
echo '资源文件编译完成!'

echo '开始编译ui文件...'
for i in ./ui/*.ui;
#do echo "$i" && "ui/ui_$(basename $i .ui).py"
do ./venv/bin/pyside6-uic "$i" -o "ui/ui_$(basename $i .ui).py"
done
echo 'ui文件编译完成!'