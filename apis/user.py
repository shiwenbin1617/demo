# --coding:utf-8--
from apis.base import MyBaseApi


class User(MyBaseApi):
    def get_users(self):
        """获取用户列表"""
        http_data = {
            'method': 'get',
            'api_path': '/auth/listUser',
        }
        resp = self.send_http(http_data)
        return resp


user_obj = User()
