import logging
import colorlog
import pytest

################################################################
# 定义一个全局变量，用于存储内容
global_data = {}
@pytest.fixture
def set_global_data():
    """
    设置全局变量，用于关联参数
    :return:
    """
    def _set_global_data(key, value):
        global_data[key] = value
    return _set_global_data

@pytest.fixture
def get_global_data():
    """
    从全局变量global_data中取值
    :return:
    """

    def _get_global_data(key):
        return global_data.get(key)

    return _get_global_data

################################################################
# 设置colorlog的日志格式
formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s %(message)s",
    log_colors={
        'DEBUG': 'blue',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    },
)

# 将日志输出到控制台
# stream = logging.StreamHandler()
# stream.setFormatter(formatter)
# logger = logging.getLogger()
# logger.addHandler(stream)

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.when == "call":
        if call.excinfo is not None:
            # 获取测试用例的执行结果
            result = call.excinfo
            # 将失败信息写入日志文件
            logging.error(f"Test case {item.name} failed: {result}")