# --coding:utf-8--
from samaker import samaker

from apis.project import project_obj
from apis.base import MyBaseApi


class Case(MyBaseApi):
    @samaker.dependence(project_obj.get_projects, "project_info")
    def get_directory(self):
        """获取测试目录"""
        project_id = self.cache.get_by_jsonpath("project_info", jsonpath_expr="$..[?(@.name=='cs')].id")
        http_data = {
            'api_path': '/testcase/directory',
            'method': 'get',
            'params': {'project_id': project_id,
                       'move': True}
        }
        resp = self.send_http(http_data)
        return resp

    @samaker.update("directory_info")
    @samaker.dependence(project_obj.get_projects, "project_info")
    def create_directory(self):
        """新建目录"""
        project_id = self.cache.get_by_jsonpath("project_info", jsonpath_expr="$..[?(@.name=='cs')].id")
        http_data = {
            'api_path': '/testcase/directory/insert',
            'method': 'post',
            'json': {
                "name": "test3",
                "project_id": project_id,
                "parent": None
            }
        }
        resp = self.send_http(http_data)
        return resp

    @samaker.dependence("case_obj.get_directory", "directory_info", imp_module="apis.testcase.case")
    def get_testcases(self):
        """获取测试用例"""
        directory_id = self.cache.get_by_jsonpath("directory_info", jsonpath_expr="$..value")
        http_data = {
            'api_path': '/testcase/list',
            'method': 'get',
            'params': {'directory_id': directory_id, 'name': '', 'create_user': ''}
        }
        resp = self.send_http(http_data)
        return resp

    @samaker.update("case_info")
    @samaker.dependence("case_obj.get_directory", "directory_info", imp_module="apis.testcase.case")
    def create_case(self, test_data: dict = None):
        """新建用例"""
        if test_data is None:
            test_data = {"name": self.get_random_name("用例")}

        directory_id = self.cache.get_by_jsonpath("directory_info", jsonpath_expr="$..value")
        http_data = {
            'api_path': '/testcase/create',
            'method': 'post',
            'json': {
                "case": {
                    "name": test_data["name"],
                    "priority": "P0",
                    "status": 3,
                    "request_type": 1,
                    "tag": None,
                    "case_type": 0,
                    "request_method": "GET",
                    "url": "https://www.baidu.com",
                    "directory_id": directory_id,
                    "request_headers": "{}"
                },
                "asserts": [],
                "data": [],
                "constructor": [],
                "out_parameters": []
            }
        }
        resp = self.send_http(http_data)
        return resp

    @samaker.update("case_info")
    @samaker.dependence("case_obj.get_testcases", "case_info", imp_module="apis.testcase.case")
    def delete_case(self, case_id: list = None):
        all_case_id = self.cache.get_by_jsonpath("case_info", jsonpath_expr="$..id", expr_index=None)
        if case_id:
            all_case_id = case_id
        http_data = {
            'api_path': '/testcase/delete',
            'method': 'delete',
            'json': all_case_id
        }
        resp = self.send_http(http_data)
        return resp


case_obj = Case()
