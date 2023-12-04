import allure
import pytest
from common.httpRequests import *
from config.url_conf import URL_Conf
from config.headers import HeadersConf
# @allure.epic()	敏捷中的概念	项目名称
# @allure.feature()	模块名称	模块名
# @allure.story()	用户故事	子模块
# @allure.title (用例的标题)	用例标题	用例标题
@allure.epic("Cubestation")
@allure.feature("赛事大厅模块-正向用例")
class Test_CompetManager:

    # @allure.title("赛事大厅模块-正向用例")
    # 赛事管理后台-分组接口正向用例001-004
    def test_001_CreateGroup(self,set_global_data):
        data = "随机赛事小组名"+ str(int(time.time()))
        self.json = {'groupName': data }
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.CreateGroup_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        print(result)
        GroupID = response.json()["data"]["id"]
        set_global_data("GroupID",GroupID)
        print(GroupID)
        assert result["code"] == 200
        assert result["msg"] == '接口调用成功'
        assert result['data']["groupName"] == data


    def test_002_AlertGroup(self,get_global_data):
        GroupID = get_global_data("GroupID")
        if not GroupID:
            data = "修改小组名称" + str(int(time.time()))
            self.json = {'id': 86, 'groupName': data}
            response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.AlertGroup_URL.value,
                                     headers=HeadersConf.HEADERS.value, json=self.json)
            result = response.json()
            print(result)
            assert result["code"] == 200
            assert result['data']["id"] == 86
            assert result["data"]["groupName"] == data
        else:
            data = "修改小组名称" + str(int(time.time()))
            self.json = {'id': GroupID,'groupName': data}
            response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.AlertGroup_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
            result = response.json()
            print(result)
            assert result["code"] == 200
            assert result['data']["id"] == GroupID
            assert result["data"]["groupName"] == data

    def test_003_DeleteGroup(self,get_global_data):
        GroupID = get_global_data("GroupID")
        self.json = {'id': GroupID}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.DeleteGroup_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        print(result)
        assert result["code"] == 200

    def test_004_QueryGroup(self):
        self.json = {"curPage" : "1","pageSize" : "2"}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.QueryGroup_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        print(result)
        assert result["code"] == 200

    # 赛事管理后台-类别接口正向用例005-006
    def test_005_CreateSubtype(self,set_global_data):
        data = "类别名称" + str(int(time.time()))
        self.json = {'groupId': 70, 'subtypeName': data,"displayTime": int(time.time()),"startTime":int(time.time())+100000,"endTime":int(time.time())+500000,"disappearTime": int(time.time())+1000000}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.CreateSubtype_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        request_body = response.request.body.decode('unicode_escape')
        print(request_body)
        print(result)
        SubtypeID = response.json()["data"]["id"]
        set_global_data("SubtypeID",SubtypeID)
        print(SubtypeID)
        assert result["code"] == 200
        assert result["msg"] == '接口调用成功'
        assert result['data']["subtypeName"] == data

    def test_006_AlertSubtype(self,get_global_data):
        SubtypeID = get_global_data("SubtypeID")
        data = "修改类别名称" + str(int(time.time()))
        self.json = {'groupId': 70, 'subtypeName': data, "subtypeId": SubtypeID,"displayTime": int(time.time()),"startTime":int(time.time())+100000,"endTime":int(time.time())+500000,"disappearTime": int(time.time())+1000000}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.AlertSubtype_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        request_body = response.request.body.decode('unicode_escape')
        print(request_body)
        print(result)
        assert result["code"] == 200
        assert result['data']["id"] == SubtypeID
        assert result["data"]["subtypeName"] == data

    def test_007_DeleteSubtype(self,get_global_data):
        SubtypeID = get_global_data("SubtypeID")
        self.json = {'id': SubtypeID}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.DeleteSubtype_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        request_body = response.request.body.decode('unicode_escape')
        print(request_body)
        print(result)
        assert result["code"] == 200

    def test_008_QuerySubtype(self):
        self.json = {"curPage" : "1","pageSize" : "2"}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.QuerySubtype_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        print(result)
        assert result["code"] == 200

    # 赛事管理后台-大厅接口正向用例009-012
    def test_009_CreateMatchHallTpye2(self,set_global_data):
        data = "大厅名称Tpye2" + str(int(time.time()))
        self.json = {'groupId': 70,
                     'subtypeId': 16,
                     'name': data,
                     "startType": 2,
                     "enrollStime": int(time.time()),
                     "enrollEtime":int(time.time())+10000,
                     "enterTime":int(time.time())+20000,
                     "matchStime": int(time.time())+30000,
                     "rules": 1,
                     "rulesDescr": "这是赛季描述",
                     "bulletin": "这是赛季公告",
                     "reward":""}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.CreateMatchHall_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        request_body = response.request.body.decode('unicode_escape')
        print(request_body)
        print(result)
        assert result["code"] == 200
        assert result["msg"] == '接口调用成功'
        assert result['data']["name"] == data
        MatchHallIDTpye2 = response.json()["data"]["id"]
        set_global_data("MatchHallIDTpye2", MatchHallIDTpye2)
        print(MatchHallIDTpye2)


    def test_010_AlertMatchHallTpye2(self,get_global_data):
        MatchHallIDTpye2 = get_global_data("MatchHallIDTpye2")
        data = "修改大厅名称" + str(int(time.time()))
        self.json = {'groupId': 70,
                     'subtypeId': 16,
                     "id" : MatchHallIDTpye2,
                     'name': data,
                     "startType": 2,
                     "enrollStime": int(time.time()),
                     "enrollEtime":int(time.time())+10000,
                     "enterTime":int(time.time())+20000,
                     "matchStime": int(time.time())+30000,
                     "rules": 1,
                     "rulesDescr": "这是修改了的赛季描述",
                     "bulletin": "这是修改了的赛季公告",
                     "reward":""}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.AlertMatchHall_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        request_body = response.request.body.decode('unicode_escape')
        print(request_body)
        print(result)
        assert result["code"] == 200
        assert result['data']["id"] == MatchHallIDTpye2
        assert result["data"]["name"] == data

    def test_011_DeleteMatchHallTpye2(self,get_global_data):
        MatchHallIDTpye2 = get_global_data("MatchHallIDTpye2")
        self.json = {'id': MatchHallIDTpye2}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.DeleteMatchHall_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        request_body = response.request.body.decode('unicode_escape')
        print(request_body)
        print(result)
        assert result["code"] == 200

    def test_012_CreateMatchHallTpye1(self,set_global_data):
        data = "大厅名称Tpye1" + str(int(time.time()))
        self.json = {'groupId': 70,
                     'subtypeId': 16,
                     'name': data,
                     "startType": 1,
                     "enrollStime": int(time.time()),
                     "enrollEtime":int(time.time())+10000,
                     "enterTime":int(time.time())+20000,
                     "matchStime": int(time.time())+30000,
                     "rules": 1,
                     "rulesDescr": "这是赛季描述",
                     "bulletin": "这是赛季公告",
                     "reward":""}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.CreateMatchHall_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        request_body = response.request.body.decode('unicode_escape')
        print(request_body)
        print(result)
        MatchHallIDTpye1 = response.json()["data"]["id"]
        set_global_data("MatchHallIDTpye1",MatchHallIDTpye1)
        print(MatchHallIDTpye1)
        assert result["code"] == 200
        assert result["msg"] == '接口调用成功'
        assert result['data']["name"] == data


    def test_013_AlertMatchHallTpye1(self,get_global_data):
        MatchHallIDTpye1 = get_global_data("MatchHallIDTpye1")
        data = "修改大厅名称Tpye1" + str(int(time.time()))
        self.json = {'groupId': 70,
                     'subtypeId': 16,
                     "id" : MatchHallIDTpye1,
                     'name': data,
                     "startType": 1,
                     "enrollStime": int(time.time()),
                     "enrollEtime":int(time.time())+10000,
                     "enterTime":int(time.time())+20000,
                     "matchStime": int(time.time())+30000,
                     "rules": 1,
                     "rulesDescr": "这是修改了的赛季描述",
                     "bulletin": "这是修改了的赛季公告",
                     "reward":""}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.AlertMatchHall_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        request_body = response.request.body.decode('unicode_escape')
        print(request_body)
        print(result)
        assert result["code"] == 200
        assert result['data']["id"] == MatchHallIDTpye1
        assert result["data"]["name"] == data

    def test_014_DeleteMatchHallTpye1(self,get_global_data):
        MatchHallIDTpye1 = get_global_data("MatchHallIDTpye1")
        self.json = {'id': MatchHallIDTpye1}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.DeleteMatchHall_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        request_body = response.request.body.decode('unicode_escape')
        print(request_body)
        print(result)
        assert result["code"] == 200

    def test_015_QueryMatchHallTpye1(self):
        self.json = {"curPage" : "1","pageSize" : "2","startType":"1"}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.QueryMatchHall_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        print(result)
        assert result["code"] == 200

    def test_016_QueryMatchHallTpye2(self):
        self.json = {"curPage" : "1","pageSize" : "2","startType":"2"}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.QueryMatchHall_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        print(result)
        assert result["code"] == 200

if __name__ == '__main__':
    pytest.main()