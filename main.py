 

import json
import random

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
    print("== 2) Sair")
    op = int(input("Qual a tua opção: "))
    return op


def verificar_resposta(pergunta, resposta_user):
    if pergunta["Resposta correta"]==resposta_user:
        print("Boa acertaste! És lindo!!")
        return True
    else:
        print("Ohh... :( Assim fico triste... Erraste...")
        return False


def main():
    perguntas = []
    

    while True:
        op = mostrar_menu()
        pontos = 0
        if op == 1:
            pontuacao_total = 0
            perguntas = carrega_perguntas()
            perguntas_escolhidas = seleciona_perguntas(perguntas)
            for pergunta in perguntas_escolhidas:
                resposta_user = mostrar_pergunta(pergunta)               
                verificacao = verificar_resposta(pergunta, resposta_user)
                if verificacao:
                    if pergunta["Dificuldade"] == "Fácil":
                        pontos = 5
                    elif pergunta["Dificuldade"] == "Médio":
                        pontos = 10
                    else:
                        pontos = 15
                    pontuacao_total = pontuacao_total + pontos
                    print(f"Pontos até agora: {pontuacao_total}")
                else:
                    print("Erraste")

        elif op == 2:
            print("Adeus bebé! Foi um gosto! Para a próxima traz chocolates!")
            break

main()
