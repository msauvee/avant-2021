import game

def test_compute_puzzle1():
    assert game.compute_puzzle1('example.txt') == 42

def test_compute_puzzle1():
    assert game.compute_puzzle1('data.txt') > 6376

def test_compute_puzzle2():
    assert game.compute_puzzle2('example.txt') == 12
