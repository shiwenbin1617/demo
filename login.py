from requests import request
from samaker.fixture import BaseLogin
from samaker.log import logger


class Login(BaseLogin):
    def _get_public_key(self):
        try:
            resp = request(method="GET", url=f"{self.host}/auth/preLogin").json()
            if resp.get('code') == 0:
                public_key = resp.get("data").get('public_key')
                print("pub_key = " + public_key)
                return public_key
            else:
                logger.error("获取登陆 public_key 失败")
        except Exception as e:
            raise e

    def login(self) -> dict:
        public_key = self._get_public_key()
        header = {"public_key": public_key}
        login_request = {
            "login_id": self.account.get("user"),
            "password": self.account.get("pwd"),
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
    login_message = Login().login()
