"""
Arquivo para cálculo de volume.
"""

class Volume:
    def __init__(self, base, altura, profundidade):
        self.base = base
        self.altura = altura
        self.profundidade = profundidade

    def cilindro(self):
        """
        Cálculo de volume de cilindro.
        V = A * h
        Onde:
            A = area da base
            h = altura
            V = volume

        Args:
            base (float): Número real que representa o raio da base do cilindro
            altura (float): Número real que representa a altura do cilindro

        Returns:
            float: Número real que representa o volume do cilindro
        """
        PI = 3.1415926538
        r = self.base
        area_base = PI * (r ** 2)
        volume = area_base * self.altura
        return volume

    def cubo(self):
        """
        Cálculo de volume de cubo.
        V = b³
        Onde:
            b = base
            V = volume

        Args:
            base (float): Número real que representa um lado do cubo

        Returns:
            float: Número real que representa o volume do cubo
        """
        volume = self.base ** 3
        return volume

    def esfera(self):
        """
        Cálculo de volume de esfera.
        V = (4 * pi * r^3) / 3
        Onde:
            PI = 3.1415926538
            r = raio
            V = volume

        Args:
            raio (float): Número real que representa o raio da esfera

        Returns:
            float: Número real que representa o volume da esfera
        """
        PI = 3.1415926538
        r = self.base
        volume = ((4 * PI * (r ** 3)) / 3)
        return volume

    def paralelepipedo(self):
        """
        Cálculo de volume de paralelepipedo.
        V = b * h * p
        Onde:
            b = base
            h = altura
            p = profundidade
            V = volume

        Args:
            base (float): Número real que representa a base do paralelepipedo
            altura (float): Número real que representa a altura do paralelepipedo
            profundidade (float): Número real que representa a profundidade do paralelepipedo

        Returns:
            float: Número real que representa o volume do paralelepipedo
        """
        volume = self.base * self.altura * self.profundidade
        return volume

    def piramide_retangular(self):
        """
        Cálculo de volume de piramide retangular.
        V = {(b * p) * h} / 3
        Onde:
            b = base
            p = profundidade
            h = altura
            V = volume

        Args:
            base (float): Número real que representa a base da piramide retangular
            profundidade (float): Número real que representa a profundidade da piramide retangular
            altura (float): Número real que representa a altura da piramide retangular

        Returns:
            float: Número real que representa o volume da piramide retangular
        """
        area_base = self.base * self.profundidade
        volume = (area_base * self.altura) / 3
        return volume

    def piramide_triangular(self):
        """
        Cálculo de volume de piramide triangular.
        V = {[(b * p) / 2] * h} / 3
        Onde:
            b = base
            p = profundidade
            h = altura
            V = volume

        Args:
            base (float): Número real que representa a base da piramide triangular
            profundidade (float): Número real que representa a profundidade da piramide triangular
            altura (float): Número real que representa a altura da piramide triangular

        Returns:
            float: Número real que representa o volume da piramide triangular
        """
        area_base = (self.base * self.profundidade) / 2
        volume = (area_base * self.altura) / 3
        return volume

    def prisma_triangular(self):
        """
        Cálculo de volume de prisma triangular.
        V = {{[(b * p) / 2] ** 2} * raiz(3)} / 4
        Onde:
            b = base
            p = profundidade
            h = altura
            V = volume

        Args:
            base (float): Número real que representa a base do prisma triangular
            profundidade (float): Número real que representa a profundidade do prisma triangular
            altura (float): Número real que representa a altura do prisma triangular

        Returns:
            float: Número real que representa o volume do prisma triangular
        """
        area_base = (self.base * self.profundidade) / 2
        volume = (((area_base ** 2) * (3 ** (1 / 2))) / 4) * self.altura
        return volume
    
    
