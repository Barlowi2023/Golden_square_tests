from lib.check_codeword import *

def test_check_codeword1():
    result = check_codeword("badger")
    assert result == 'WRONG!'

def test_check_codeword2():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword3():
    result = check_codeword("house")
    assert result == "Close, but nope."