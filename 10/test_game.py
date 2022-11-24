import game

def test_compute_puzzle1():
    assert game.compute_puzzle1('example.txt') == 26397

def test_compute_puzzle2():
    assert game.compute_puzzle2('example.txt') == 288957

def test_score(): 
    assert game.score_stack(['<', '{', '(', '[']) == 294

    