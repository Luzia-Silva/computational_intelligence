import math

class Hash:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Representação do tabuleiro
        self.human_player = 'X' # jogador humano
        self.gambler_ia = 'O' # inteligência

    def display_board(self):
        for i in range(0, 9, 3):
            print(' | '.join(self.board[i:i+3]))
            if i < 6:
                print('--+---+--')

    def play_available(self, index): # Jogadas Disponíveis
        return self.board[index] == ' '

    def make_move(self, index, player): # Fazer Jogada
        self.board[index] = player

    def check_vitoria(self, player):   # Verificação das combinações vencedoras
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for comb in winning_combinations:
            if all(self.board[i] == player for i in comb):
                return True
        return False

    def board_cheio(self):
        return ' ' not in self.board

    def minimax(self, profundidade, player):
      if player == self.gambler_ia:
          best_score = float('-inf')
          best_move = None
      else:
          best_score = float('inf')
          best_move = None

      # Check for a draw
      if self.board_cheio():
          return 0  # Retornará 0 para indicar empate

      for i in range(9):
          if self.board[i] == ' ':
              self.board[i] = player
              punctuation = self.minimax(profundidade + 1, self.human_player if player == self.gambler_ia else self.gambler_ia)
              self.board[i] = ' '

              if player == self.gambler_ia:
                  if punctuation > best_score:
                      best_score = punctuation
                      best_move = i
              else:
                  if punctuation < best_score:
                      best_score = punctuation
                      best_move = i

      if profundidade == 0:
          return best_move
      else:
          return best_score

    
    def toPlay(self):
      print("Bem-vindo ao Jogo da Velha!")
      self.display_board()

      while True:
          if self.board_cheio():
              print("Empate!")
              break

          # Vez do jogador humano
          escolha = int(input("Escolha uma posição para jogar (de 1 a 9): ")) - 1
          if escolha >= 0 and escolha < 9 and self.play_available(escolha):
              self.make_move(escolha, self.human_player)
              self.display_board()

              if self.check_vitoria(self.human_player):
                  print("Você ganhou! Parabéns!")
                  break
          else:
              print("Posição inválida. Tente novamente.")
              continue

          # Verifique se há empate após a movimentação do usuário
          if self.board_cheio():
              print("Empate!")
              break

          # Vez da IA (usando o algoritmo Minimax)
          print("Turno da IA...")
          best_move = self.minimax(0, self.gambler_ia)

          # Lide com o caso em que best_move (Melhor Jogada) é None
          if best_move is None:
              print("Empate!")
              break

          self.make_move(best_move, self.gambler_ia)
          self.display_board()

          if self.check_vitoria(self.gambler_ia):
              print("A IA ganhou! Melhor sorte da próxima vez.")
              break

if __name__ == "__main__":
    game = Hash()
    game.toPlay()
