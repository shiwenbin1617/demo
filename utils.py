# --coding:utf-8--
import time


class UtilsMixin:
    @staticmethod
    def get_random_name(prefix=None):
        """生成随机名称"""
        if prefix is None:
            prefix = 'test'

        def get_time():
            return time.strftime("%H%M%S", time.localtime(time.time()))
        return prefix + get_time()

