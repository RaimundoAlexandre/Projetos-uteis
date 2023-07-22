# github RaimundoAlexandre
from random import randint
from time import sleep

print("="*40)
print(f"{'SIMULADOR DE DADOS':^40}")
print("="*40)


print("-"*40)
nome = str(input("Qual é o seu nome? ")).strip().capitalize()
while True:
  while True:
    try:
      player = int(input(f"Senhor {nome} escolha um número de 1 a 6: "))
      if player > 0 and player < 6:
        break
      elif player <= 0 or player > 6:
        print("Valor incorreto")
        print("Digite novamente")
    except ValueError:
      print("Valor in correto")
  pc = randint(1, 6)

  print(f"O sr. {nome} escolheu {player} e o computador escolheu {pc}")

  print("Vamos jogar o dado")
  print("-"*40)
  dado = randint(1, 6)
  sleep(2)
  print(f"O número {dado} saio ao rolar o dado")
  sleep(1)
  if dado == player > pc:
    print(f"Parabéns sr. {nome}, você ganhou!!")
  elif dado == pc > player:
    print(f"Que pena sr. {nome}, você perdeu!!")
  elif player > pc:
    print(f"O sr.{nome} tirou o maior valor, e ganhou a partida")
  elif player == pc:
    print(f"O sr. {nome} tirou o mesmo número que o computador")
    print("Empate!!")
  else:
    print("O computador tirou o maior número")
    print(f"O sr. perdeu sr. {nome}")
  sair = str(input("Quer jogar novamente?[S/N]: "))[0].upper().strip()
  if sair == 'N':
    break
