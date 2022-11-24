import game

def test_compute_puzzle1():
    assert game.compute_puzzle1(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']) == 150

def test_compute_puzzle2():
    assert game.compute_puzzle2(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']) == 900



    