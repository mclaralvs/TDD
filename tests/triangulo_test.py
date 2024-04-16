import pytest
from triangulo import triangulo

def test_escaleno_valido():
    assert triangulo(3, 4, 5) == "Triângulo escaleno."

def test_isosceles_valido():
    assert triangulo(3, 3, 2) == "Triângulo isósceles."
    assert triangulo(2, 3, 3) == "Triângulo isósceles."
    assert triangulo(3, 2, 3) == "Triângulo isósceles."

def test_equilatero_valido():
    assert triangulo(2, 2, 2) == "Triângulo equilátero."

@pytest.mark.parametrize("l1, l2, l3", [(2, 2, 3), (2, 3, 2), (3, 2, 2)])
def test_permutacao_isosceles_valido(l1, l2, l3):
    assert triangulo(l1, l2, l3) == "Triângulo isósceles."

def test_valor_zero():
    assert triangulo(2, 0, 2) == "Não é um triângulo."

def test_valor_negativo():
    assert triangulo(-1, 2, 3) == "Não é um triângulo."

def test_soma_igual_terceiro_lado():
    assert triangulo(2, 3, 5) == "Não é um triângulo."

@pytest.mark.parametrize("l1, l2, l3", [(3, 2, 5), (5, 2, 3), (2, 3, 5)])
def test_permutacao_soma_igual_terceiro_lado(l1, l2, l3):
    assert triangulo(l1, l2, l3) == "Não é um triângulo."

def test_todos_valores_zero():
    assert triangulo(0, 0, 0) == "Não é um triângulo."