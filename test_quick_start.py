#全局函数，作用是把string反转并返回。
def reverse(string):
    return string[::-1]

#2个断言，测试reverse()方法的正确性
def test_veverse():
    string = "good"
    assert reverse(string) == "doog"

    another_string = "itest"
    assert reverse(another_string) == "tseti"
