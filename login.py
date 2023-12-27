from requests import request

from samaker.fixture import BaseLogin
from samaker.log import logger


class Login(BaseLogin):

    def login(self) -> dict:
        login_request = {
            "username": self.account.get("user"),
            "password": self.account.get("pwd")
        }
        try:
            resp = request("POST", f"{self.host}/auth/login", json=login_request).json()
        except Exception as e:
            logger.error("登录失败")
            raise e
        print('r:', resp)
        return resp

    def make_headers(self, resp_login: dict) -> dict:
        print(resp_login)
        headers = {
            'Token': resp_login.get("data").get("token")}
        return headers
