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

kkkkkkkkkkkkkkkkkkkk