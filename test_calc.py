"""pytest潜规则
1、pytest会找当前以及递查找子文件夹下所有的test_*.py或*_test.py的文件，把其当作测试文件
2、在这些文件里，pytest会收集下面的一些函数或方法，当作测试用例
   1）不在类定义中的以test_开头的函数或方法
   2）在以Test开头的类中（不能包含__init__方法），以test_开头的方法
3、pytest也支持unittest模式的用例定义
"""
def add(x,y):
    return x+y

def test_add():
    assert add(1,0)==1
    assert add(1,1)==2
    assert add(1,99)==100
