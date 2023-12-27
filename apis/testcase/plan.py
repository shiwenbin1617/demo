# --coding:utf-8--
from samaker import samaker

from apis.project import project_obj
from apis.env import env_obj
from apis.testcase.case import case_obj
from apis.base import MyBaseApi
from apis.testcase import model


class Plan(MyBaseApi):
    def get_plans(self):
        """获取所有测试计划"""
        http_data = {
            'api_path': '/testcase/plan/list',
            'method': 'get',
            'params': {'page': '1', 'size': '10'}
        }
        resp = self.send_http(http_data)
        return resp

    @samaker.dependence(project_obj.get_projects, "project_info")
    @samaker.dependence(env_obj.get_envs, "env_info")
    @samaker.dependence(case_obj.get_testcases, "case_info")
    def create_plan(self, plan_name: str = None, **kwargs):
        """新建测试计划"""
        project_id = self.cache.get_by_jsonpath("project_info", jsonpath_expr="$..[?(@.name=='aomaker-test')].id")
        env_id = self.cache.get_by_jsonpath("env_info", jsonpath_expr="$..[?(@.name=='Test')].id")
        case_id_list = self.cache.get_by_jsonpath("case_info", jsonpath_expr="$..id", expr_index=None)

        if plan_name is None:
            plan_name = self.get_random_name('plan')

        params_model = model.CreatePlan(name=plan_name, env=[env_id], case_list=case_id_list, project_id=project_id,
                                        **kwargs)

        http_data = self.build_http_data(api_path="/testcase/plan/insert", method="post", dataclass_obj=params_model)
        resp = self.send_http(http_data)

        return resp

    @samaker.dependence("plan_obj.get_plans", "plan_info", imp_module="apis.testcase.plan")
    def run_plan(self):
        """执行测试计划"""
        plan_id = self.cache.get_by_jsonpath("plan_info", jsonpath_expr="$..id")
        http_data = {
            'api_path': '/testcase/plan/execute',
            'method': 'get',
            'params': {
                "id": plan_id
            }
        }
        resp = self.send_http(http_data)
        return resp


plan_obj = Plan()
