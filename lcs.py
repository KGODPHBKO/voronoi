import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

y = ['','b','b','b','a','a','a','a','a','a','a','a','c','c','c','c','b','b','b','b','b','b','b','b','a','a','a','a','a','c','c','c','c','a','a','a','a']
x=['','a','a','a','b','b','b','b','b','b','c','c','c','c','a','a','a','a','a','a','a','a','a','a','a','a']
dp = np.full((len(x), len(y)),0)
#print(len(x), len(y))
trace = np.full((len(x), len(y)),4)
road = np.full((len(x), len(y)),'  0')

for i in range(1,len(x)):
    for j in range(1,len(y)):
        #print(x[i],y[j])
        if(x[i] == y[j]):
            dp[i][j] = dp[i-1][j-1]+1
            trace[i][j] = 0
        else:
            maxvalue = max(dp[i-1][j],dp[i][j-1])
            if(dp[i][j-1] >= dp[i-1][j]):#左走
                trace[i][j] = 1
                #print(i,j,dp[i-1][j],dp[i][j-1],'down')
            else:#上走
                trace[i][j] = 2
                #print(i,j,dp[i-1][j],dp[i][j-1],'top')
            dp[i][j] = maxvalue

#print(trace)

i = 25
j = 36
sum = 0
for _ in range(40):
    print(i,j,dp[i][j])
    road[i][j]=chr(0x25cf)
    if(trace[i][j]==0):
        sum+=1
        i-=1
        j-=1
    elif(trace[i][j]==1):
        j-=1
    elif(trace[i][j]==2):
        #i-=1
        j-=1
    else:
        break


        


    
        



       


max_digits = 2
with open('road.txt', 'w') as file:
    # 写入列标号
    file.write(" " * (max_digits + 1))
    for col in range(len(road[0])):
        file.write(" {:>{}}  ".format(col, max_digits))
    file.write("\n")

    # 写入每一行的数据，包括行标号
    for row_index, row in enumerate(road):
        file.write("{:>{}}  ".format(row_index, max_digits))
        for num in row:
            formatted_num = "{:>{}}  ".format(num, max_digits)
            file.write(formatted_num)
        file.write("\n")

print("数据已写入文件road。")

'''
max_digits = 2
with open('matrix.txt', 'w') as file:
    # 写入列标号
    file.write(" " * (max_digits + 1))
    for col in range(len(dp[0])):
        file.write("{:>{}}  ".format(col, max_digits))
    file.write("\n")

    # 写入每一行的数据，包括行标号
    for row_index, row in enumerate(dp):
        file.write("{:>{}}  ".format(row_index, max_digits))
        for num in row:
            formatted_num = "{:>{}}  ".format(num, max_digits)
            file.write(formatted_num)
        file.write("\n")

print("数据已写入文件matrix。")


max_digits = 2
with open('forced path.txt', 'w') as file:
    # 写入列标号
    file.write(" " * (max_digits + 1))
    for col in range(len(trace[0])):
        file.write("{:>{}}  ".format(col, max_digits))
    file.write("\n")

    # 写入每一行的数据，包括行标号
    for row_index, row in enumerate(trace):
        file.write("{:>{}}  ".format(row_index, max_digits))
        for num in row:
            formatted_num = "{:>{}}  ".format(num, max_digits)
            file.write(formatted_num)
        file.write("\n")

print("数据已写入文件forced path。")
'''