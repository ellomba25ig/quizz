# Modelo de dados
.listas
.dicionario com certas/erradas
.lista de dicionários em pontuacoes.json

Exemplo 1
pergunta = [
   
    {
        "Pergunta" : "Quem escreveu os Lusíadas?",
        "Opções" : ["A)Gil Vicente","B)Caetano da Costa ","C)Luis de Camoes","D)Alda do Espirito Santo"]
        "Resposta correta" : 2,
        "Categoria" : "Literatura"
    },

    {   "Pergunta" : "Qual é o maoir orgão do corpo humano?",
        "Opções" : ["A)Coração","B)Pulmão"," C)Cérebro"," D)Pele"],
        "Resposta correta" : 3,
        "Categoria" : "Biologia"
]

#2) Entradas / Processamento / Saídas
    Entrada
.Ficheiro de perguntas
.Escolha do utilizar no menu
.Mostrar categorias
.Respostas do utilizador
.Respostas ao longo do jogo

    Processamento
.Carregamento das perguntas
.Pedir ajuda ao jogo
.Verificar a resposta escolhida
.Comparar com a resposta certas
.Calcular a pontuação
.Determinar resultado final
    Saidas
.Perguntas que o utlizar deve responder
.Respostas "correta" ou "errada"
.Chances
.Pontos adqueridos/pontuação final

#  Lista de funções (com responsabilidades)

 Função
.mostrar_perguntas
.mostrar_menu
.mostar_categoria
.mostrar_respostas
.mostar_verificção de respostas
.mostrar_chances
.calcular_pontução
.mostrar_pontuação
.mostar resultado final