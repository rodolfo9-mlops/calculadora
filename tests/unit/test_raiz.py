import pytest 
from calculator.operations import raiz_cuad

@pytest.mark.parametrize(
    "input_value, expected",
    [
        (0, 0),
        (1, 1),
        (4, 2),
        (9, 3),
        (2.25, 1.5),
    ]
)
def test_safe_sqrt_valid(input_value, expected):
    assert raiz_cuad(input_value)==expected