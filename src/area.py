"""
Arquivo para cálculo de área.
"""

class Area:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def circunferencia(self) -> float:
        """
        Cálculo de área de circunferência.
        A = pi * r²
        Onde:
            PI = 3.1415926538
            r = raio
            A = área

        Args:
            raio (float): Número real que representa o raio da circunferência

        Returns:
            float: Número real que representa a área da circunferência
        """
        PI = 3.1415926538
        r = self.base
        return PI * (r ** 2)

    def retangulo(self) -> float:
        """
        Cálculo de área de retângulo.
        A = b * h
        Onde:
            b = base
            h = altura
            A = área

        Args:
            base (float): Número real que representa a base do retângulo
            altura (_type_): Número real que representa a altura do retângulo

        Returns:
            _float: Número real que representa a área do retângulo
        """
        area = self.base * self.altura
        return area
    
    def triangulo(self) -> float:
        """
        Cálculo de área de triângulo.
        A = (b * h) / 2
        Onde:
            b = base
            h = altura
            A = área

        Args:
            base (float): Número real que representa a base do triângulo
            altura (float): Número real que representa a altura do triângulo

        Returns:
            float: Número real que representa a área do triângulo
        """
        return (self.base * self.altura) / 2
