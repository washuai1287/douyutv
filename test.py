import requests
import json
session=requests.Session()
session.auth=('sysadmin','ibmioc1r6')
url='https://cnwbzp1087.cn.dst.ibm.com/IOCCBackend/ws/secure/alarmType/getAllAlarmType'
resp=session.get(url,verify=False)
data=json.loads(resp.text)
print(data)