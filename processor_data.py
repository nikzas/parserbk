
with open("result", "r") as file:
    lines = [line for line in file]

numlist = []
for numbers_str in lines:
    numbers = [float(num_str) for num_str in numbers_str.strip()[1:-1].split(', ')]
    numlist.append(numbers)

pure_array = numlist[0]

idx0 = 0 #1
idx1 = 1 #2

while idx0 != len(numlist) + 1:
    if numlist[idx0] == numlist[idx1]:
        idx0 += 1
        idx1 += 1
    elif numlist[idx0] != numlist[idx1]:
        idx = numlist[idx1].index(numlist[idx0][0])
        #добавить сюда "добавить в начало списка"
        pure_array += numlist[idx1][:idx]
        idx0 += 1
        idx1 += 1
    else:
        print('Все готово')


