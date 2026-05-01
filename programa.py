from funcoes import *

cartela_pontuacao = {
    'regra_simples': {i: -1 for i in range(1, 7)},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1,
    }
}

opcoes_combinacao = [
    '1', '2', '3', '4', '5', '6',
    'cinco_iguais', 'full_house', 'quadra',
    'sem_combinacao', 'sequencia_alta', 'sequencia_baixa'
]

imprime_cartela(cartela_pontuacao)

for numero_rodada in range(1, 13):
    dados_na_mesa = rolar_dados(5)
    dados_guardados = []
    quantidade_rerrolagens = 0

    print(f"Dados rolados: {dados_na_mesa}")
    print(f"Dados guardados: {dados_guardados}")
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

    rodada_encerrada = False
    while not rodada_encerrada:
        escolha_menu = input()

        if escolha_menu == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice_dado = int(input())
            novo_estado_dados = guardar_dado(dados_na_mesa, dados_guardados, indice_dado)
            dados_na_mesa = novo_estado_dados[0]
            dados_guardados = novo_estado_dados[1]

            print(f"Dados rolados: {dados_na_mesa}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif escolha_menu == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice_dado = int(input())
            novo_estado_dados = remover_dado(dados_na_mesa, dados_guardados, indice_dado)
            dados_na_mesa = novo_estado_dados[0]
            dados_guardados = novo_estado_dados[1]

            print(f"Dados rolados: {dados_na_mesa}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif escolha_menu == '3':
            if quantidade_rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_na_mesa = rolar_dados(len(dados_na_mesa))
                quantidade_rerrolagens += 1

            print(f"Dados rolados: {dados_na_mesa}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif escolha_menu == '4':
            imprime_cartela(cartela_pontuacao)
            print(f"Dados rolados: {dados_na_mesa}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif escolha_menu == '0':
            print("Digite a combinação desejada:")
            while True:
                combinacao_escolhida = input()

                if combinacao_escolhida not in opcoes_combinacao:
                    print("Combinação inválida. Tente novamente.")
                    continue

                if combinacao_escolhida in cartela_pontuacao['regra_avancada']:
                    combinacao_ja_utilizada = cartela_pontuacao['regra_avancada'][combinacao_escolhida] != -1
                else:
                    combinacao_ja_utilizada = cartela_pontuacao['regra_simples'][int(combinacao_escolhida)] != -1

                if combinacao_ja_utilizada:
                    print("Essa combinação já foi utilizada.")
                    continue

                todos_os_dados = dados_na_mesa + dados_guardados
                faz_jogada(todos_os_dados, combinacao_escolhida, cartela_pontuacao)
                break

            rodada_encerrada = True

        else:
            print("Opção inválida. Tente novamente.")

imprime_cartela(cartela_pontuacao)

total_regra_simples = sum(
    valor for valor in cartela_pontuacao['regra_simples'].values() if valor != -1
)

total_regra_avancada = sum(
    valor for valor in cartela_pontuacao['regra_avancada'].values() if valor != -1
)

bonus_regra_simples = 35 if total_regra_simples >= 63 else 0
pontuacao_total = total_regra_simples + total_regra_avancada + bonus_regra_simples

print(f"Pontuação total: {pontuacao_total}")