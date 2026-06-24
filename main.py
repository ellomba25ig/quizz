import time 
import json
import random

def regras():
    print("1) São feitas 5 perguntas")
    print("2) As perguntas têm dificuldades diferentes. Quanto mais dificil, mais pontos.")
    print("3) Cada pergunta deve ser respondida dentro de 10 segundos")
    print("4) O utilizador deve escolher apenas uma resposta por pergunta ")
    print("5) No final o programa apresenta quantas perguntas o utilizador acertou")


# Objetivo: Escolher 5 perguntas aleatórias
# Recebe:
# - perguntas: Lista com as perguntas
# Devolve:
# - As perguntas selecionadas
def seleciona_perguntas(perguntas):
    perguntas_escolhidas = []
    perguntas_escolhidas = random.sample(perguntas, 5)
    return perguntas_escolhidas
    
def carrega_perguntas():
    perguntas_temp = []
    with open("perguntas.json", "r", encoding="utf-8") as f:
        perguntas_temp = json.load(f)
    return perguntas_temp

def mostrar_pergunta(pergunta):
    i = 0
    print("=========== Pergunta ===========")
    print(f"Categoria: {pergunta["Categoria"]}")
    print(f"Dificuldade:{pergunta["Dificuldade"]}\n")
    print(f"Pergunta: {pergunta["Pergunta"]}")
    for opcao in pergunta["Opções"]:
        print(f"== {i} - {opcao}")
        i = i + 1
    op = int(input("== Qual a tua resposta? "))
    return op


def mostrar_menu():
    print("=========== Jogo das Perguntas ===========")
    print("== 1) Jogar")
    print("== 2) Regras")
    print("== 3) Sair")
    op = int(input("Qual a tua opção: "))
    return op

def escolher_dificuldade():
    print("=========== Escolhe a dificuldade ===========")
    print("== 1) Fácil")
    print("== 2) Médio")
    print("== 3) Dificil")
    print("== 4) Aleatório")
    print("== 5) Voltar")
    op = int(input("Qual a tua opção: "))
    return op

def verificar_resposta(pergunta, resposta_user):
    if pergunta["Resposta correta"]==resposta_user:
        print("Boa acertaste! És lindo!!")
        return True
    else:
        print("Ohh... :( Assim fico triste... Erraste...")
        return False

def mostar_resultado_final(pontuacao_total, perguntas_acertadas):
    print("=========== Resultado final ===========")
    print(f"Pontuação total:{pontuacao_total}")
    print(f"Número de perguntas acertadas:{perguntas_acertadas}")

def main():
    perguntas = []
    tempo_permitido = 10

    while True:
        op = mostrar_menu()
        pontos = 0
        if op == 1:
            op_dificuldade = escolher_dificuldade()
            pontuacao_total = 0
            perguntas_acertadas = 0
            perguntas_filtradas = []
            perguntas = carrega_perguntas()

            if op_dificuldade == 1:
                for pergunta in perguntas:
                    if pergunta["Dificuldade"] == "Fácil":
                        perguntas_filtradas.append(pergunta)
            elif op_dificuldade == 2:
                for pergunta in perguntas:
                    if pergunta["Dificuldade"] == "Médio":
                        perguntas_filtradas.append(pergunta)
            elif op_dificuldade == 3:
                for pergunta in perguntas:
                    if pergunta["Dificuldade"] == "Difícil":
                        perguntas_filtradas.append(pergunta)
            elif op_dificuldade == 4:
                perguntas_filtradas = perguntas

            perguntas_escolhidas = seleciona_perguntas(perguntas_filtradas)
            for pergunta in perguntas_escolhidas:
                tempo_inicial = time.time()
                resposta_user = mostrar_pergunta(pergunta)               
                verificacao = verificar_resposta(pergunta, resposta_user)
                if verificacao:
                    tempo_final = time.time()
                    tempo_resposta = tempo_final - tempo_inicial

                    if tempo_resposta <= tempo_permitido:
                        perguntas_acertadas = perguntas_acertadas + 1
                        if pergunta["Dificuldade"] == "Fácil":
                            pontos = 5
                        elif pergunta["Dificuldade"] == "Médio":
                            pontos = 10
                        else:
                            pontos = 15
                        pontuacao_total = pontuacao_total + pontos
                        print(f"Pontos até agora: {pontuacao_total}")
                    else:
                        print(f"Ohhhh... Até acertaste... Mas demoraste {tempo_resposta}")
                else:
                    print("Erraste")
                    break
                    
            mostar_resultado_final(pontuacao_total, perguntas_acertadas)
        elif op == 2:
            regras()
        elif op == 3:
            print("Adeus bebé! Foi um gosto! Para a próxima traz chocolates!")
            break

main()


