````markdown
# 📘 Exercícios de Funções em Python  

📌 **Objetivo**  
Este repositório contém exercícios práticos em **Python** desenvolvidos para fins acadêmicos no **programa de qualificação da Softex PE**.  

Os exercícios exploram a criação e utilização de funções em Python, passando por funções simples, parâmetros opcionais, uso de `*args`, `**kwargs`, funções internas e funções passadas como parâmetros.  

---

## 📑 Índice

1. [Saudação](#1️⃣-saudação)  
2. [Dobro de um número](#2️⃣-dobro-de-um-número)  
3. [Soma de dois números](#3️⃣-soma-de-dois-números)  
4. [Mensagem personalizada](#4️⃣-mensagem-personalizada)  
5. [Operações (soma, subtração e multiplicação)](#5️⃣-operações-soma-subtração-e-multiplicação)  
6. [Média de vários números](#6️⃣-média-de-vários-números)  
7. [Dados pessoais com **kwargs](#7️⃣-dados-pessoais-com-kwargs)  
8. [Calculadora com funções internas](#8️⃣-calculadora-com-funções-internas)  
9. [Aplicar operação recebida como parâmetro](#9️⃣-aplicar-operação-recebida-como-parâmetro)  

---

## 📝 Exercícios

### 1️⃣ Saudação  
```python
def saudacao():
    print("Olá, bem-vindo ao Python!")

saudacao()
````

✅ Saída:

```
Olá, bem-vindo ao Python!
```

---

### 2️⃣ Dobro de um número

```python
def dobro(numero):
    return numero * 2

print(dobro(5))   # 10
print(dobro(10))  # 20
```

---

### 3️⃣ Soma de dois números

```python
def soma(a, b):
    return a + b

print(soma(10, 20))  # 30
```

---

### 4️⃣ Mensagem personalizada

```python
def mensagem(nome="visitante"):
    print(f"Olá, {nome}!")

mensagem("Gabriel")   # Olá, Gabriel!
mensagem()            # Olá, visitante!
```

---

### 5️⃣ Operações (soma, subtração e multiplicação)

```python
def operacoes(a, b):
    return a + b, a - b, a * b

soma_, sub_, mult_ = operacoes(10, 5)
print("Soma:", soma_)           # 15
print("Subtração:", sub_)       # 5
print("Multiplicação:", mult_)  # 50
```

---

### 6️⃣ Média de vários números

```python
def media(*numeros):
    return sum(numeros) / len(numeros)

print(media(3, 5, 7))                # 5.0
print(media(10, 20, 30, 40, 50))     # 30.0
```

---

### 7️⃣ Dados pessoais com \*\*kwargs

```python
def dados_pessoais(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

dados_pessoais(nome="Ana", idade=25, cidade="Recife")
```

✅ Saída:

```
nome: Ana
idade: 25
cidade: Recife
```

---

### 8️⃣ Calculadora com funções internas

```python
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

print(calculadora(10, 5, "soma"))          # 15
print(calculadora(10, 5, "subtracao"))     # 5
print(calculadora(10, 5, "multiplicacao")) # 50
print(calculadora(10, 5, "divisao"))       # 2.0
```

---

### 9️⃣ Aplicar operação recebida como parâmetro

```python
def aplicar_operacao(a, b, funcao):
    return funcao(a, b)

def soma(a, b): return a + b
def multiplicar(a, b): return a * b

print(aplicar_operacao(3, 4, soma))        # 7
print(aplicar_operacao(3, 4, multiplicar)) # 12
```

---

## 📚 Tecnologias utilizadas

* Python 3.x

---

## 📌 Considerações finais

Este material foi desenvolvido para **prática acadêmica**, como parte das atividades do **programa de qualificação da Softex PE**.


---
