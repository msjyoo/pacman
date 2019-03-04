from pacman import pacman, pacman_args


def test_basic():
    assert pacman("test0.txt") == (1, 4, 7)  # Test given case
    assert pacman("test1.txt") != (-1, -1, 0)  # Test really large values
    assert pacman("test2.txt") == (-1, -1, 0)  # Test out of bounds
    assert pacman("test3.txt") == (0, 0, 15)  # Test roundabout
    assert pacman("test4.txt") == (-1, -1, 0)  # Test malformed input
    assert pacman("test5.txt") == (-1, -1, 0)  # Test invalid starting param
    assert pacman("test6.txt") == (9, 0, 9)  # Made up case
    assert pacman("test7.txt") == (3, 1, 6)  # Made up case
    assert pacman("test8.txt") == (1, 4, 7)  # Test non-decimal numbers
