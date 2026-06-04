import os

print("Calculadora Simples  - Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = input("Digite o número da operação desejada (1/2/3/4): ")

os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela para melhor visualização do resultado

if opcao == '1':
    print("Você escolheu Adição.")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print(f"O resultado da adição é: {resultado}")
elif opcao == '2':
    print("Você escolheu Subtração.")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif opcao == '3': 
    print("Você escolheu Multiplicação.")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif opcao == '4':
    print("Você escolheu Divisão.")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Opção inválida. Por favor, escolha uma operação válida (1/2/3/4).")  