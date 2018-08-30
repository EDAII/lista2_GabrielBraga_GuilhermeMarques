import random
import os

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def mainMenu():
  print('1 - Criar lista aleatória')
  print('2 - Ordenar lista Selection Sort')
  print('3 - Ordenar lista Insertion Sort')
  print('4 - Ordenar lista Bubble Sort')
  print('5 - Printar lista')
  print('0 - Sair')
  option = input()
  return option

def selection_sort(list):

    for x in range(0, len(list)-1):
        min = x
        for y in range(x+1, len(list)):
            if (list[y] < list[min]):
                min = y
        aux = list[min]
        list[min] = list[x]
        list[x] = aux
    return list

def insertion_sort(list):

    for x in range(0, len(list)):
        y = x
        while ((y!=0) and (list[y] < list[y-1])):
            aux = list[y]
            list [y] = list[y-1]
            list[y-1] = aux
            y-=1
    return list

def bubble_sort(list):

    for x in range(0, len(list)):
        for y in range(0, len(list)-1):
            if list[y]>list[y+1]:
                aux = list[y]
                list[y] = list[y+1]
                list[y+1] = aux
    return list

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
      print(lst)
    else:
      pass