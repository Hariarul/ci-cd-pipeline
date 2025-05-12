from src.main import add

def add_test_func(a,b):
    assert add(1,3)==4
    assert add(0,0)==0
    assert add(4,1)==5