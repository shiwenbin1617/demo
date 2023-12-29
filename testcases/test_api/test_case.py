# --coding:utf-8--
import pytest

from samaker.base.base_testcase import BaseTestcase
from samaker import samaker

import apis

test_data_file_path = "data/api_data/search_data.yaml"


@pytest.mark.case
# @pytest.mark.usefixtures("clear_resource")
class TestCase(BaseTestcase):
    @pytest.mark.parametrize("test_data", samaker.data_maker(test_data_file_path, "search", "search_data"))
    def test_search_things(self, test_data):
        # print(test_data)
        res = apis.search_obj.search_first(test_data)
        print(res)
        # self.assert_eq(res['code'], 0)

    def test_search_hots(self):
        # print(test_data)
        res = apis.search_obj.search_hot()
        print(res)
        # self.assert_eq(res['code'], 0)

    @pytest.mark.parametrize("limit", samaker.data_maker(test_data_file_path, "search", "search_limit"))
    def test_search_hot_words(self, limit):
        # print(test_data)
        res = apis.search_obj.search_hot_words(limit=limit)
        print(res)
        # self.assert_eq(res['code'], 0)
