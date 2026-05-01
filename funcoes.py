
import random


def rolar_dados(numero_dados):
    lista = []
    i = 0
    while i < numero_dados:
        resultado = random.randint(1, 6)
        lista.append(resultado)
        i += 1
    return lista


def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dados_rolados_final = []
    valor_guardado = dados_rolados[dado_para_guardar]

    i = 0
    while i < len(dados_rolados):
        if i != dado_para_guardar:
            dados_rolados_final.append(dados_rolados[i])
        i += 1

    dados_no_estoque.append(valor_guardado)

    return [dados_rolados_final, dados_no_estoque]


def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    if dado_para_remover < len(dados_no_estoque):
        dados_rolados.append(dados_no_estoque[dado_para_remover])
        del dados_no_estoque[dado_para_remover]

    return [dados_rolados, dados_no_estoque]


def calcula_pontos_regra_simples(dados_rolados):
    dicionario_pontos_simples = {}

    for numero in range(1, 7):
        dicionario_pontos_simples[numero] = 0

    for i in range(len(dados_rolados)):
        dicionario_pontos_simples[dados_rolados[i]] += dados_rolados[i]

    return dicionario_pontos_simples


def calcula_pontos_soma(dados_rolados):
    soma = 0
    for dado in dados_rolados:
        soma += dado
    return soma


def calcula_pontos_sequencia_baixa(dados_rolados):
    for n in [1, 2, 3]:
        if n in dados_rolados and n + 1 in dados_rolados and n + 2 in dados_rolados and n + 3 in dados_rolados:
            return 15
    return 0


def calcula_pontos_sequencia_alta(dados_rolados):
    for n in [1, 2]:
        if n in dados_rolados and n + 1 in dados_rolados and n + 2 in dados_rolados and n + 3 in dados_rolados and n + 4 in dados_rolados:
            return 30
    return 0


def calcula_pontos_full_house(dados_rolados):
    dicio_full_house = {}

    for num in dados_rolados:
        if num in dicio_full_house:
            dicio_full_house[num] += 1
        else:
            dicio_full_house[num] = 1

    for num in range(1, 7):
        if num not in dados_rolados:
            dicio_full_house[num] = 0

    valores = list(dicio_full_house.values())
    soma = 0

    if 2 in valores and 3 in valores:
        for num, valor in dicio_full_house.items():
            if valor == 2 or valor == 3:
                soma += num * valor

    return soma


def calcula_pontos_quadra(dados):
    i = 1

    while i <= 6:
        contador = 0
        j = 0

        while j < len(dados):
            if dados[j] == i:
                contador += 1
            j += 1

        if contador >= 4:
            soma = 0
            k = 0

            while k < len(dados):
                soma += dados[k]
                k += 1

            return soma

        i += 1

    return 0


def calcula_pontos_quina(dados):
    i = 1

    while i <= 6:
        contador = 0
        j = 0

        while j < len(dados):
            if dados[j] == i:
                contador += 1
            j += 1

        if contador >= 5:
            return 50

        i += 1

    return 0


def calcula_pontos_regra_avancada(dados):
    dicio_notas = {
        'sem_combinacao': calcula_pontos_soma(dados),
        'quadra': calcula_pontos_quadra(dados),
        'full_house': calcula_pontos_full_house(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'cinco_iguais': calcula_pontos_quina(dados)
    }
    return dicio_notas


def faz_jogada(dados, categoria, cartela):
    regra_simples = cartela['regra_simples']
    regra_avancada = cartela['regra_avancada']

    if categoria in ['1', '2', '3', '4', '5', '6']:
        regra_simples[int(categoria)] = calcula_pontos_regra_simples(dados)[int(categoria)]
    else:
        regra_avancada[categoria] = calcula_pontos_regra_avancada(dados)[categoria]

    return cartela


def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-" * 25)
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-" * 25)