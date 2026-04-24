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

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    if dado_para_remover < len(dados_no_estoque):
        dados_rolados.append(dados_no_estoque[dado_para_remover])   
        del dados_no_estoque[dado_para_remover]
    
    return [dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples(dados_rolados):
    dicionario_pontos = {}

    for numero in range(1,7):
        if numero not in dicionario_pontos:
            dicionario_pontos[numero] = 0

    for i in range(0, len(dados_rolados)):
        dicionario_pontos[dados_rolados[i]] += dados_rolados[i]

    return dicionario_pontos