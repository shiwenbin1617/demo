# --coding:utf-8--
from samaker import samaker

from apis.base import MyBaseApi
from apis.user import user_obj


class Env(MyBaseApi):
    def get_envs(self):
        """获取所有环境"""
        http_data = {
            'api_path': '/config/environment/list',
            'method': 'get',
            'params': {'page': '1', 'size': '10'}
        }
        resp = self.send_http(http_data)
        return resp

    def create_env(self):
        """新建环境"""
        http_data = {
            'api_path': '/config/environment/insert',
            'method': 'post',
            'json': {'name': '1', 'remarks': 'test', id: 0}
        }
        resp = self.send_http(http_data)
        return resp


env_obj = Env()
