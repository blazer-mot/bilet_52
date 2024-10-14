input_data = open('input.txt', 'r',) # ВАЖНО!!!  не забыть создать файл; открытие файла ввода
data = input_data.read()
a = 0
i = 0
max = 0
a = int(data[0]) + int(data[1]) + int(data[2])
b = int(data[3]) + int(data[4]) + int(data[5])
if a == b:
    out = 'YES'
else:
    out = 'NO'
output_data = open('output.txt', 'w') # созпдние и открытие файла для вывода ответа
output_data.write(str(out)) # преобразование числа в строку при выводе и сам вывод
input_data.close() # закрытие файла считывания 
output_data.close() # закрытия файла вывода