"""
任何1条测试数据导致断言不通过后就会停止运行，这样每次只能检查出1条不符合规范的数据
---解决办法：参数化的fixture特性

参数化fixture允许我们向fixture提供参数，参数可以是list，该list中有几条数据，fixture就会运行几次，相应的测试用例也会运行几次
语法:@pytets.fixture(params=["smtp.gmail.com","mail.python.org"])
len(params) 的值=用例执行的次数
在fixture的定义中，可以使用request.param来获取每次传入的参数

使用参数化fixtures来实现一次性检查出弱密码的用例
"""
import pytest
import json
users =json.loads(open('./users.test.json','r').read())

class TestUserPasswordWithParam(object):
    @pytest.fixture(params=users)
    def user(self,request):
        return request.param

    def test_user_password(self,user):
        passwd = user['password']
        assert len(passwd) >= 6
        msg = "user %s has w weak password" %(user['name'])
        assert passwd != 'password',msg
        assert passwd != 'password123',msg