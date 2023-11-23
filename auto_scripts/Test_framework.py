import jsonpath
import requests
import pytest
from xToolkit import xfile
from Automated_Testing.auto_scripts.Cookies import Cookies
from string import Template

# 读取接口用例
test_data = xfile.read("接口测试用例.xls").excel_to_dict(sheet=1)
# 获取token
ossToken = Cookies().get_cookie()

dic = {}

@pytest.mark.parametrize("case_info", test_data)
def test_excute(case_info):
    url = case_info["接口URL"]
    if '$' in url:
        url = Template(url).substitute(dic)

    response = requests.request(url=url,
                                method=case_info["请求方式"],
                                headers=eval(case_info["URL参数"]),
                                cookies=ossToken,
                                data=eval(case_info["表单参数"]),
                                json=case_info["JSON参数"])
    if case_info["提取参数"]:
        str_list = case_info["提取参数"]
        list_extract_parameters = str_list.split(',')

        #有多个参数可以用for循环提取
        for i in range(len(list_extract_parameters)):
            rlst = jsonpath.jsonpath(response.json(),'$..' + list_extract_parameters[i])
            dic[list_extract_parameters[i]] = rlst[i]

    print()
    # print("请求头: " + str(response.headers))
    # print("请求体: " + str(response.request.body))

    print("响应状态码：" + str(response.status_code))
    print("响应体：" + str(response.text))

    # print("响应cookie: " + str(response.cookies))

if __name__ == '__main__':
    pytest.main(["-vs"])
