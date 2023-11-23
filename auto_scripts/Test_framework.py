import requests
from xToolkit import xfile


test_data = xfile.read("接口测试用例.xls").excel_to_dict(sheet=1)
print(test_data)
def excute(case_info):
    rs = requests.request(url=case_info["url"],
                          method=case_info["method"],
                          headers=case_info["headers"],
                          cookies=case_info["cookie"],
                          json=case_info["data"])


    print(rs.text)
