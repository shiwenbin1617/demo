# --coding:utf-8--
import apis


class CaseBusiness:
    @classmethod
    def create_case(cls):
        """新建用例"""
        res = apis.case_obj.get_directory()
        if not res.get('data'):
            apis.case_obj.create_directory()
        return apis.case_obj.create_case()
