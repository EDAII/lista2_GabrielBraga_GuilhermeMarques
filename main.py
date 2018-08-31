import random
import os
import time
from algorithms import *
from plotter import plotter, tester

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def mainMenu():
  print('1 - Criar lista aleatória')
  print('2 - Ordenar lista Selection Sort')
  print('3 - Ordenar lista Insertion Sort')
  print('4 - Ordenar lista Bubble Sort')
  print('5 - Gerar gráfico Selection Sort')
  print('6 - Gerar gráfico Insertion Sort')
  print('7 - Gerar gráfico Bubble Sort')
  print('8 - Printar lista')
  print('0 - Sair')
  option = input()
  return option

if __name__ == '__main__':
  lst = []
  exit = False

  while(not exit):
    option = mainMenu()
    if option == '0':
      exit =  True
      clear()
    elif option == '1':
      clear()
      entry = int(input('Insira o tamanho da lista: '))
      lst = random.sample(range(0,3*entry), entry)
      print('Lista criada com sucesso')
    elif option == '2':
      clear()
      lst = selection_sort(lst)
    elif option == '3':
      clear()
      lst = insertion_sort(lst)
    elif option == '4':
      clear()
      lst = bubble_sort(lst)
    elif option == '5':
      clear()
      qtdTeste = int(input('Insira a quantidade de testes: '))
      times = tester(selection_sort, lst, qtdTeste)
      plotter(times)
    elif option == '6':
      clear()
      qtdTeste = int(input('Insira a quantidade de testes: '))
      times = tester(insertion_sort, lst, qtdTeste)
      plotter(times)
    elif option == '7':
      clear()
      qtdTeste = int(input('Insira a quantidade de testes: '))
      times = tester(bubble_sort, lst, qtdTeste)
      plotter(times)
    elif option == '8':
      clear()
      print(lst)
    else:
      pass
