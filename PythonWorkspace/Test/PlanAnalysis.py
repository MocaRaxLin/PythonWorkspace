__author__ = 'Justin'

#variables
dataX_array = []
dataY_array = []

#input file
file = open('txtfile/plan data.txt','r',encoding='UTF-8')
i = 0
while True:
    strDA = file.readline()
    if not strDA: break
    dataAmount = int(strDA)
    #print('方案個數：'+strDA)
    x = [];
    y = [];
    for i in range(0, dataAmount, 1):
        s = file.readline()
        char = s.split(" ")
        intX = int(char[0])
        intY = int(char[1])
        #print(intX+", "+intY)
        x.append(intX)
        y.append(intY)
    dataX_array.append(x)
    dataY_array.append(y)
file.close()

#show
for i in range(0,4):
    print('用量(MB):')
    print(dataX_array[i])
    print('合約費用(NTD):')
    print(dataY_array[i])
print()

#how much per MB
dollarPerMB = []
for a, b in zip(dataX_array, dataY_array):
    for x, y in zip(a, b):
        dollarPerMB.append(y/x)
    print('每MB多少錢：')
    print(dollarPerMB)
    dollarPerMB.clear()

