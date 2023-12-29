import hashlib

from requests import request
from samaker.fixture import BaseLogin
from samaker.log import logger


class Login(BaseLogin):
    def _get_public_key(self):
        try:
            resp = request(method="GET", url=f"{self.host}/auth/preLogin").json()
            if resp.get('code') == 0:
                public_key = resp.get("data").get('public_key')
                return public_key
            else:
                logger.error("获取登陆 public_key 失败")
        except Exception as e:
            raise e

    def _get_login_code(self, mobile: str):
        jsondata = {
            "mobile": mobile
        }
        try:
            resp = request(method="POST", url=f"{self.host}/auth/loginCode", json=jsondata).json()
            if resp.get('code') == 0:
                data = resp.get("data")
                return data
            else:
                logger.error("获取登陆 public_key 失败")
        except Exception as e:
            raise e

    @staticmethod
    def _pwd_md5(password: str):
        hl = hashlib.md5()
        hl.update(password.encode(encoding='utf-8'))
        return hl.hexdigest()

    def login(self) -> dict:
        public_key = self._get_public_key()
        self._get_login_code(self.account.get("user"))
        header = {"public_key": public_key}
        login_request = {
            "login_id": self.account.get("user"),
            "password": "",
            "sms_code": 222222
        }
        try:
            resp = request("POST", f"{self.host}/auth/login", json=login_request, headers=header).json()
        except Exception as e:
            logger.error("登录失败")
            raise e
        print('r:', resp)
        return resp

    def make_headers(self, resp_login: dict) -> dict:
        headers = {
            'Token': resp_login.get("data").get("token")
        }
        return headers


if __name__ == '__main__':
    login_message = Login()
