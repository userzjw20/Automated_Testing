from Automated_Testing.auto_scripts.Cookies import Cookies
import Test_framework

headers = {
    'Content-Type': 'application/json;charset=UTF-8',
}
data = {
    "marketingQueueCode": "test12",
    "marketingQueueName": "测试队列3",
    "marketingQueueStatus": "01",
    "callSupplierCode": "03",
    "remark": "备注123",
    "providerStrategyList": [
        {
            "providerCode": "External_seats_01",
            "coverageRate": "100",
            "marketingEffectiveDay": "32",
            "marketingEndCaseFlag": "01",
            "isAutoUploadForecastCall": "Y",
            "marketingCallTotalLimit": "14",
            "marketingCallDayLimit": "7"
        }
    ]
}

data2 = {
    "marketingQueueName": "",
    "marketingQueueCode": "",
    "callSupplierCode": "",
    "marketingQueueStatus": "",
    "sortAsc": "",
    "sortKey": "",
    "pageNo": 1,
    "pageSize": 50
}

# 获取cookie
ossToken = Cookies().get_cookie()
print(ossToken)

url = "https://lt-srm-docker-06.smyjf.cn/oss-oms/marketing/queue/add"  #新增营销队列
url2 = "https://lt-srm-docker-06.smyjf.cn/oss-oms/marketing/queue/listPage"
url3 = "https://lt-srm-docker-06.smyjf.cn/oss-oms/callSupplier/queryAllEnableCallSupplierConfig"  #查询所有外呼供应商
post = 'post'
get = 'get'

queue_listPage = {}
queue_listPage.update(
    {"url": url2,
     "method": post,
     "headers": headers,
     "cookie": ossToken,
     "data": data2
     })

queryAllEnableCallSupplierConfig = {}
queryAllEnableCallSupplierConfig.update(
    {"url": url3,
     "method": get,
     "headers": headers,
     "cookie": ossToken,
     "data": ""
     })

param_list = []
param_list.append(queue_listPage)
param_list.append(queryAllEnableCallSupplierConfig)

# 循环执行发送请求
# for case in param_list:
#     Test_framework.excute(case)
