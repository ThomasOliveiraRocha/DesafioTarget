# Desafio de Computação - Target
Nome: Thomas Oliveira Rocha Sampaio Silva

Este repositório contém a solução para um desafio de computação solicitado pela empresa Target. O objetivo foi desenvolver soluções para problemas de programação. Abaixo estão os detalhes e requisitos de cada um dos problemas.

______________________________________________________________________________
## 1) Soma dos Números Inteiros

Observe o trecho de código abaixo:

```c
int INDICE = 13, SOMA = 0, K = 0;
while (K < INDICE) {
    K = K + 1;
    SOMA = SOMA + K;
}
printf("%d", SOMA);
```
Ao final do processamento, qual será o valor da variável SOMA?
______________________________________________________________________________
## 2) Sequência de Fibonacci
Dado a sequência de Fibonacci, onde se inicia por 0 e 1, e o próximo valor sempre será a soma dos dois valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa que, ao ser informado um número, calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não à sequência.

#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código.
______________________________________________________________________________
## 3) Cálculo de Faturamento Diário
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa que calcule e retorne:

O menor valor de faturamento ocorrido em um dia do mês.
O maior valor de faturamento ocorrido em um dia do mês.
O número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
# IMPORTANTE:

Usar o JSON ou XML disponível como fonte dos dados do faturamento mensal.
Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média.
______________________________________________________________________________
## 4) Cálculo de Percentual de Faturamento por Estado
Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53
Escreva um programa que calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
______________________________________________________________________________
## 5) Inversão de String
Escreva um programa que inverta os caracteres de uma string.

# IMPORTANTE:

A string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código.
Evite usar funções prontas, como, por exemplo, reverse.
______________________________________________________________________________
