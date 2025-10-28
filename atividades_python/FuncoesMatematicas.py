# -*- coding: utf-8 -*-
import os
import math
import random

os.system("cls")

def raiz_quadrada():
    os.system("cls")

    num = float(input("Digite o número da raiz quadrada: "))

    if num < 0:
        print("Não é possível calcular  raíz quadrada de número negativo.")
    
    else:
        resultado = math.sqrt(num)
        print(f"A raiz quadrada de {num} é {resultado}")

    input("\nPressione Enter para continuar...")


def potencia():
    os.system("cls")

    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))

    resultado = math.pow(base, expoente)

    print(f"{base} elevado a {expoente} = {resultado}")

    input("\nPressione Enter para continuar...")

def numero_aleatorio():
    os.system("cls")

    inicio = int(input("Digite o valor inicial do intervalo: "))
    fim = int(input ("Digite o valor final do intervalo: "))

    if inicio > fim:
        print("O valor inicial deve ser menor ou igual ao valor final.")
    else:
        num = random.randint(inicio, fim)
        print(f"Número aleatório gerado entre {inicio} e {fim}: {num}")

    input("\nPressione Enter para continuar...")

def calculos():
    os.system("cls")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    potencia = math.pow(num1, num2)

    print(f"\n{num1} + {num2} = {soma}")

    print(f"\n{num1} - {num2} = {subtracao}")

    print(f"\n{num1} * {num2} = {multiplicacao}")

    if num2 == 0:
        print("\nA divisão não pode ser feita")
    else:
        divisao = num1 / num2
        print(f"\n{num1} / {num2} = {divisao}")

    print(f"\n{num1} ^ {num2} = {potencia}")

    input("\nPressione Enter para continuar...")
    

def main():

    while True:
        os.system("cls")

        print("╔═══ MENU DE OPERAÇÕES ════╗")
        print("║  1. Raiz quadrada        ║")
        print("║  2. Potência             ║")
        print("║  3. Número aleatório     ║")
        print("║  4. Calculos             ║")
        print("║  5. Sair                 ║")
        print("╚══════════════════════════╝")

        opcao = input("Escolha uma opção: ") 

        if opcao == "1":
            raiz_quadrada()
        elif opcao == "2":
            potencia()
        elif opcao == "3":
            numero_aleatorio()
        elif opcao == "4":
            calculos()
        elif opcao == "5":
            print("Saindo do programa... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

