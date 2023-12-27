# --coding:utf-8--
from samaker import samaker

from apis.user import user_obj
from apis.base import MyBaseApi


class Project(MyBaseApi):
    def get_projects(self):
        """获取所有项目"""
        http_data = {
            'api_path': '/project/list',
            'method': 'get',
            'params': {'page': '1', 'size': '10'}
        }
        resp = self.send_http(http_data)
        return resp

    @samaker.update("project_info")
    @samaker.dependence(user_obj.get_users, "user_info")
    def create_project(self):
        """新增项目"""
        user_id = self.cache.get_by_jsonpath("user_info", jsonpath_expr="$..[?(@.name=='aomaker')].id")
        http_data = {
            'api_path': '/project/insert',
            'method': 'post',
            'json': {
                "name": self.get_random_name("project"),
                "app": "ad",
                "owner": user_id,
                "description": "a",
                "private": True
            }
        }
        resp = self.send_http(http_data)
        return resp


project_obj = Project()
