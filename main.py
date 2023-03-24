import time
import pandas as pd
import generator
import Data

def parent(i):
    return (i - 1) // 2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def to_xls_file(arr, file_name: str):
    df = pd.DataFrame(data = data_array(arr), columns = ['Date', 'Flight', 'Full Name', 'Place'])
    file_name = file_name + '.xlsx'
    writer = pd.ExcelWriter(file_name, engine ='xlsxwriter')
    df.to_excel(writer, 'flight_table1')
    writer.save()

def from_xlsx_file(file_name: str):
    xl = pd.ExcelFile(file_name)
    df = xl.parse('flight_table1')
    arr = []
    for i in range(len(df)):
        row = df.iloc[i]
        data = Data.Data(row[1].to_pydatetime(), int(row[2]), str(row[3]), int(row[4]))
        arr.append(data)
    return arr

def data_array(array):
    arr = []
    for i in range(len(array)):
        arr2 = []
        arr2.append(array[i].Date)
        arr2.append(array[i].Flight)
        arr2.append(array[i].FullName)
        arr2.append(array[i].Place)
        arr.append(arr2)
    return arr

def insertation_sort(data_file: str, text_file: str):
    f = open(text_file, 'a')
    arr = from_xlsx_file(data_file)
    start_time = time.time()
    for i in range(1, len(arr)):
        j = i
        temp = arr[j]
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = temp
    print(data_file + ' :')
    print("       %s seconds       " % (time.time() - start_time))
    note = data_file + ' time = ' + str(time.time() - start_time) + '  !! INSERT SORT !!' + '\n'
    f.write(note)
    f.close()
    note2 = data_file.rsplit(".", 1)[0] + '_insert_sorted'
    to_xls_file(arr, note2)

def heapify(heap, index, size):
    l = left(index)
    r = right(index)
    if (l < size and heap[l] > heap[index]):
        largest = l
    else:
        largest = index
    if (r < size and heap[r] > heap[largest]):
        largest = r
    if (largest != index):
        heap[largest], heap[index] = heap[index], heap[largest]
        heapify(heap, largest, size)


def heap_sort(data_file: str, text_file: str):
    f = open(text_file, 'a')
    array = from_xlsx_file(data_file)
    start_time = time.time()
    length = len(array)
    beginning = parent(length - 1)
    while beginning >= 0:
        heapify(array, index=beginning, size=length)
        beginning = beginning - 1
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, index=0, size=i)
    print(data_file + ' :')
    print("       %s seconds       " % (time.time() - start_time))
    note = data_file + ' time = ' + str(time.time() - start_time) + '  !! HEAP SORT !!' + '\n'
    f.write(note)
    f.close()
    note2 = data_file.rsplit(".", 1)[0] + '_heap_sorted'
    to_xls_file(array, note2)

def bubble_sort(data_file: str, text_file: str):
    f = open(text_file, 'a')
    array = from_xlsx_file(data_file)
    start_time = time.time()
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff
    print(data_file + ' :')
    print("       %s seconds       " % (time.time() - start_time))
    note = data_file + ' time = ' + str(time.time() - start_time) + ' !! BUBBLE SORT !!' + '\n'
    f.write(note)
    f.close()
    note2 = data_file.rsplit(".", 1)[0] + '_bubblesort'
    to_xls_file(array, note2)

bubble_sort('flight_info_100.xlsx', 'times.txt')
insertation_sort('flight_info_100.xlsx', 'times.txt')
heap_sort('flight_info_100.xlsx', 'times.txt')

bubble_sort('flight_info_500.xlsx', 'times.txt')
insertation_sort('flight_info_500.xlsx', 'times.txt')
heap_sort('flight_info_500.xlsx', 'times.txt')

bubble_sort('flight_info_1000.xlsx', 'times.txt')
insertation_sort('flight_info_1000.xlsx', 'times.txt')
heap_sort('flight_info_1000.xlsx', 'times.txt')

bubble_sort('flight_info_2500.xlsx', 'times.txt')
insertation_sort('flight_info_2500.xlsx', 'times.txt')
heap_sort('flight_info_2500.xlsx', 'times.txt')

bubble_sort('flight_info_5000.xlsx', 'times.txt')
insertation_sort('flight_info_5000.xlsx', 'times.txt')
heap_sort('flight_info_5000.xlsx', 'times.txt')

bubble_sort('flight_info_7500.xlsx', 'times.txt')
insertation_sort('flight_info_7500.xlsx', 'times.txt')
heap_sort('flight_info_7500.xlsx', 'times.txt')

bubble_sort('flight_info_10000.xlsx', 'times.txt')
insertation_sort('flight_info_10000.xlsx', 'times.txt')
heap_sort('flight_info_10000.xlsx', 'times.txt')
