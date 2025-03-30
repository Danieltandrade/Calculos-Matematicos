"""
Testes para a classe Area do módulo `src.area`.
Verifica se os métodos de cálculo de área de retângulo, triângulo e circunferência 
retornam os valores corretos.
"""

from src import Area

def test_retangulo():
    """
    Testa se o cálculo de área de retângulo retorna o valor correto.
    """
    area = Area(10, 5)
    assert area.retangulo() == 50

def test_triangulo():
    """
    Testa se o cálculo de área de triângulo retorna o valor correto.
    """
    area = Area(10, 5)
    assert area.triangulo() == 25

def test_circunferencia():
    """
    Testa se o cálculo de área de circunferência retorna o valor correto.
    """
    area = Area(10, 0)
    assert area.circunferencia() == 314.15926538
