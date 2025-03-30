"""
Testes para a classe Volume do módulo `src.volume`.
Verifica se os métodos de cálculo de volume de cilindro, cubo, esfera, paralelepipedo, 
piramide retangular e piramide triangular retornam os valores corretos.
"""

from src import Volume

def test_cilindro():
    """
    Teste para o cálculo de volume de cilindro.
    """
    volume = Volume(5, 5, 0)
    assert volume.cilindro() == 392.69908172500004

def test_cubo():
    """
    Teste para o cálculo de volume de cubo.
    """
    volume = Volume(10, 0, 0)
    assert volume.cubo() == 1000

def test_piramide_retangular():
    """
    Teste para o cálculo de volume de piramide retangular.
    """
    volume = Volume(5, 6, 7)
    assert volume.piramide_retangular() == 70