import math
import os

print("Calculadora Científica - Escolha a operação:")
print("1. Seno")
print("2. Cosseno")
print("3. Tangente")
print("4. Raiz Quadrada")
print("5. Logaritmo")
print("6. Potência")
print("7. Fatorial")
print("8. Valor da constante Pi: π")
print("9. Valor da constante Euler: e")
opcao = input("Digite o número da operação desejada (1/2/3/4/5/6/7/8/9): ")

# Limpa a tela para melhor visualização do resultado
os.system('cls' if os.name == 'nt' else 'clear')

#Usar função para fazer as operações
def seno(grau):
    resultado = math.sin(math.radians(grau))
    return resultado

def cosseno(grau):
    resultado = math.cos(math.radians(grau))
    return resultado

def tangente(grau):
    resultado = math.tan(math.radians(grau))
    return resultado

def raiz_quadrada(numero):
    resultado = math.sqrt(numero)
    return resultado

def logaritmo(x, base):
    resultado = math.log(x, base)
    return resultado

def potencia(base, expoente):
    resultado = math.pow(base, expoente)
    return resultado

def fatorial(numero):
    resultado = math.factorial(numero)
    return resultado

def valor_pi():
    return math.pi

def valor_euler():
    return math.e


if opcao == '1':
    grau = float(input("Digite o ângulo em graus: "))
    print("Resultado:", seno(grau))   
elif opcao == '2':
    grau = float(input("Digite o ângulo em graus: "))
    print("Resultado:", cosseno(grau))
elif opcao == '3':
    grau = float(input("Digite o ângulo em graus: "))
    print("Resultado:", tangente(grau))
elif opcao == '4':
    numero = float(input("Digite o número: "))
    print("Resultado:", raiz_quadrada(numero))
elif opcao == '5':
    x = float(input("Digite o número: "))
    base = float(input("Digite a base: "))
    print("Resultado:", logaritmo(x, base))
elif opcao == '6':
    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))
    print("Resultado:", potencia(base, expoente))
elif opcao == '7':
    numero = int(input("Digite o número inteiro: "))
    print("Resultado:", fatorial(numero))
elif opcao == '8':
    print("Resultado:", valor_pi())
elif opcao == '9':
    print("Resultado:", valor_euler())
else:
    print("Opção inválida. Por favor, escolha uma operação válida (1/2/3/4/5/6/7/8/9).")