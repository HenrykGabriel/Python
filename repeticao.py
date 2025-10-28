# -*- coding: utf-8 -*-

import os

while True:
    os.system("cls")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("\nDigite o segundo número: "))

    resultado = num1 * num2

    print(f"\nA multiplicação de {num1} x {num2} é {resultado}")

    continuar = input("\nDeseja continuar? (s/n): ").strip().lower()

    if continuar != 's':
        print("\nPrograma encerrado")
        break

print("-" * 40)