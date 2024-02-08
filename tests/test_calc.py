from src import calc


def test_add_numbers():
    assert calc.add_numbers(2, 2) == 4
    assert calc.add_numbers(0.1, 0.2) == 0.3
    assert calc.add_numbers(0.2222, 2) == 2.2222
    assert calc.add_numbers(1, 0.36) == 1.36
    assert calc.add_numbers(-2.3, 4.123777) == 1.823777
