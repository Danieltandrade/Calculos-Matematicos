"""
Este projeto foi desenvolvido com o intuito de facilitar os cálculos matemáticos de área e volume.
"""

from log import log
from src import Area
from src import Volume

import getpass

def calculo_area(opcao_area) -> None:
    """
    Função para o cálculo de área.
    Opções de cálculo:
        1 -> Área do Retângulo
        2 -> Área do Triângulo
        3 -> Área da Circunferência

    Args:
        opcao_area (str): Opção escolhida pelo usuário
    """

    match opcao_area:
        case '1': # Área do Retângulo
            base = float(input("Digite o valor da base: "))
            altura = float(input("Digite o valor da altura: "))
            area = Area(base, altura)
            resultado = area.retangulo()
            log("INFO", getpass.getuser(), "Area do Retangulo", resultado)
            print(f"A area do retângulo e: {resultado}cm²")
        case '2': # Área do Triângulo
            base = float(input("Digite o valor da base: "))
            altura = float(input("Digite o valor da altura: "))
            area = Area(base, altura)
            resultado = area.triangulo()
            log("INFO", getpass.getuser(), "Area do Triangulo", resultado)
            print(f"A area do triângulo e: {resultado}cm²")
        case '3': # Área da Circunferência
            raio = float(input("Digite o valor do raio: "))
            area = Area(raio, 0)
            resultado = area.circunferencia()
            log("INFO", getpass.getuser(), "Area da Circunferencia", resultado)
            print(f"A area da circunferência e: {resultado}cm²")
        case _:
            resultado = "None"
            log("WARNING", getpass.getuser(), "Nenhum calculo realizado", resultado)
            print("Opção inválida. Por favor, escolha uma opção válida.")

def calculo_volume(opcao_volume) -> None:
    """
    Função para o cálculo de volume.
    Opções de cálculo:
        1 -> Volume do Cilindro
        2 -> Volume do Cubo
        3 -> Volume da Esfera
        4 -> Volume do Paralelepipedo
        5 -> Volume do Piramede Retangular
        6 -> Volume da Piramide Triangular
        7 -> Volume do Prisma Triangular

    Args:
        opcao_volume (str): Opção escolhida pelo usuário
    """
    match opcao_volume:
        case '1': # Volume do Cilindro
            raio = float(input("Digite o valor do raio: "))
            altura = float(input("Digite o valor da altura: "))
            volume = Volume(raio, altura, 0)
            resultado = volume.cilindro()
            log("INFO", getpass.getuser(), "Volume do Cilindro", resultado)
            print(f"O volume do cilindro e: {resultado}cm³")
        case '2': # Volume do Cubo
            lado = float(input("Digite o valor de um lado: "))
            volume = Volume(lado, 0, 0)
            resultado = volume.cubo()
            log("INFO", getpass.getuser(), "Volume do Cubo", resultado)
            print(f"O volume do cubo e: {resultado}cm³")
        case '3': # Volume do Esfera
            raio = float(input("Digite o valor do raio: "))
            volume = Volume(raio, 0, 0)
            resultado = volume.esfera()
            log("INFO", getpass.getuser(), "Volume da Esfera", resultado)
            print(f"O volume da esfera e: {resultado}cm³")
        case '4': # Volume do Paralelepipedo
            base = float(input("Digite o valor da base: "))
            altura = float(input("Digite o valor da altura: "))
            profundidade = float(input("Digite o valor da profundidade: "))
            volume = Volume(base, altura, profundidade)
            resultado = volume.paralelepipedo()
            log("INFO", getpass.getuser(), "Volume do Paralelepipedo", resultado)
            print(f"O volume do paralelepipedo e: {resultado}cm³")
        case '5': # Volume da Piramide Retangular
            base = float(input("Digite o valor da base: "))
            profundidade = float(input("Digite o valor da profundidade: "))
            altura = float(input("Digite o valor da altura: "))
            volume = Volume(base, altura, profundidade)
            resultado = volume.piramide_retangular()
            log("INFO", getpass.getuser(), "Volume da Piramide Retangular", resultado)
            print(f"O volume da piramide retangular e: {resultado}cm³")
        case '6': # Volume da Piramide Triangular
            base = float(input("Digite o valor da base: "))
            profundidade = float(input("Digite o valor da profundidade: "))
            altura = float(input("Digite o valor da altura: "))
            volume = Volume(base, altura, profundidade)
            resultado = volume.piramide_triangular()
            log("INFO", getpass.getuser(), "Volume da Piramide Triangular", resultado)
            print(f"O volume da piramide triangular e: {resultado}cm³")
        case '7': # Volume do Prisma Triangular
            base = float(input("Digite o valor da base: "))
            profundidade = float(input("Digite o valor da profundidade: "))
            altura = float(input("Digite o valor da altura: "))
            volume = Volume(base, altura, profundidade)
            resultado = volume.prisma_triangular()
            log("INFO", getpass.getuser(), "Volume do Prisma Triangular", resultado)
            print(f"O volume do prisma triangular e: {resultado}cm³")
        case _:
            resultado = "None"
            log("WARNING", getpass.getuser(), "Nenhum calculo realizado", resultado)
            print("Opção inválida. Por favor, escolha uma opção válida.")

def main() -> None:
    """
    Função principal utilizada para executar o programa.
    Opções de cálculo:
        1 -> Área
        2 -> Volume
        3 -> Sair
    """
    print("Calculadora de Área e Volume")
    try:
        while True:
            print("\nEscolha uma opção abaixo:")
            print("1 -> Área")
            print("2 -> Volume")
            print("3 -> Sair")

            opcao = input("Digite a opção desejada: ")
            match opcao:
                case '1':
                    print("Escolha uma opção abaixo:")
                    print("1 -> Área do Retângulo")
                    print("2 -> Área do Triângulo")
                    print("3 -> Área da Circunferência")
                    opcao_area = input("Digite a opção desejada: ")
                    calculo_area(opcao_area)
                case '2':
                    print("Escolha uma opção abaixo:")
                    print("1 -> Volume do Cilindro")
                    print("2 -> Volume do Cubo")
                    print("3 -> Volume da Esfera")
                    print("4 -> Volume do Paralelepipedo")
                    print("5 -> Volume da Piramide Retangular")
                    print("6 -> Volume da Piramide Triangular")
                    print("7 -> Volume do Prisma Triangular")
                    opcao_volume = input("Digite a opção desejada: ")
                    calculo_volume(opcao_volume)
                case '3':
                    print("Saindo do programa...")
                    break
                case _:
                    log("WARNING", getpass.getuser(), "Opcao de calculo invalida", "Novo Loop de Calculo!")
                    print("Opção inválida. Por favor, escolha uma opção válida.")
            resultado = "Area" if opcao == '1' else "Volume" if opcao == '2' else "Saindo..."
            log("INFO", getpass.getuser(), f"Opcao Selecionada: {opcao}!", f"{resultado}")
    except KeyboardInterrupt as e:
        log("ERROR", getpass.getuser(), "Erro na função main", f"{e}")

if __name__ == '__main__':
    main()
