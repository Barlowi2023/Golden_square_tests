from lib.greet import *

def test_greet():
    result = greet("Dave")
    assert result == "Hello, Dave!"