from apis.base import MyBaseApi


class Search(MyBaseApi):

    def search_first(self, search_name):
        """搜索第一页聚合"""
        http_data = {
            'api_path': '/search',
            'method': 'post',
            'json': {
                "page": 0,
                "pagesize": 0,
                "query": {
                    "name": search_name["name"],
                    "category_id": 0
                }
            }
        }
        resp = self.send_http(http_data)
        return resp

    def search_hot(self):
        """推荐,查询各素材下的热门数据"""
        http_data = {
            'api_path': '/search/hot',
            'method': 'get'
        }
        resp = self.send_http(http_data)
        return resp

    def search_hot_words(self, limit: int):
        """搜索热词"""
        http_data = {
            'api_path': f'/search/hotWords/{limit}',
            'method': 'get'
        }
        resp = self.send_http(http_data)
        return resp


search_obj = Search()
