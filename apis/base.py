# --coding:utf-8--
from samaker.base.base_api import BaseApi
from samaker.base.base_testcase import BaseTestcase as BaseAssertion

from utils import UtilsMixin


class MyBaseApi(BaseApi, UtilsMixin):

    def build_http_data(self, *, api_path: str, method: str, dataclass_obj) -> dict:
        data = self._filter_none_field(dataclass_obj)
        return {"api_path": api_path, "method": method, "json": data}

    @staticmethod
    def _filter_none_field(dataclass_obj):
        """过滤掉dataclass中的None字段"""
        data = dataclass_obj.all_fields
        return {k: v for k, v in data.items() if v is not None}
