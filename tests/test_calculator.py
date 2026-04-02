from app.calculator import sum, resta

def test_sum() -> None:
    assert sum(2, 3) == 5

def test_resta() -> None:
    assert resta(5, 3) == 2