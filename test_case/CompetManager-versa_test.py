import allure
import pytest
from common.httpRequests import *
from config.url_conf import URL_Conf
from config.headers import HeadersConf

@allure.feature("赛事大厅模块-反向用例-赛事小组")
class Test_CompetManagerversa:

    @allure.title("赛事小组-创建重名")
    def test_017_CreateGroup(self):
        self.json = {'groupName': "随机赛事小组名1699339618" }
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.CreateGroup_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        print(result)
        assert result["code"] == 202
        assert result["msg"] == '分组名称已存在'

    @allure.title("赛事小组-创建小组名为空")
    def test_018_CreateGroup(self):
        self.json = {'groupName': "" }
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.CreateGroup_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        print(result)
        assert result["code"] == 500
        assert result["msg"] == '分组名称不能为空'

    @allure.title("赛事小组-创建小组名称空参")
    def test_019_CreateGroup(self):
        self.json = { }
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.CreateGroup_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        print(result)
        assert result["code"] == 500
        assert result["msg"] == '分组名称不能为空'    \

    @allure.title("赛事小组-创建小组名称错参")
    def test_020_CreateGroup(self):
        self.json = {'groupNadme': "随机赛事小组名1699339618"}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.CreateGroup_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        print(result)
        assert result["code"] == 500
        assert result["msg"] == '分组名称不能为空'


    @allure.title("赛事小组-创建小组名称多参")
    def test_021_CreateGroup(self):
        self.json = {'groupNaaaaame': "随机赛事小组名1699339618",'groupName': "随机赛事小组名1699343418"}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.CreateGroup_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        print(result)
        assert result["code"] == 202
        assert result["msg"] == '分组名称已存在'

    @allure.title("赛事小组-修改不存在的小组")
    def test_022_AlertGroup(self):
        data = "修改小组名称" + str(int(time.time()))
        self.json = {'id': 1277, 'groupName': data}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.AlertGroup_URL.value,headers=HeadersConf.HEADERS.value, json=self.json)
        result = response.json()
        print(result)
        assert result["code"] == 100400101
        assert result["msg"] == '业务对象为空异常'

    @allure.title("赛事小组-修改小组重名")
    def test_023_AlertGroup(self):
        self.json = {'id': 127, 'groupName': "修改小组名称1699512106"}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.AlertGroup_URL.value,headers=HeadersConf.HEADERS.value, json=self.json)
        result = response.json()
        print(result)
        assert result["code"] == 202
        assert result["msg"] == '分组名称已存在'

    @allure.title("赛事小组-修改小组id为空参")
    def test_024_AlertGroup(self):
        self.json = {'id': "", 'groupName': "修改小组名称1699512106"}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.AlertGroup_URL.value,headers=HeadersConf.HEADERS.value, json=self.json)
        result = response.json()
        print(result)
        assert result["code"] == 500
        assert result["msg"] == '分组ID不能为空'

    @allure.title("赛事小组-修改小组groupName为空参")
    def test_025_AlertGroup(self):
        self.json = {'id': "127", 'groupName': ""}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.AlertGroup_URL.value,headers=HeadersConf.HEADERS.value, json=self.json)
        result = response.json()
        print(result)
        assert result["code"] == 500
        assert result["msg"] == '分组名称不能为空'

    @allure.title("赛事小组-修改小组id错参")
    def test_026_AlertGroup(self):
        self.json = {'id': "12227", 'groupName': "修改06"}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.AlertGroup_URL.value,headers=HeadersConf.HEADERS.value, json=self.json)
        result = response.json()
        print(result)
        assert result["code"] == 100400101
        assert result["msg"] == '业务对象为空异常'

    @allure.title("赛事小组-修改小组groupName错参")
    def test_027_AlertGroup(self):
        self.json = {'id': "127", 'groupNamde': "修改小组名称1699512106"}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.AlertGroup_URL.value,headers=HeadersConf.HEADERS.value, json=self.json)
        result = response.json()
        print(result)
        assert result["code"] == 500
        assert result["msg"] == '分组名称不能为空'

    @allure.title("赛事小组-删除小组id为空")
    def test_028_DeleteGroup(self):
        self.json = {"id": ""}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.DeleteGroup_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        print(result)
        assert result["code"] == 500
        assert result["msg"] == '分组ID不能为空'

    @allure.title("赛事小组-删除小组的id不存在")
    def test_028_DeleteGroup(self):
        self.json = {"id": 343}
        response = requests.post(url=URL_Conf.TEST_URL.value + URL_Conf.DeleteGroup_URL.value,headers=HeadersConf.HEADERS.value,json=self.json)
        result = response.json()
        print(result)
        assert result["code"] == 100400101
        assert result["msg"] == '业务对象为空异常'

if __name__ == '__main__':
    pytest.main()