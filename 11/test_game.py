import game

def test_compute_puzzle1():
    assert game.compute_puzzle1('example.txt') == 1656

def test_2():
    assert game.compute_puzzle1('data.txt') == 1702

def test_compute_puzzle2():
    assert game.compute_puzzle2('example.txt') == 195