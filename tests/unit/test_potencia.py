import pytest
from calculator.operations import potencia   # <-- cámbialo al nombre real del módulo


# -----------------------------
# TESTS QUE DEBEN DAR UN RESULTADO
# -----------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 8),
        (4, 0.5, 2.0),
        (-2, 3, -8),
        (10, 0, 1),
        (0.5, 2, 0.25),
    ]
)
def test_safe_power_valid(a, b, expected):
    assert potencia(a, b) == expected