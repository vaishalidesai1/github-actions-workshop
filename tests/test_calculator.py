from app.calculator import sum, resta, mul

def test_sum() -> None:
    assert sum(2, 3) == 5

def test_resta() -> None:
    assert resta(5, 3) == 2

def test_multiply() -> None:
    assert mul(2, 3) == 6