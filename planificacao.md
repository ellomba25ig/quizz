# Planificação

## Grupo

> Catarina

> ElLomba

> Infiltrado

---

## Opções Escolhidas

### Nível 2

- Categorias e/ou dificuldade
- Pontuações guardadas

### Nível 3

- Modo contra-relógio

---

## Modelo de Dados

- listas
- dicionario com certas/erradas
- lista de dicionários em pontuacoes.json

### Exemplo 1

```json
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
    }
]
```

---

## Entradas / Processamento / Saídas
    
### Entrada
- Ficheiro de perguntas
- Escolha do utilizar no menu
- Mostrar categorias
- Respostas do utilizador
- Respostas ao longo do jogo

### Processamento
- Carregamento das perguntas
- Pedir ajuda ao jogo
- Verificar a resposta escolhida
- Comparar com a resposta certas
- Calcular a pontuação
- Determinar resultado final
- Efeitos sonores durante o jogo

### Saidas
- Perguntas que o utlizar deve responder
- Respostas "correta" ou "errada"
- Tentativas
- Pontos adqueridos/pontuação final

---

## Lista de funções (com responsabilidades)

- mostrar_perguntas
- mostrar_pergunta
- mostrar_menu
- escolher_categoria
- receber_respostas
- verificar_resposta
- gerir_tentativas
- calcular_pontução
- mostrar_pontuação
- mostar_resultado_final
- calcular_tempo
- Produzir_som

---

## Fluxo do programa

1. Iniciar o programa
2. Limpar o ecrã e apresentar o meno principal
3. Ler a opção selecionada pelo utilizador
4. Se a opção for inválida,apresentar uma mensagem de erro e voltar a pedir uma opção
5. Se a opção for jogar,carregar as perguntas do ficheiro Json
6. Solicitar ao utilizador que escolha uma categoria
7. Atualizar a pontuação após cada resposta correta
8. Quando tiverem sido respondidas,apresentar a pontução final
9. Se escolher *Sim*,reiniciar o jogo
10. Se escolher *Não*,regressar ao menu principal ou terminar o programa
11. Se escolher *Sair* no menu principal,encerrar o programa

---

## Ecrãs do programa
- o utilizador verá duas opcões como escolher jogar e sair
- Escolha de categoria(listas das categorias para seleção)
- Jogo(perguntas, opções de perguntas,pontuação atual )
- pontuação final(pontuação final)
- Ajuste de som

---

## Plano de testes (manual)
- Se escolher uma opção fora do intervalo, dá erro e repete
- se utilizar escolher uma categoria inexistente,o programa não crasha e volta a pedir
- o ficheiro das perguntas não existe
- se o programa mostrar 4 opções de resposta e o utilizador introduz uma 5 resposta
- se a pontuação for mal carregada do ficheiro e não conseguir calcular a pontuação final
- se a biblioteca para carregar o relógio não carregar






