# -*- coding: utf-8 -*-
import os
import math
import random


def calculadora():
    os.system("cls")

    print("OPERAÇÕES")
    print("\n1) Adição")
    print("2) Subtração")
    print("3) Multiplicação")
    print("4) Divisão")
    print("5) Potência")
    print("6) Raiz quadrada")

    op = int(input("\nQual opção voçê deseja? "))

    if op in [1, 2, 3, 4, 5]:
        os.system("cls")
        
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if op == 1:
            soma = num1 + num2
            print(f"\n{num1} + {num2} = {soma}")
        elif op == 2:
            sub = num1 - num2
            print(f"\n{num1} - {num2} = {sub}")
        elif op == 3:
            mult = num1 * num2
            print(f"\n{num1} * {num2} = {mult}")
        elif op == 4:
            div = num1 / num2
            print(f"\n{num1} / {num2} = {div}")
        else:
            potencia = num1 ** num2
            print(f"\n{num1} ^ {num2} = {potencia}")
    elif op == 6:
        os.system("cls")

        num = float(input("\nDigite o número da raiz: "))

        raiz = math.sqrt(num)

        print(f"\nA raiz quadrada de {num} é {raiz}")

    else:
        input("\nOpção inválida! Pressione Enter para voltar ao menu...")
        main() 


def triangulos():
    os.system("cls")

    lado1 = float(input("Digite o tamanho do lado 1: "))
    lado2 = float(input("Digite o tamanho do lado 2: "))
    lado3 = float(input("Digite o tamanho do lado 3: "))

    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:

        if lado1 == lado2 == lado3:
            print("Esse triângulo é equilátero!")
        elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
            print("Esse triângulo é isósceles!")
        else:
            print("Esse triângulo é escaleno!")
    else:
        input("\nImpossível formar um triângulo! Pressione Enter para voltar ao menu...")
        main()


        

def main():

    while True:
        os.system("cls")

        print("╔═══ MENU DE OPERAÇÕES ════╗")
        print("║  1. Calculadora          ║")
        print("║  2. Tipos de triângulos  ║")
        print("║  3. Hipotenusa           ║")
        print("║  4. Média com menção     ║")
        print("║  5. Tabuada              ║")
        print("║  6. Equação de 2° grau   ║")
        print("║  7. Jogo de advinhação   ║")
        print("║  8. Nome e Sobrenome     ║")
        print("║  9. Sair                 ║")
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
