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
分析:
1、使用@pytest.fixture装饰器可以定义feature
2、在用例的参数中传递fixture的名称以便直接调用fixture，拿到fixture的值
3、3个assert是递进关系，前1个assert断言失败后，后面的assert是不会运行的，因此重要的assert放在前面
4、E AssertionError：user tom has a week password 可以很容易判断出是哪条数据出了问题，所以定制可读性好的错误信息很有必要
5、任何1个断言失败以后，for循环就会退出，所以上面的用例1个只能发现1条错误数据，换句话说任何1个assert失败后，用例就终止运行了
执行顺序：
1、pytest找到以test_开头的方法，即test_user_password方法，执行该方法时发现传入的参数里有跟fixture users名称相同的参数
2、pytest认定users是fixture，执行该fixture，读取json文件解析成dict实例
3、test_user_password方法真正被执行，users fixture被传入到该方法
P.S. pytest --fixtures test_user_password.py 查看用例中可用的fixtures
"""
import pytest
import json
class TestUserPassword(object):
    @pytest.fixture
    def users(self):
        # 读取当前路径下的users.dev.json文件，返回的结果是dict
        return json.loads(open('./users.dev.json','r').read())

    def test_user_password(self,users):
        #遍历每条user数据
        for user in users:
            passwd = user['password']
            assert len(passwd) >= 6
            msg = "user %s has a week password" %(user['name'])
            assert passwd != 'password', msg
            assert passwd != 'password123',msg
