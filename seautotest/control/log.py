import datetime
import logging
import sys
from pathlib import Path

from seautotest.control.utils import mkdir


def today():
    # 获取当前时间
    now = datetime.datetime.now()
    return now.strftime('%y%m%d')


looger = logging.getLogger("seautotest")
# 指定格式
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s line:%(lineno)d:%(massage)s')

# 创建log文件
mkdir("log")

# 文件日志
log_file = str(Path('log') / '{}.log'.format(today()))
file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-80", delay=False)
file_handler.setFormatter(formatter)

# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter

# 为logger添加日志处理器
looger.addHandler(file_handler)
looger.addHandler(console_handler)

# 指定日志级别默认warning
# DEBUG，INFO，WARNING，ERROR，CRITICAL
looger.setLevel(logging.INFO)
