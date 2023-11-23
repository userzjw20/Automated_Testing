import requests
import pytest
from xToolkit import xfile
from Automated_Testing.auto_scripts.Cookies import Cookies

#读取接口用例
test_data = xfile.read("接口测试用例.xls").excel_to_dict(sheet=1)
#获取token
ossToken = Cookies().get_cookie()

@pytest.mark.parametrize("case_info",test_data)
def test_excute(case_info):
    response = requests.request(url=case_info["接口URL"],
                          method=case_info["请求方式"],
                          headers=eval(case_info["URL参数"]),
                          cookies=ossToken,
                          json=case_info["JSON参数"])

    # print("请求头:")
    # print(response.headers)
    #
    # print("请求体:")
    # print(response.request.body)
    #
    # print("响应体：")
    # print(response.text)
    #
    # print("响应cookie:")
    # print(response.cookies)

if __name__ == '__main__':
    pytest.main(["-vs"])
