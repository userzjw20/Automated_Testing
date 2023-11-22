import requests
import json
from requests.cookies import RequestsCookieJar

class Cookies:

    def get_cookie(self):

        #定义登录接口参数
        url = "https://lt-srm-docker-06.smyjf.cn/oss-oms/usermanage/login/authenticate"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        data = {
            "userCode": "zhengjiwei",
            "password": "IhXe2FSvOWrv+IsGI4HaHI9H6o9gcUzH72NVS5EWmTm+ZAVJbyuAwtMiuBe80YbfHUyvmHAiafCxI3dFKd2MgwiiNdeGr7jvYrzIsY6PjMUr2AxMFkBXYSJdBS2rckhtWz1/qdPUoMRgX3xiiXDUcmjDS8xKaHdKlH1edewq+2k=",
            "authCode": ""
        }

        #调用登录接口，获取token
        response = requests.post(url, headers=headers, data=data)

        #保存cookie
        cookie_jar = RequestsCookieJar()
        cookie_jar.update(response.cookies)

        return cookie_jar


        # 查找出ossTOKEN的值
        # for cookie in cookie_jar:
        #     if cookie.name == 'ossTOKEN':
        #         ossTOKEN = cookie.value
        # #print(ossTOKEN)
        # return {"ossTOKEN":ossTOKEN}


