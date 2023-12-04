
#定义共同的url

import enum

class URL_Conf(enum.Enum):
    # 环境共同URL
    TEST_URL   = 'http://test-cubev2.cubestation.com/race'
    UAT_URL    = 'http://uat-api.ganrobot.com/user/api/v2/user'
    PROD_URL   = 'https://prod-api.ganrobot.com/gw/userdata'

    # 赛事管理后台-分组接口
    CreateGroup_URL = "/spi/cube/race/manager/group/create"
    DeleteGroup_URL = "/spi/cube/race/manager/group/delete"
    AlertGroup_URL  = "/spi/cube/race/manager/group/alert"
    QueryGroup_URL  = "/spi/cube/race/manager/group/queryPage"

    # 赛事管理后台-类别接口
    CreateSubtype_URL = "/spi/cube/race/manager/subtype/create"
    DeleteSubtype_URL = "/spi/cube/race/manager/subtype/delete"
    AlertSubtype_URL  = "/spi/cube/race/manager/subtype/alert"
    QuerySubtype_URL  = "/spi/cube/race/manager/subtype/queryPage"

    # 赛事管理后台-大厅接口
    CreateMatchHall_URL = "/spi/cube/race/manager/matchHall/create"
    DeleteMatchHall_URL = "/spi/cube/race/manager/matchHall/delete"
    AlertMatchHall_URL  = "/spi/cube/race/manager/matchHall/alert"
    QueryMatchHall_URL  = "/spi/cube/race/manager/matchHall/queryPage"

    # 赛事管理后台-发布赛事接口
    PublishMatchHall_URL = "/spi/cube/race/manager/matchHall/publish"