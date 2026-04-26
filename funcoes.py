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
        i+=1

    dados_no_estoque.append(valor_guardado)  

    return [dados_rolados_final, dados_no_estoque]    

dados_rolados = [6, 1, 6, 4]
dados_no_estoque = [2]
dado_para_guardar = 2

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    if dado_para_remover < len(dados_no_estoque):
        dados_rolados.append(dados_no_estoque[dado_para_remover])   
        del dados_no_estoque[dado_para_remover]
    
    return [dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples(dados_rolados):
    dicionario_pontos_simples = {}

    for numero in range(1,7):
        if numero not in dicionario_pontos_simples:
            dicionario_pontos_simples[numero] = 0

    for i in range(0, len(dados_rolados)):
        dicionario_pontos_simples[dados_rolados[i]] += dados_rolados[i]
    return dicionario_pontos_simples

def calcula_pontos_soma(dados_rolados):
    soma = 0
    for dado in dados_rolados:
        soma += dado
    return soma

def calcula_pontos_sequencia_baixa(dados_rolados):
    for n in [1,2,3]:
        if n in dados_rolados and n+1 in dados_rolados and n+2 in dados_rolados and n+3 in dados_rolados:
            return 15
    return 0