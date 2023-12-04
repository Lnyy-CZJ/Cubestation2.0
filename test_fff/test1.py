# import os
# import sys
# import pytest
# import json
# from common.http_requests import *
# from config.url_conf import URLConf
# project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# sys.path.append(project_root)
#
# class TestV2x:
#
#     @classmethod
#     def setup_class(cls) -> None:
#         cls.url = URLConf.TEST_URL.value
#         cls.http = HttpRequests(cls.url)
#
#     def setup(self) -> None:
#         self.headers = {'Content-Type': 'application/json', 'User-Agent': 'Node midway-v2x Version/1.28.1'}
#         self.http = HttpRequests(self.url)
#
#     def tearDown(self):
#         pass
#
#     @staticmethod
#     def get_token():
#         headers = {'Content-Type': 'application/json', 'User-Agent': 'Node midway-v2x Version/1.28.1'}
#         response = TestV2x.http.post(url=URLConf.TEST_URL.value, data='{"cmd":"signin","params":{"userName":"smarttest","password":"72be4b7f62832c516b85fb26de59df53"}}', headers=headers)
#         token = response.json()['detail']['token']
#         return token
#
#     def test_001_queryArea(self):
#         """查询区域"""
#         playload = {"cmd": "queryArea", "csrfToken": TestV2x.get_token(), "params": {"cityId": "320200"}}
#         response = TestV2x.http.post(self.url, data=json.dumps(playload), headers=self.headers)
#         resultNote = response.json().get('resultNote')
#         assert resultNote, 'Success'
#
#     def test_002_queryYearlyCheckCount(self):
#         """查询年检总数"""
#         playload = {"cmd": "queryYearlyCheckCount", "Token": TestV2x.get_token(), "params": {}}
#         response = TestV2x.http.post(self.url, data=json.dumps(playload), headers=self.headers)
#         resultNote = response.json().get('resultNote')
#         assert resultNote, 'SUCCESS'
#
#     def test_003_queryTrafficEvent(self):
#         """查询交通事件"""
#         playload = {"cmd": "queryTrafficEvent", "Token": TestV2x.get_token(), "params": {}}
#         response = TestV2x.http.post(self.url, data=json.dumps(playload), headers=self.headers)
#         resultNote = response.json().get('resultNote')
#         assert resultNote, 'Success'
#
#     def test_004_queryRsuCount(self):
#         """查询rsu总数"""
#         playload = {"cmd": "queryRsuCount", "Token": TestV2x.get_token(), "params": {}}
#         response = TestV2x.http.post(self.url, data=json.dumps(playload), headers=self.headers)
#         resultNote = response.json().get('resultNote')
#         assert resultNote, '查询路测设备数量成功！'
#
#     def test_005_queryDeviceDetail(self):
#         """查询设备详情"""
#         playload = {"cmd": "queryDeviceDetail", "params": {"deviceId": '0086860703231572'}, "Token": TestV2x.get_token()}
#         response = TestV2x.http.post(self.url, data=json.dumps(playload), headers=self.headers)
#         resultNote = response.json().get('resultNote')
#         assert resultNote, '查询终端信息成功！'
#
#
# if __name__ == '__main__':
#     pytest.main()
import time


# def generate_phones():
#     for i in range(40000000000, 50000000001):
#         phone = "86" + " " + str(i)
#         print(phone)
# #
# #
# import yaml
# with open("../test_data/login_data.yaml",'r') as f:
#     data = list(yaml.safe_load_all(f))[1]
#     print(data)
import time
print(int(time.time()*1000))
print(int(time.time()*1000)+1000000)