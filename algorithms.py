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
        while ((y != 0) and (list[y] < list[y-1])):
            aux = list[y]
            list[y] = list[y-1]
            list[y-1] = aux
            y -= 1
    return list

def bubble_sort(list):

    for x in range(0, len(list)):
        for y in range(0, len(list)-1):
            if list[y] > list[y+1]:
                aux = list[y]
                list[y] = list[y+1]
                list[y+1] = aux
    return list
