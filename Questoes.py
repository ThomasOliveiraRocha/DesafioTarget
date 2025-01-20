import json

# 1) Soma dos números inteiros de 1 até 13
def soma_inteiros():
    indice = 13
    soma = 0
    k = 0
    while k < indice:
        k += 1
        soma += k
    return soma

# 2) Verificar se o número pertence à sequência de Fibonacci
def verifica_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero

# 3) Calcular o menor, maior faturamento e dias acima da média
def calcular_faturamento():
    faturamento_json = '''
    {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    '''
    faturamento = json.loads(faturamento_json)
    total_faturamento = sum(faturamento.values())
    media_faturamento = total_faturamento / len(faturamento)
    menor_faturamento = min(faturamento.values())
    maior_faturamento = max(faturamento.values())
    dias_acima_media = sum(1 for valor in faturamento.values() if valor > media_faturamento)
    return menor_faturamento, maior_faturamento, dias_acima_media

# 4) Calcular o percentual de cada estado no faturamento
def percentual_estado():
    faturamento_estado = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    faturamento_total = sum(faturamento_estado.values())
    percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_estado.items()}
    return percentuais

# 5) Inverter a string
def inverter_string(s):
    return s[::-1]

# Função principal para chamar todas as outras funções
def main():
    print("Olá! Vamos começar com os cálculos e verificações.")

    # 1) Soma dos números de 1 até 13
    soma = soma_inteiros()
    print(f"\n1) A soma dos números de 1 até 13 é: {soma}")

    # 2) Verificar se número pertence à Fibonacci
    numero = int(input("\n2) Digite um número para saber se ele faz parte da sequência de Fibonacci: "))
    if verifica_fibonacci(numero):
        print(f"Sim, o número {numero} faz parte da sequência de Fibonacci!")
    else:
        print(f"Não, o número {numero} não está na sequência de Fibonacci.")

    # 3) Resultados do faturamento
    menor_faturamento, maior_faturamento, dias_acima_media = calcular_faturamento()
    print(f"\n3) Sobre o faturamento mensal:\n"
          f"  - O menor faturamento foi de R${menor_faturamento:.2f}\n"
          f"  - O maior faturamento foi de R${maior_faturamento:.2f}\n"
          f"  - Houve {dias_acima_media} dias com faturamento acima da média.")

    # 4) Percentuais de participação de cada estado
    percentuais = percentual_estado()
    print("\n4) Percentual de participação de cada estado no faturamento total:")
    for estado, percentual in percentuais.items():
        print(f"  - {estado}: {percentual:.2f}%")

    # 5) Inverter a string
    string = input("\n5) Digite uma string para inverter: ")
    print(f"  A string invertida é: {inverter_string(string)}")

# Chama a função principal
if __name__ == "__main__":
    main()
