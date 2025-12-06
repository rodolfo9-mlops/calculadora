
import pytest
from calculator.calculadora import calculadora
import re

# if __name__ == "__main__":
@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["1", "2", "3"], 5),
        (["2", "10", "4"], 6),
        (["3", "3", "7"], 21),
        (["4", "20", "5"], 4),
        (["5", "2", "2"], 4),
        (["6", "4"], 2)
    ]
)
def test_calculadora(monkeypatch,capsys, inputs, expected):
    sequence = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(sequence))
    
    calculadora()
    captured = capsys.readouterr().out
    match = re.search(r"Resultado.*\d+\.\d+",captured)
    number = re.sub(r"Resultado:\s+",'',match.group())
    assert  float(number) == float(expected)


