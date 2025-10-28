# -*- coding: utf-8 -*-

import os

os.system("cls")

num = int(input("Digite o número da sua tabuada: "))
comeco = int(input("Digite o valor inicial da contagem: "))
fim = int(input("Digite o valor final da contagem: "))

for i in range(comeco, fim + 1):
    print(f"{num} x {i} = {num * i}")

print("\nFim da repetição!")