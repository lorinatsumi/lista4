
import random

apostas = []
nomes = []
numerosorteado = 0
teveganhador = 0


def printMenu():
  print("==============================")
  print("Opções:")
  print("1 - Adicionar aposta")
  print("2 - Listar apostas")
  print("3 - Sortear um número")
  print("4 - Apresentar o ganhador")
  print("5 - Sair")

def adicionarAposta():
  aposta = int(input("Digite a sua aposta: "))
  nome = input ("Digite seu nome: ")
  print(aposta)
  apostas.append(aposta)
  nomes.append(nome)

def listarapostas():
  for i in range (len(apostas)):
    aposta = apostas [i]
    nome = nomes [i]
    print (f"{nome} apostou {aposta}")

def numsorteio():
  num = random.randrange(1,20)
  print(num)
  return num

def nomeGanhador():
  teveganhador = False
  for i in range (len(apostas)):
    if apostas [i] == numerosorteado:
      print(nomes[i])
      teveganhador = True
    if not teveganhador:
      print ("Não teve ganhador")





opcao = 0
while opcao != 5:
  printMenu()
  opcao = int(input("Digite a opção: "))
  if opcao == 1:
    adicionarAposta()
  if opcao == 2:
    listarapostas()
  if opcao == 3: 
    numerosorteado = numsorteio()
  if opcao == 4:
    teveganhador = nomeGanhador ()

print("Game over")