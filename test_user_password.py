"""
    Fixture:准备测试数据和初始化测试对象的阶段。
    一般对测试数据和测试对象的管理有这样一些场景：
    1、所有用例开始之前初始化测试数据或对象
    2、所有用例结束之后销毁测试数据或对象
    3、每个用例开始之前初始化测试数据或对象
    4、每个用例结束之后销毁测试数据或对象
    5、在每个/所有module的用例开始之前初始化数据或对象
    6、在每个/所有module的用例开始之前销毁数据或对象
    7、.......
eg：
场景：判断用户的密码中包含简单密码，规则：密码必须至少6位，满足6位的话判断用户的密码不是password123或password之类的弱密码
"""
import pytest
import json
class TestUserPassword(object):
    @pytest.fixture
    def users(self):
        # 读取当前路径下的users.dev.json文件，返回的结果是dict
        return json.loads(open('./users.dev.json','r').read())