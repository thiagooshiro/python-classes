### **Proposta 1: Jogo de Pedra, Papel e Tesoura**  

**Objetivo:**  
Criar um jogo interativo em Python onde o usuário pode desafiar o computador em partidas de Pedra, Papel e Tesoura. O objetivo principal é implementar as regras do jogo, criar uma interação fluida com o usuário e aplicar conceitos de funções e loops para um funcionamento contínuo.  

---

**Instruções Detalhadas:**  
1. **Apresentação do Jogo:**  
   - Ao iniciar o programa, exiba uma mensagem de boas-vindas com uma breve explicação do jogo.  
   - Informe ao jogador as regras básicas e como encerrar o jogo caso deseje sair.  

2. **Escolha das Opções:**  
   - Exiba um menu onde o jogador possa selecionar uma das três opções:  
     1. Pedra  
     2. Papel  
     3. Tesoura  
   - O jogador deve inserir sua escolha digitando o número correspondente ou o nome da opção.  
   - Valide a entrada do jogador e, caso seja inválida, peça para que ele digite novamente.  

3. **Escolha do Computador:**  
   - O computador deve selecionar uma das opções (pedra, papel ou tesoura) de forma aleatória.  
   - Utilize a função `random.choice()` para garantir que a seleção seja imprevisível.  

4. **Regras do Jogo:**  
   - Implemente a lógica para determinar o vencedor da rodada com base nas regras:  
     - Pedra ganha de tesoura, mas perde para papel.  
     - Tesoura ganha de papel, mas perde para pedra.  
     - Papel ganha de pedra, mas perde para tesoura.  
   - Caso o jogador e o computador façam a mesma escolha, declare um empate.  

5. **Exibição dos Resultados:**  
   - Após cada rodada, exiba:  
     - A escolha do jogador e do computador.  
     - O vencedor da rodada ou se houve empate.  

6. **Funcionamento Contínuo:**  
   - Após exibir o resultado, pergunte ao jogador se ele deseja jogar novamente ou encerrar o jogo.  
   - Se o jogador optar por continuar, inicie uma nova rodada.  
   - Se o jogador decidir sair, encerre o programa com uma mensagem de despedida e exiba um resumo (veja o próximo passo).  

7. **Contagem de Pontuações (Opcional):**  
   - Adicione um contador para rastrear:  
     - Quantas rodadas foram jogadas.  
     - Quantas vitórias o jogador teve.  
     - Quantas vitórias o computador teve.  
     - Quantos empates ocorreram.  
   - Exiba esse resumo no final do jogo, antes de encerrar.  

---

**Desafio Extra:**  
- Antes de começar o jogo, ofereça ao jogador a opção de jogar partidas "melhor de 3" ou "melhor de 5":  
  - Defina que o vencedor geral será quem ganhar o número necessário de rodadas (ex.: 2 vitórias para melhor de 3).  
  - Mostre o placar atualizado ao final de cada rodada.  
  - Caso o jogador escolha não ativar o modo “melhor de X”, permita que ele jogue rodadas ilimitadas, encerrando o jogo apenas quando desejar.  

---

**Dicas e Sugestões:**  
- Organize seu código utilizando funções para tarefas como:  
  - Mostrar o menu inicial.  
  - Receber e validar a escolha do jogador.  
  - Determinar a escolha do computador.  
  - Calcular o vencedor da rodada.  
  - Atualizar e exibir o placar.  
- Use loops para garantir que o jogo funcione de forma contínua até que o jogador escolha sair.  
- Para um programa mais interativo, utilize mensagens criativas e divertidas que tornem o jogo mais envolvente.  

---

**Exemplo de Saída:**  
```
Bem-vindo ao jogo de Pedra, Papel e Tesoura!
Regras:
- Pedra ganha de Tesoura.
- Tesoura ganha de Papel.
- Papel ganha de Pedra.
Digite "sair" a qualquer momento para encerrar.

Escolha uma opção:
1 - Pedra
2 - Papel
3 - Tesoura

Sua escolha: Pedra
Escolha do computador: Tesoura
Você ganhou esta rodada!

Deseja jogar novamente? (sim/não): sim

Escolha uma opção:
1 - Pedra
2 - Papel
3 - Tesoura
```
