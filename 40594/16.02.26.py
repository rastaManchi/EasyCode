
class MyError(Exception):
    pass

def test(num):
    if num < 0:
        raise ValueError()

try:
    test(-2)
except KeyError as e:
    print(e)
