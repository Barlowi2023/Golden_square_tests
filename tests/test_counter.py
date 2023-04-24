from lib.Counter import *

def test_counter1():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."

def test_counter2():
    counter = Counter()
    counter.add(12)
    result = counter.report()
    assert result == "Counted to 12 so far."
