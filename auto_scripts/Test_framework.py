import requests


def excute(case_info):
    rs = requests.request(url=case_info["url"],
                          method=case_info["method"],
                          headers=case_info["headers"],
                          cookies=case_info["cookie"],
                          json=case_info["data"])

    print(rs.text)
