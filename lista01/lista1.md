# MC102 - Algoritmos e Programação de Computadores

## Lista de Exercícios 1

1. Responda qual tipo de objeto deve ser usado para armazenar cada uma das seguintes informações:

    - a. A idade de uma pessoa.
        - Inteiro
    - b. A área do seu quintal em metros quadrados.
        - Ponto flutuante
    - c. A média da quantidade de chuva no mês de fevereiro.
        - Ponto flutuante
    - d. O número de estrelas na galáxia.
        - Inteiro

2. Considere o trecho de código abaixo:

   ```python
   a = 10 # a vale 10
   b = a # b vale 10
   c = 9 # c vale 9
   d = c # d vale 9
   c = c + 1 # c vale 10
   ```

   Após a execução desse trecho de código, qual será o valor armazenado em cada variável?

3. Faça um programa que leia um número ponto flutuante `x` e calcule o valor de `f(x) = √x + (x/2) + x * x`.  
   (Dica: √x = x^(1/2)).

   ```python
   x = float(input())
   
   f_x = x ** 0.5 + (x / 2) + x ** x
   
   print("O valor para f(x) é: ", f_x.__round__(2))
   ```


4. Faça um programa que leia dois valores inteiros nas variáveis `x` e `y` e troque o conteúdo das variáveis.  
   Por exemplo, supondo que `x = 2` e `y = 10` foram os valores lidos, o seu programa deve fazer com que `x = 10` e
   `y = 2`.  
   Refaça este problema usando apenas `x` e `y` como variáveis.

5. Faça um programa que leia os valores correspondentes aos três lados `a`, `b` e `c` de um triângulo.  
   O programa então deve determinar se o triângulo é isósceles, escaleno ou equilátero, informando isto para o usuário,
   e em seguida o programa deve imprimir a área `A` do triângulo utilizando a fórmula de Heron:

   ```markdown
   A = √(s(s−a)(s−b)(s−c))
   ```

   onde

   ```markdown
   s = (a + b + c) / 2
   ```

6. Considere um programa que deve classificar um número como par ou ímpar e, além disso, classificar ele como menor do
   que
   100 ou maior ou igual a 100. A solução abaixo faz essa classificação de maneira correta?

   ```python
   print("Digite um número:")
   a = int(input())
   if a % 2 == 0 and a < 100:
       print("O número é par e menor do que 100")
   else:
       if a >= 100:
           print("O número é par e maior ou igual que 100")
       if a % 2 != 0 and a < 100:
           print("O número é ímpar e menor do que 100")
       else:
           if a >= 100:
               print("O número é ímpar e maior ou igual que 100")
   ```

7. Faça um programa que leia um caractere `‘F’` ou `‘C’`, que indica se o próximo valor corresponde à temperatura em
   Fahrenheit ou Celsius.
   Em seguida, o programa deve ler o valor da temperatura e então imprimir o valor correspondente à temperatura na outra
   unidade de medida.  
   Observação: C = 5/9 * (F - 32)

8. Faça um programa que leia um ano (valor inteiro) e imprima se ele é bissexto ou não.  
   Observação: um ano é bissexto se ele é múltiplo de 400, ou se ele é múltiplo de 4 mas não é múltiplo de 100.

9. Suponha que uma pessoa possa se aposentar pelo INSS caso atenda alguma das situações abaixo:

    - É do sexo masculino, possui pelo menos 65 anos e pelo menos 10 anos de contribuição.
    - É do sexo masculino, possui pelo menos 63 anos e pelo menos 15 anos de contribuição.
    - É do sexo feminino, possui pelo menos 63 anos e pelo menos 10 anos de contribuição.
    - É do sexo feminino, possui pelo menos 61 anos e pelo menos 15 anos de contribuição.

   Crie um programa que leia um caractere (`‘M’` ou `‘F’`), que representa o sexo de um indivíduo, e dois inteiros, que
   representam a idade e
   o tempo de contribuição. O programa deverá então imprimir “Aposentável” se o indivíduo atenda uma das situações
   acima. Caso contrário, o programa deverá imprimir “Não Aposentável”.

10. Faça um programa que leia dois números e em seguida um caracter que representa um operador aritmético (`‘+’`, `‘−’`,
    `‘∗’` ou `‘/’`).
    Seu programa então deve imprimir o resultado do operador aplicado aos dois números dados.
