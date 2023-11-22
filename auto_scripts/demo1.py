

from auto_scripts.Cookies import Cookies
import Test_framework

url = "https://lt-srm-docker-06.smyjf.cn/oss-oms/marketing/queue/add"
url2 = "https://lt-srm-docker-06.smyjf.cn/oss-oms/marketing/queue/listPage"
url3 = "https://lt-srm-docker-06.smyjf.cn/oss-oms/callSupplier/queryAllEnableCallSupplierConfig"

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
# 定义登录接口参数
urlc = "https://lt-srm-docker-06.smyjf.cn/oss-oms/usermanage/login/authenticate"
headersc = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}
datac = {
    "userCode": "zhengjiwei",
    "password": "IhXe2FSvOWrv+IsGI4HaHI9H6o9gcUzH72NVS5EWmTm+ZAVJbyuAwtMiuBe80YbfHUyvmHAiafCxI3dFKd2MgwiiNdeGr7jvYrzIsY6PjMUr2AxMFkBXYSJdBS2rckhtWz1/qdPUoMRgX3xiiXDUcmjDS8xKaHdKlH1edewq+2k=",
    "authCode": ""
}

#获取cookie
ossToken = Cookies().get_cookie(urlc, headersc, datac)

#发送请求
Test_framework.excute(url2, 'post', headers, ossToken, data2)

