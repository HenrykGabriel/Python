# -*- coding: utf-8 -*-
import os
import math
import random


def calculadora():
    os.system("cls")

    print("CALCULADORA")

    print("\nOPERAÇÕES")
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
    
    input("\nPressione Enter para voltar ao menu...")
    main()



def triangulos():
    os.system("cls")

    print("TIPOS DE TRIÂNGULOS")

    lado1 = float(input("\nDigite o tamanho do lado 1: "))
    lado2 = float(input("Digite o tamanho do lado 2: "))
    lado3 = float(input("Digite o tamanho do lado 3: "))

    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:

        os.system("cls")

        if lado1 == lado2 == lado3:
            print("Esse triângulo é equilátero!")
        elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
            print("Esse triângulo é isósceles!")
        else:
            print("Esse triângulo é escaleno!")
    else:
        input("\nImpossível formar um triângulo! Pressione Enter para voltar ao menu...")
        main()

    input("Pressione enter para voltar ao menu...")
    main()


def hipotenusa():
    os.system("cls")

    print("HIPOTENUSA")

    print("\n1) Você tem dois catetos")
    print("2) Você tem um cateto e a hipotenusa")
    opcao = int(input(f"\nEscolha sua opção: "))

    if opcao == 1:
        os.system("cls")

        cateto1 = float(input("Qual o comprimento do primeiro cateto: "))
        cateto2 = float(input("Qual o comprimento do segundo cateto: "))

        resultado = math.pow(cateto1, 2) + math.pow(cateto2, 2)

        hipotenusa = math.sqrt(resultado)

        print(f"\nA hipotenusa é {hipotenusa}")
    elif opcao == 2:
        os.system("cls")

        hipotenusa = float(input("Qual o comprimento da hipotenusa: "))
        cateto = float(input("Qual o comprimento do cateto: "))

        resultado = math.pow(hipotenusa, 2) - math.pow(cateto, 2)

        cateto_desconhecido = math.sqrt(resultado)

        print(f"\nO valoe do cateto desconhecido é {cateto_desconhecido}")
    else:
        input("\nOpção inválida, pressione enter para voltar ao menu...")
        main()
    
    input("\nPressione enter para voltar ao menu...")
    main()


def media():
    os.system("cls")

    print("MÉDIA COM MENÇÃO")

    nota1 = float(input("\nDigite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

    if (nota1 <= 10 or nota1 > 0 or
    nota2 <= 10 or nota2 > 0 or
    nota3 <= 10 or nota3 > 0 or
    nota4 <= 10 or nota4 > 0):
        
        os.system("cls")

        media = (nota1 + nota2 + nota3 + nota4) / 4

        if media >= 9:
            print(f"Sua média foi {media} e sua menção foi MB")
        elif media >= 7 and media < 9:
            print(f"Sua média foi {media} e sua menção foi B")
        elif media >= 5 and media < 7:
            print(f"Sua média foi {media} e sua menção foi R")
        else:
            print(f"Sua média foi {media} e sua menção foi I")

    else:
        input("\nOpção inválida, pressione enter para voltar ao menu...")
        main()

    input("\nPressione enter para voltar ao menu...")
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
            calculadora()
        elif opcao == "2":
            triangulos()
        elif opcao == "3":
            hipotenusa()
        elif opcao == "4":
            media()
        elif opcao == "5":
            print("Saindo do programa... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
