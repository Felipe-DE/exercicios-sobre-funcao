# 1 - Função saudacao
def saudacao():
    print("Olá, bem-vindo ao Python!")

saudacao()


# 2 - Função dobro
def dobro(numero):
    return numero * 2

print(dobro(5))
print(dobro(10))
print(dobro(7))


# 3 - Função soma
def soma(a, b):
    return a + b

print(soma(10, 20))


# 4 - Função mensagem
def mensagem(nome="visitante"):
    print(f"Olá, {nome}!")

mensagem("Gabriel")
mensagem()


# 5 - Função operacoes
def operacoes(a, b):
    return a + b, a - b, a * b

soma_, sub_, mult_ = operacoes(10, 5)
print("Soma:", soma_)
print("Subtração:", sub_)
print("Multiplicação:", mult_)


# 6 - Função media
def media(*numeros):
    return sum(numeros) / len(numeros)

print(media(3, 5, 7))
print(media(10, 20, 30, 40, 50))
print(media(1, 2, 3, 4, 5, 6, 7))


# 7 - Função dados_pessoais
def dados_pessoais(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

dados_pessoais(nome="Ana", idade=25, cidade="Recife")
dados_pessoais(nome="Gabriel", idade=31, cidade="São Paulo", curso="Engenharia de Software")


# 8 - Função calculadora com funções internas
def calculadora(a, b, operacao):
    def somar(x, y): return x + y
    def subtrair(x, y): return x - y
    def multiplicar(x, y): return x * y
    def dividir(x, y): return x / y if y != 0 else "Erro: divisão por zero"

    if operacao == "soma":
        return somar(a, b)
    elif operacao == "subtracao":
        return subtrair(a, b)
    elif operacao == "multiplicacao":
        return multiplicar(a, b)
    elif operacao == "divisao":
        return dividir(a, b)
    else:
        return "Operação inválida!"

print(calculadora(10, 5, "soma"))
print(calculadora(10, 5, "subtracao"))
print(calculadora(10, 5, "multiplicacao"))
print(calculadora(10, 5, "divisao"))


# 9 - Função aplicar_operacao
def aplicar_operacao(a, b, funcao):
    return funcao(a, b)

def soma(a, b): return a + b
def multiplicar(a, b): return a * b

print(aplicar_operacao(3, 4, soma))
print(aplicar_operacao(3, 4, multiplicar))
