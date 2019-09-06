"""assert  断言
    每个测试用例都需要断言
    与unittest不同，pytest使用的是python自带的assert关键字进行断言
    assert关键字后面可以接一个表达式，只要表达式的最终结果是true--断言通过，用例执行成功，否则用例执行失败


"""
#  pytest有自己的异常抛出断言套路
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0

# pytest允许我们访问异常的具体信息
def tets_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert 'maximum recursion' in str(excinfo.value)

# 定制断言异常的错误信息(报TypeError？？？)
def test_zero_division_1():
    with pytest.raises(ZeroDivisionError,message="Expecting ZeroDivisionError"):
        1/0