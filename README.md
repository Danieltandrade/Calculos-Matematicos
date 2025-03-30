# Calculos Matemáticos

![Python](https://img.shields.io/badge/Python-3.10|3.11|3.12-blue.svg)
![Licença](https://img.shields.io/badge/Licença-MIT-green.svg)
![Status do Projeto](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow.svg)
![Versão](https://img.shields.io/badge/Versão-1.0.0-red.svg)
![Plataforma](https://img.shields.io/badge/Plataforma-Linux%2FWindows%2FMacOS-blue.svg)

Projeto desenvolvido para calcular a área e o volume de diversas figuras geométricas.

## Objetivo

O objetivo do projeto é criar uma ferramenta útil e eficiente para calcular a área e o volume de diferentes figuras geométricas.

## Descrição

O projeto possuí em sua estrutura os diretórios:
* log: Arquivo para criar logs.
* src: Arquivos para cálculos de área e volume.
* tests: Arquivos para testes unitários.
* main.py: Arquivo principal do projeto.

Abaixo é apresentado a estrutura completa do projeto:

```bash
Calculos-Matematicos/
├── log/
│   ├── __init__.py
│   └── log.py
├── src/
│   ├── __init__.py
│   ├── area.py
│   └── volume.py
├── tests/
│   ├── __init__.py
│   ├── test_area.py
│   ├── test_log.py
│   └── test_volume.py
├── __version__.py
├── .gitignore
├── LICENSE
├── main.py
├── log.log
├── README.md
└── requirements.txt
```

O projeto possuí duas classes para cálculos de área e volume. Com cada classe contendo métodos para cálculos de diversas figuras geométricas.

    1. Classe Area.
        - Área da circunferência
        - Área de retângulos/quadrados
        - Área de triângulos

    2. Classe Volume.
        - Volume de cubos
        - Volume de esferas
        - Volume de cilindros
        - Volume de paralélepipedos
        - Volume da piramide retangular
        - Volume da piramide triangular
        - Volume do prisma triangular

Também está presente no projeto a funcionalidade de log, registrando no arquivo "log.log" as interações do usuário.

## Uso

Para utilizar o projeto siga os passos abaixo:
1. Clonar o repositório do projeto: `git clone https://github.com/Danieltandrade/Calculos-Matematicos.git`
2. Instalar as dependências: `pip install -r requirements.txt`
3. Executar o projeto: `python main.py`

> [!IMPORTANT]
> Para não ter problemas ao executar o projeto, recomenda-se criar um ambiente virtual.

## Exemplos

Cálculo de Área:
```bash
Escolha uma opção abaixo:
1 -> Área
2 -> Volume
3 -> Sair
Digite a opção desejada: 1
Escolha uma opção abaixo:  
1 -> Área do Retângulo     
2 -> Área do Triângulo     
3 -> Área da Circunferência
Digite a opção desejada: 2 
Digite o valor da base: 5
Digite o valor da altura: 5
A area do triângulo e: 12.5
```

Cálculo de Volume:
```bash
Escolha uma opção abaixo:     
1 -> Área
2 -> Volume
3 -> Sair
Digite a opção desejada: 2
Escolha uma opção abaixo:
1 -> Volume do Cilindro
2 -> Volume do Cubo
3 -> Volume da Esfera
4 -> Volume do Paralelepipedo
5 -> Volume da Piramide Retangular
6 -> Volume da Piramide Triangular
7 -> Volume do Prisma Triangular
Digite a opção desejada: 4
Digite o valor da base: 5
Digite o valor da altura: 5
Digite o valor da profundidade: 5
O volume do paralelepipedo e: 125.0
```	

Log:
```log
INFO - 2025-03-30 17:09:30,433 - my_user - Opcao Selecionada: 1 - Resultado: Area
INFO - 2025-03-30 17:09:44,528 - my_user - Area do Triangulo - Resultado: 12.5
INFO - 2025-03-30 17:09:47,608 - my_user - Opcao Selecionada: 2 - Resultado: Volume
INFO - 2025-03-30 17:09:55,905 - my_user - Volume do Paralelepipedo - Resultado: 125.0
INFO - 2025-03-30 17:10:02,708 - my_user - Opcao Selecionada: 0 - Resultado: Saindo...
WARNING - 2025-03-30 17:10:02,708 - my_user - Opcao de calculo invalida - Resultado: Novo Loop de Calculo!
INFO - 2025-03-30 17:10:06,007 - my_user - Opcao Selecionada: 3 - Resultado: Saindo...
```

> [!NOTE]
> No projeto não foi aplicado o uso de unidades.

## Contribuições

Se desejar contribuir, sinta-se livre para fazer pull requests ou abrir issues.

## Licença

O projeto será licenciado sob a licença [MIT](LICENSE).

## Conclusão

O projeto foi desenvolvido com o objetivo de praticar e aprimorar as habilidades e conhecimentos em Python, bem como a criação de uma ferramenta utíl para cálculos matemáticos de área e volume.
Pretendo em um futuro próximo expandir o projeto, criando mais cálculos e transformando em uma API para uso externo.
