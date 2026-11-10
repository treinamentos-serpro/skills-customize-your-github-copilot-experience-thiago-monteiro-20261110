
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Pratique strings, listas, loops, condicionais e entrada do usuário criando um jogo da Forca em Python. Ao final, o jogo deverá permitir que uma pessoa adivinhe uma palavra oculta antes de esgotar as tentativas.

## 📝 Tarefas

### 🛠️ Escolha da Palavra e Preparação do Jogo

#### Descrição
Complete o código inicial para escolher uma palavra aleatória da lista e preparar as variáveis que representam o estado da partida. Mostre a palavra como uma sequência de espaços ocultos, um para cada letra.

#### Requisitos
O programa concluído deve:

- Selecionar uma palavra aleatoriamente da lista `words`.
- Inicializar uma coleção para registrar as letras já tentadas.
- Definir o limite de palpites incorretos permitido para a partida.
- Exibir o progresso da palavra usando um sublinhado para cada letra ainda não descoberta.

### 🛠️ Jogue e Apresente o Resultado

#### Descrição
Implemente o loop principal para receber palpites de letras e atualizar o progresso. Continue a partida até que a pessoa descubra a palavra ou alcance o limite de palpites incorretos.

#### Requisitos
O programa concluído deve:

- Solicitar um palpite de letra e verificar se ele aparece na palavra escolhida.
- Revelar todas as posições de uma letra correta e atualizar o progresso exibido.
- Contar palpites incorretos e informar quantas tentativas restam.
- Encerrar a partida quando a palavra for descoberta ou não houver mais tentativas.
- Exibir uma mensagem indicando vitória ou derrota; em caso de derrota, revelar a palavra escolhida.