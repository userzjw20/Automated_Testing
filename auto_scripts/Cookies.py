import requests
import json
from requests.cookies import RequestsCookieJar

class Cookies:

    def get_cookie(self,url,headers,data):
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


