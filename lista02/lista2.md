
# MC102 - Algoritmos e Programação de Computadores

## Lista de Exercícios 2

### Exercício 1
Considere o seguinte menu:

1. Pizza Marguerita  
2. Pizza de Calabresa  
3. Pizza de Pepperoni  
4. Pizza de Mussarela  
5. Sair  

O programa deve: imprimir o menu; ler um número de 1 até 5; e imprimir a opção correspondente ao número lido. Isso deve ser repetido até que o usuário selecione a opção 5.

---

### Exercício 2
Faça um programa que leia um número `n`. Após isso, o programa deve ler uma sequência de `n` números e imprimir uma mensagem indicando se a sequência lida está ordenada de forma crescente ou não.

---

### Exercício 3
Faça um programa que leia dois números `m` e `n`. O programa deve imprimir o Máximo Divisor Comum (MDC) dos números `m` e `n`, utilizando o Algoritmo de Euclides:

- mdc(m, n) = m, se n = 0;  
- mdc(m, n) = mdc(n, m % n), se n > 0.

---

### Exercício 4
Escreva um programa que leia um número `n`. O programa deve imprimir o menor número primo maior ou igual a `n` e o maior número primo menor ou igual a `n`.

---

### Exercício 5
O que será impresso pelo programa abaixo? Assuma que o valor de `D` é o último dígito do seu RA.

```python
x = 5 + D
y = 0
while True:
    y = (x % 2) + 10 * y
    x = x // 2
    print('x =', x, 'y =', y)
    if x == 0:
        break

while y != 0:
    x = y % 100
    y = y // 10
    print('x =', x, 'y =', y)
```

---

### Exercício 6
Escreva um programa que leia `n` números inteiros e imprima quantos deles estão nos seguintes intervalos:  
- `[0, 25]`
- `[26, 50]`
- `[51, 75]`
- `[76, 100]`

Exemplo: Para `n = 10` e os números `{2, 61, -1, 0, 88, 55, 3, 121, 25, 75}`, o programa deve imprimir:  
- `[0, 25]: 4`  
- `[26, 50]: 0`  
- `[51, 75]: 3`  
- `[76, 100]: 1`

---

### Exercício 7
Escreva um programa para computar a raiz quadrada de um número positivo utilizando o método de Newton. O programa deve imprimir o valor da vigésima aproximação. Fórmula:  

\[ x_{n+1} = x_n - rac{f(x_n)}{f'(x_n)} \]

---

### Exercício 8
Aponte os erros no código abaixo, que deveria calcular o fatorial de um número inteiro não negativo:

```python
valor = int(input("Digite um número: "))
fatorial = n = valor

if n >= 0:
    while n > 0:
        n = n - 1
        fatorial = fatorial * n

print("O fatorial de", valor, "é igual a:", fatorial)
print("Não existe fatorial de", valor)
```

---

### Exercício 9
Faça um programa que leia um número inteiro positivo `C`. O programa deve imprimir todas as soluções da equação:  
\[ x_1 + x_2 + x_3 = C \]  
onde as variáveis \( x_1, x_2, x_3 \) são inteiras não negativas.

---

### Exercício 10
Faça um programa que leia um número na base decimal e o imprima na base binária.

---

### Exercício 11
Faça um programa que leia um número inteiro positivo `n` e imprima `n` linhas no formato abaixo (exemplo para `n = 6`):

```
1
2
3
4
5
6
```

---

### Exercício 12
Faça um programa que leia um número `n` e imprima `n` linhas no formato abaixo (exemplo para `n = 6`):

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
```

---

### Exercício 13
Faça um programa que leia um número `n` e imprima `n` linhas no formato abaixo (exemplo para `n = 6`):

```
+ * * * * *
* + * * * *
* * + * * *
* * * + * *
* * * * + *
* * * * * +
```

---

### Exercício 14
Um jogador da Mega-Sena só faz jogos onde os números são alternados entre par e ímpar. Faça um programa que imprima todas as combinações possíveis de jogos com essa regra.

```
Exemplo: [2, 3, 4, 5, 6, 7]
```
