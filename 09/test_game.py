import game

def test_compute_puzzle1():
    assert game.compute_puzzle1('example.txt') == 15

def test_compute_puzzle2():
    assert game.compute_puzzle2('example.txt') == 1134

def test_compute_puzzle2():
    assert game.compute_puzzle2('data.txt') > 480

    