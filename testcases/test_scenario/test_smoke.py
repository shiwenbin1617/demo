# --coding:utf-8--
import pytest
from samaker.base.base_testcase import BaseTestcase

import apis
import business


class TestSmoke(BaseTestcase):
    @pytest.mark.smoke
    def test_smoke(self):
        # 1.创建项目
        res = apis.project_obj.create_project()
        self.assert_eq(res.get('code'), 0)
        # 2.创建环境
        # apis.env_obj.create_env()
        # 3.创建测试用例
        res = business.CaseBusiness.create_case()
        self.assert_eq(res.get('code'), 0)
        # 4.创建测试计划
        res = apis.plan_obj.create_plan()
        self.assert_eq(res.get('code'), 0)
        # 5.执行测试计划
        res = apis.plan_obj.run_plan()
        self.assert_eq(res.get('code'), 0)
