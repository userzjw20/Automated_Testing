import requests


def excute(url, method, headers, cookie, data):
    rs = requests.request(url=url, method=method, headers=headers, cookies=cookie, json=data)

    print(rs.text)
