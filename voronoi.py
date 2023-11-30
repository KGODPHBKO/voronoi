import tkinter as tk
from tkinter import filedialog
import math
import re
import copy

edge = []
polygon = []
vertex =[]
samepol = []

stepBysteparray = []
stepbystepcount = 0
turn = 0



def recursive_function(n):
    if n <= 3:
        return 1

    # 递归调用左右两部分
    left_size = n // 2
    right_size = n - left_size
    return 1 + recursive_function(left_size) + recursive_function(right_size)


#檢查是否三點共線
def are_points_collinear(x1, y1, x2, y2, x3, y3):
    # 檢查兩個點是否共線
    return (x1 - x2) * (y2 - y3) == (x2 - x3) * (y1 - y2)


#算外心
def calculate_circumcenter(x1, y1, x2, y2, x3, y3):
    #// 計算分母D，以確保不會除以零
    D = 2 * ((x1 - x2) * (y2 - y3) - (y1 - y2) * (x2 - x3))
    # // 計算外心的x和y座標
    x = ((y2 - y3) * (x1 * x1 + y1 * y1 - x2 * x2 - y2 * y2) -(y1 - y2) * (x2 * x2 + y2 * y2 - x3 * x3 - y3 * y3)) / D

    y = ((x1 - x2) * (x2 * x2 + y2 * y2 - x3 * x3 - y3 * y3) -(x2 - x3) * (x1 * x1 + y1 * y1 - x2 * x2 - y2 * y2)) / D


    return (x, y)

def cross_product(x1, y1, x2, y2, x3, y3):
    # 計算向量 [x1, y1] [x2, y2] 和 [x1, y1] [x3, y3] 的叉積
    cross = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    
    if cross > 0:
        return 2#左轉
    elif cross < 0:
        return 1#右轉
    else:
        return 0
    
def cross_productbymerge(a,b):
    return a[0] * b[1] - a[1] * b[0]

#暴力解
def doviolance(i,k,j):
    
    global edge
    global polygon
    global vertex
    print("doviolance",i,k,j)
    lengthOfpol = len(polygon)
    lengthOfedge = len(edge)
    lengthOfvertex = len(vertex)

    reverseline = 1; #法向量方向

    x1=point[i][0]
    y1=point[i][1]
    x2=point[k][0]
    y2=point[k][1]
    x3=point[j][0]
    y3=point[j][1]

    if(j-i+1==2):
    
        edge.append([lengthOfpol+2,lengthOfpol+1,lengthOfvertex+1,lengthOfvertex+2,lengthOfedge+3,lengthOfedge+2,lengthOfedge+2,lengthOfedge+3,1])#最後一bit 線是真還是無窮遠 e1
        edge.append([lengthOfpol+1,lengthOfpol+3,lengthOfvertex+1,lengthOfvertex+2,lengthOfedge+1,lengthOfedge+3,lengthOfedge+3,lengthOfedge+1,0])#e2
        edge.append([lengthOfpol+2,lengthOfpol+3,lengthOfvertex+2,lengthOfvertex+1,lengthOfedge+1,lengthOfedge+2,lengthOfedge+2,lengthOfedge+1,0])#e3
        
        polygon.append([lengthOfedge+1])#poligon1
        polygon.append([lengthOfedge+1])#poligon2
        polygon.append([lengthOfedge+2])#poligon3
       

        v1 = x3-x1 #正向量
        v2 = y3-y1
        v2_x = -1*v2
        v2_y = v1

        vertex.append([-20*v2_x,-20*v2_y,0]) #vertex1
        vertex.append([20*v2_x,20*v2_y,0]) #vertex2
       

    elif(j-i+1==3):
        if(are_points_collinear(x1,y1,x2,y2,x3,y3)):
            edge.append([lengthOfpol+2,lengthOfpol+1,lengthOfvertex+1,lengthOfvertex+2,lengthOfedge+3,lengthOfedge+4,lengthOfedge+4,lengthOfedge+5,1]) # e1-e6
            edge.append([lengthOfpol+3,lengthOfpol+2,lengthOfvertex+3,lengthOfvertex+4,lengthOfedge+6,lengthOfedge+3,lengthOfedge+5,lengthOfedge+6,1])
            edge.append([lengthOfpol+2,lengthOfpol+4,lengthOfvertex+3,lengthOfvertex+1,lengthOfedge+2,lengthOfedge+6,lengthOfedge+4,lengthOfedge+1,0])
            edge.append([lengthOfpol+1,lengthOfpol+4,lengthOfvertex+1,lengthOfvertex+2,lengthOfedge+1,lengthOfedge+3,lengthOfedge+5,lengthOfedge+1,0])
            edge.append([lengthOfpol+2,lengthOfpol+4,lengthOfvertex+2,lengthOfvertex+4,lengthOfedge+1,lengthOfedge+4,lengthOfedge+6,lengthOfedge+2,0])
            edge.append([lengthOfpol+3,lengthOfpol+4,lengthOfvertex+4,lengthOfvertex+3,lengthOfedge+2,lengthOfedge+5,lengthOfedge+3,lengthOfedge+2,0])
        
            polygon.append([lengthOfedge+1])#poligon1-4
            polygon.append([lengthOfedge+1])#poligon1
            polygon.append([lengthOfedge+2])#poligon1
            polygon.append([lengthOfedge+6])#poligon1


            v1 = x2-x1 #正向量
            v2 = y2-y1
            v2_x = -1*v2
            v2_y = v1

            vertex.append([-20*v2_x,-20*v2_y,0]) #vertex1
            vertex.append([20*v2_x,20*v2_y,0]) #vertex2

            v1 = x3-x2 #正向量
            v2 = y3-y2
            v2_x = -1*v2
            v2_y = v1

            vertex.append([-20*v2_x,-20*v2_y,0]) #vertex3
            vertex.append([20*v2_x,20*v2_y,0]) #vertex4


        else: 
            if(cross_product(x1, y1, x2, y2, x3, y3)==2):
                print("case1")
                reverseline = 1
                edge.append([lengthOfpol+3,lengthOfpol+1,lengthOfvertex+1,lengthOfvertex+2,lengthOfedge+3,lengthOfedge+2,lengthOfedge+5,lengthOfedge+4,1]) # e1-e6
                edge.append([lengthOfpol+1,lengthOfpol+2,lengthOfvertex+1,lengthOfvertex+3,lengthOfedge+1,lengthOfedge+3,lengthOfedge+6,lengthOfedge+5,1])
                edge.append([lengthOfpol+2,lengthOfpol+3,lengthOfvertex+1,lengthOfvertex+4,lengthOfedge+2,lengthOfedge+1,lengthOfedge+4,lengthOfedge+6,1])
                edge.append([lengthOfpol+3,lengthOfpol+4,lengthOfvertex+2,lengthOfvertex+4,lengthOfedge+1,lengthOfedge+5,lengthOfedge+6,lengthOfedge+3,0])
                edge.append([lengthOfpol+1,lengthOfpol+4,lengthOfvertex+3,lengthOfvertex+2,lengthOfedge+2,lengthOfedge+6,lengthOfedge+4,lengthOfedge+1,0])
                edge.append([lengthOfpol+2,lengthOfpol+4,lengthOfvertex+4,lengthOfvertex+3,lengthOfedge+3,lengthOfedge+4,lengthOfedge+5,lengthOfedge+2,0])
            else:
                print("case2")
                reverseline = -1.

                edge.append([lengthOfpol+1,lengthOfpol+3,lengthOfvertex+1,lengthOfvertex+2,lengthOfedge+2,lengthOfedge+3,lengthOfedge+4,lengthOfedge+5,1]) # e1-e6
                edge.append([lengthOfpol+2,lengthOfpol+1,lengthOfvertex+1,lengthOfvertex+3,lengthOfedge+3,lengthOfedge+1,lengthOfedge+5,lengthOfedge+6,1])
                edge.append([lengthOfpol+3,lengthOfpol+2,lengthOfvertex+1,lengthOfvertex+4,lengthOfedge+1,lengthOfedge+2,lengthOfedge+6,lengthOfedge+4,1])
                edge.append([lengthOfpol+3,lengthOfpol+4,lengthOfvertex+4,lengthOfvertex+2,lengthOfedge+3,lengthOfedge+6,lengthOfedge+5,lengthOfedge+1,0])
                edge.append([lengthOfpol+1,lengthOfpol+4,lengthOfvertex+2,lengthOfvertex+3,lengthOfedge+1,lengthOfedge+4,lengthOfedge+6,lengthOfedge+2,0])
                edge.append([lengthOfpol+2,lengthOfpol+4,lengthOfvertex+3,lengthOfvertex+4,lengthOfedge+2,lengthOfedge+5,lengthOfedge+4,lengthOfedge+3,0])

            circumcenter = calculate_circumcenter(x1, y1, x2, y2, x3, y3)
            #print(f"外心座標：{circumcenter}")
            x = circumcenter[0]
            y = circumcenter[1]
            vertex.append([x,y,1]) #vertex1
            v1 = x3-x1 #正向量
            v2 = y3-y1
            v2_x = -1*v2
            v2_y = v1
    
            vertex.append([20*reverseline*v2_x,20*reverseline*v2_y,0]) #vertex2
          
           

            v1 = x1-x2 #正向量
            v2 = y1-y2
            v2_x = -1*v2
            v2_y = v1
            vector_A = (v1,v2)
            vector_B = (v2_x,v2_y)
            vertex.append([20*reverseline*v2_x,20*reverseline*v2_y,0]) #vertex3

            v1 = x2-x3 #正向量
            v2 = y2-y3
            v2_x = -1*v2
            v2_y = v1
            vector_A = (v1,v2)
            vector_B = (v2_x,v2_y)
            vertex.append([20*reverseline*v2_x,20*reverseline*v2_y,0]) #vertex4)

            polygon.append([lengthOfedge+1])#poligon1-4
            polygon.append([lengthOfedge+2])#poligon1
            polygon.append([lengthOfedge+1])#poligon1
            polygon.append([lengthOfedge+1])#poligon1
    


def showdiagram(edgetmp,vertextmp):
    for m in edgetmp:
        if(m[8]==1):#線真實存在
            v1 = m[2]-1 #startvertex
            v2 = m[3]-1 #endvertex
            rightpointofpoly = polyToPoint(m[0])-1
            leftpointofpoly =  polyToPoint(m[1])-1

            print("leftpologon",leftpointofpoly,"rightpologon",rightpointofpoly)
            middleOfTwoPointX =(point[rightpointofpoly][0]+ point[leftpointofpoly][0])/2
            middleOfTwoPointY =(point[rightpointofpoly][1]+ point[leftpointofpoly][1])/2
            print(point[rightpointofpoly],point[leftpointofpoly],middleOfTwoPointX,middleOfTwoPointY)

            if(vertextmp[v1][2]==0):#vertex start不是真的(代表式向量)

                if(vertextmp[v2][2]==0):#vertex end也不是真的(代表式向量)
                    start_x, start_y =middleOfTwoPointX,middleOfTwoPointY

                elif(vertextmp[v2][2]==1):#vertex end是真的(代表式向量)
                    start_x, start_y =vertextmp[v2][0],vertextmp[v2][1]

                # 定义向量的坐标
                vector_x, vector_y = vertextmp[v1][0],vertextmp[v1][1]
                # 计算终点坐标
                end_x = start_x + 50*vector_x
                end_y = start_y + 50*vector_y
                # 在Canvas上绘制向量
                #canvas.create_oval(start_x - 2, (600-start_y) - 2, start_x + 2, (600-start_y) + 2, fill="red")
                canvas.create_line(start_x, (600-start_y), end_x, (600-end_y), fill="blue", width=2,tags="line")


            if(vertextmp[v2][2]==0):
                if(vertextmp[v1][2]==0):
                    start_x, start_y =middleOfTwoPointX,middleOfTwoPointY

                elif(vertextmp[v1][2]==1):
                    start_x, start_y =vertextmp[v1][0],vertextmp[v1][1]
                

                # 定义向量的坐标
                vector_x, vector_y = vertextmp[v2][0],vertextmp[v2][1]
                # 计算终点坐标
                end_x = start_x + 30*vector_x
                end_y = start_y + 30*vector_y
                # 在Canvas上绘制向量
                print('vector',vector_x,vector_y,v1,v2)
                canvas.create_line(start_x, (600-start_y), end_x, (600-end_y), fill="blue", width=2,tags="line")
            
            
            if(vertextmp[v1][2]==1 and vertextmp[v2][2]==1):
                start_x, start_y = vertextmp[v1][0],vertextmp[v1][1]
                end_x,end_y = vertextmp[v2][0],vertextmp[v2][1]
                
                canvas.create_line(start_x, (600-start_y), end_x, (600-end_y), fill="blue", width=2,tags="line")

    return

#畫convexhill
def showconvexhill(array):
    global point
    for m in array:
        p1 = m[0]
        p2 = m[1]
        print(p1,p2)
        startx = point[p1][0]
        starty = point[p1][1]
        endx = point[p2][0]
        endy = point[p2][1]

        canvas.create_line(startx, (600-starty), endx, (600-endy), fill="green", width=2,tags="line")


def checkdup(x,y):
    for m in y:
        if(m==x):
            return 0
    return 1

# 計算兩直線的交點
def line_intersection(line1, line2):
    #print(line1,line2)
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    # 計算分子和分母
    det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if det == 0:
        return None  # 兩直線平行

    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / det
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / det
    
    result = [px,py]
    #print(result)
    return result

# 判斷點是否在線段上
def on_segment(p, q, r):
    return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))



def borderpoint(middleOfTwoPointX,middleOfTwoPointY,vectorxstart,vectorystart):
    # 封閉線段的端點
    array = []
    p = [[0,0,0,600],[0,0,600,0],[600,0,600,600],[0,600,600,600]]
    # 計算第二個點的坐標
    x2, y2 = middleOfTwoPointX + vectorxstart, middleOfTwoPointY + vectorystart
    
    # 給定的線段的端點
    p2, q2 = (middleOfTwoPointX, middleOfTwoPointY), (x2, y2)

    # 計算交點
    for m in p:
        intersection = line_intersection((m[0], m[1], m[2], m[3]), (p2[0], p2[1], q2[0], q2[1]))
    
        # 檢查交點是否在兩線段上
        if intersection  and on_segment((m[0],m[1]), intersection, (m[2],m[3])) and on_segment(p2, intersection, q2):
            #print("兩線段相交於點：", intersection)
            if(checkdup(intersection,array)):
                array = intersection #最多一個焦點
        else:
            #print("兩線段不相交")
            1
    return array


def outputfile():
    global vertex
    global edge
    outputpoint  =  point
    edgereal = []
    for m in edge:
        if(m[8]==1):
            v1 = m[2]-1 #startvertex
            v2 = m[3]-1 #endvertex
            if(vertex[v1][2]==1):
                if(vertex[v2][2]==0):
                    startx = vertex[v1][0]
                    starty = vertex[v1][1]
                    vectorx = 50*vertex[v2][0]
                    vertory = 50*vertex[v2][1]
                    array = borderpoint(startx,starty,vectorx,vertory)
                    tmp = [startx,starty]
                    edgereal.append(tmp+array)
                elif(vertex[v2][2]==1):
                    startx = vertex[v1][0]
                    starty = vertex[v1][1]
                    endx = vertex[v2][0]
                    endy = vertex[v2][1]
                    edgereal.append([startx,starty,endx,endy])
            elif(vertex[v1][2]==0):
                if(vertex[v2][2]==0):
                    rightpol = m[0]-1
                    leftpol = m[1]-1
                    middleOfTwoPointX =(point[rightpol][0]+ point[leftpol][0])/2
                    middleOfTwoPointY =(point[rightpol][1]+ point[leftpol][1])/2
                    vectorxstart = 50*vertex[v1][0]
                    vectorystart = 50*vertex[v1][1]
                    array1 = borderpoint(middleOfTwoPointX,middleOfTwoPointY,vectorxstart,vectorystart)
                    array2 = borderpoint(middleOfTwoPointX,middleOfTwoPointY,-1*vectorxstart,-1*vectorystart)
                    edgereal.append(array1+array2)
                    
                    
    print("outputfile point and edge",outputpoint,edgereal)
    edgereal.sort()

    file_path = "output.txt"
    try:
        with open(file_path, 'w') as file:
            for item in outputpoint:
                # 將子列表元素轉換為字符串，然後加入文字，再換行
                line = f"P {item[0]} {item[1]}\n"
                file.write(line)
            for item in edgereal:
                # 將子列表元素轉換為字符串，然後加入文字，再換行
                if(item[0]==0):
                    x1 = 0
                else:
                    x1=round(item[0],2)
                if(item[1]==0):
                    y1 = 0
                else:
                    y1=round(item[1],2)
                if(item[2]==0):
                    x2 = 0
                else:
                    x2=round(item[2],2)
                if(item[3]==0):
                    y2 = 0
                else:
                    y2=round(item[3],2)
                if(x1<x2):
                    line = f"E {x1} {y1} {x2} {y2}\n"
                elif(x1==x2):
                    if(y1<=y2):
                        line = f"E {x1} {y1} {x2} {y2}\n"
                    else:
                        line = f"E {x2} {y2} {x1} {y1}\n"
                else:
                    line = f"E {x2} {y2} {x1} {y1}\n"
                
                file.write(line)
        print("成功寫入文件。")
    except IOError as e:
        print(f"寫入文件時出錯：{e}")


def findAllEdgeOfPol(number,k):#number = pol邊號
    global edge
    edgeset = []
    edgePointByPolygon = polygon[number-1][0] #pol隊的第一條邊
    edgestart = polygon[number-1][0]
    print("找出pol所有edge",number)
    node=1
    while(1):
        node+=1
        if(node>=10):
            break
        print(edgePointByPolygon,edge[edgePointByPolygon-1])
        if(edgePointByPolygon > len(edge)):
            break
        #print(edgePointByPolygon,edge[edgePointByPolygon-1][0],edge[edgePointByPolygon-1][1],number,edgeset)
        if(edge[edgePointByPolygon-1][0] == number):  #如果rightpol是pol
            if((edge[edgePointByPolygon-1][8]==1) and (k==0)):
                edgeset.append(edgePointByPolygon)
            elif((edge[edgePointByPolygon-1][8]==0) and (k==1)):
                edgeset.append(edgePointByPolygon)
                print("不存在的邊",edgePointByPolygon)
            edgePointByPolygon = edge[edgePointByPolygon-1][7]
            #print("右")

        elif(edge[edgePointByPolygon-1][1] == number):
            if((edge[edgePointByPolygon-1][8]==1) and (k==0)):
                edgeset.append(edgePointByPolygon)
            elif((edge[edgePointByPolygon-1][8]==0) and (k==1)):
                edgeset.append(edgePointByPolygon)
                print("不存在的邊",edgePointByPolygon)
            edgePointByPolygon = edge[edgePointByPolygon-1][5]
            #print("左")
        else:
            break
        if(edgePointByPolygon == edgestart):
            break
    return edgeset

def is_point_in_range(intersection_x, intersection_y, x2, y2, a2, b2):
    # 判斷交點是否在區間內
    return ((x2 <= intersection_x <= a2) and (y2 <= intersection_y <= b2)) or ((a2 <= intersection_x <= x2) and (b2 <= intersection_y <= y2))


def are_lines_parallel(a1, b1, a2, b2):
    print("are_lines_parallel",a1,b1,a2,b2)
    if a1 * a2 + b1 * b2 == 0:
        return False
   
    # 檢查兩個向量的斜率是否相等
    if ((a1 != 0) and (a2 != 0)):
        return (b1 / a1) == (b2 / a2)
    
    if((a1==0) and (a2==0)):
        return True
    
    if((b2==0) and (b1==0)):
        return True
    
    return False

def find_intersection_point(x1, y1, a1, b1, x2, y2, a2, b2):
    print(x1, y1, a1, b1, x2, y2, a2, b2)
    # 如果兩條線平行，則返回None
    if are_lines_parallel(a1, b1, a2, b2):
        return None
    # 計算交點
    t = (b2 * (x2 - x1) - a2 * (y2 - y1)) / (a1 * b2 - a2 * b1)
    intersection_x = x1 + t * a1
    intersection_y = y1 + t * b1
    return [intersection_x, intersection_y]


def same_sign(num1, num2):

    # 判斷兩數字是否同為正數或同為負數
    print("sign",num1,num2)
    if (num1 >= 0 and num2 >= 0) or (num1 <= 0 and num2 <= 0):
        return True
    else:
        return False

def calculate_vector_direction(a, b):
    # 計算向量的方向（弧度）
    return math.atan2(b, a)


def findThehighestEdge(vextor,x,y,edgesubset,array,check): #check 看現在是往上還是往下

    print("findThehighestEdge",vextor,x,y,edgesubset)
    global edge
    maxwho = -1
    maxx = -10000
    maxy = -10000
    
    for m in edgesubset:

        vertexStoreInEdgeStart = edge[m-1][2]
        vertexStoreInEdgeEnd = edge[m-1][3]

        if(array[vertexStoreInEdgeStart-1][2]==1 and array[vertexStoreInEdgeEnd-1][2]==0):#無限邊和無線邊之焦點
            
            if not(are_lines_parallel(array[vertexStoreInEdgeEnd-1][0], array[vertexStoreInEdgeEnd-1][1], vextor[0], vextor[1])):
                intersection_point=  find_intersection_point(array[vertexStoreInEdgeStart-1][0] ,array[vertexStoreInEdgeStart-1][1] ,array[vertexStoreInEdgeEnd-1][0],array[vertexStoreInEdgeEnd-1][1] , x,y, vextor[0],vextor[1])
                print("有")
                #print("intersection_point",intersection_point,m)
                '''
                canvas.create_oval(vertex[vertexStoreInEdgeStart-1][0] - 2, (600-vertex[vertexStoreInEdgeStart-1][1]) - 2, vertex[vertexStoreInEdgeStart-1][0] + 2, (600-vertex[vertexStoreInEdgeStart-1][1]) + 2, fill="green")
                canvas.create_oval(intersection_point[0] - 2, (600-intersection_point[1]) - 2, intersection_point[0] + 2, (600-intersection_point[1]) + 2, fill="black")
                '''
            else:
                print("平行")
                continue


            if intersection_point:
                if check==0:
                    if((round(intersection_point[1],3)>=round(y,3)) and (same_sign(array[vertexStoreInEdgeEnd-1][1],intersection_point[1]-array[vertexStoreInEdgeStart-1][1])) and (same_sign(array[vertexStoreInEdgeEnd-1][0],intersection_point[0]-array[vertexStoreInEdgeStart-1][0]))):
                        print("intersection_point",intersection_point,m)
                        if(intersection_point[1]>maxy):
                            maxx =  intersection_point[0]
                            maxy = intersection_point[1]
                            maxwho = m
                else:
                    #print(intersection_point[1]<y,same_sign(vertex[vertexStoreInEdgeEnd-1][1],intersection_point[1]-vertex[vertexStoreInEdgeStart-1][1]),same_sign(vertex[vertexStoreInEdgeEnd-1][0],intersection_point[0]-vertex[vertexStoreInEdgeStart-1][0]))
                    if((round(intersection_point[1],3)<=round(y,3)) and (same_sign(array[vertexStoreInEdgeEnd-1][1],intersection_point[1]-array[vertexStoreInEdgeStart-1][1])) and (same_sign(array[vertexStoreInEdgeEnd-1][0],intersection_point[0]-array[vertexStoreInEdgeStart-1][0]))):
                        print("intersection_point[1]<y",intersection_point[1],y)
                        if(intersection_point[1]>maxy):
                            maxx =  intersection_point[0]
                            maxy = intersection_point[1]
                            maxwho = m
            else:
                print("兩條線平行，沒有交點。")
            



        elif(array[vertexStoreInEdgeStart-1][2]==1 and array[vertexStoreInEdgeEnd-1][2]==1):#無限邊和有線邊交點
            print("無限邊vs有限")
            if not(are_lines_parallel(vertex[vertexStoreInEdgeEnd-1][0], vertex[vertexStoreInEdgeEnd-1][1], vextor[0], vextor[1])):
                intersection_point=  find_intersection_point(array[vertexStoreInEdgeStart-1][0] ,array[vertexStoreInEdgeStart-1][1] ,array[vertexStoreInEdgeEnd-1][0],array[vertexStoreInEdgeEnd-1][1], x,y, vextor[0],vextor[1])
                if(is_point_in_range(intersection_point[0], intersection_point[1], array[vertexStoreInEdgeStart-1][0], array[vertexStoreInEdgeStart-1][1], array[vertexStoreInEdgeEnd-1][0], array[vertexStoreInEdgeEnd-1][1])):
                    if(intersection_point[1]>maxy):
                        maxx =  intersection_point[0]
                        maxy = intersection_point[1]
                        maxwho = m

        elif(array[vertexStoreInEdgeStart-1][2]==0 and array[vertexStoreInEdgeEnd-1][2]==0):
            
            print(edge[m-1][1],edge[m-1][0],samepol[-2])
            tmpleftpoint = polyToPoint(edge[m-1][1])
            tmprightpoint = polyToPoint(edge[m-1][0])
            '''
            if(edge[m-1][0]<samepol[-2]):
                tmpleftpoint = edge[m-1][1]-1
                tmprightpoint = edge[m-1][0]-1
            elif(edge[m-1][1]>samepol[-2]):
                tmpleftpoint = edge[m-1][1]-len(samepol)
                tmprightpoint = edge[m-1][0]-len(samepol)
            else:
                tmpleftpoint = edge[m-1][1]-1
                tmprightpoint = edge[m-1][0]-len(samepol)
            '''

            leftpointX = point[tmpleftpoint-1][0]
            leftpointY = point[tmpleftpoint-1][1]

            rightpointX = point[tmprightpoint-1][0]
            rightpointY = point[tmprightpoint-1][1]
            
            midX = (rightpointX + leftpointX)/2
            midy = (rightpointY + leftpointY)/2  

            print("碰到都是無限的邊point",tmpleftpoint,tmprightpoint)
            if (not(are_lines_parallel(array[vertexStoreInEdgeEnd-1][0], array[vertexStoreInEdgeEnd-1][1], vextor[0], vextor[1]))):
                intersection_point=  find_intersection_point(midX,midy,array[vertexStoreInEdgeEnd-1][0],array[vertexStoreInEdgeEnd-1][1] , x,y, vextor[0],vextor[1])
                if intersection_point:
                    if(check == 0):
                        if(round(intersection_point[1],3) >= round(y,3)):
                            if(intersection_point[1]>maxy):
                                maxx =  intersection_point[0]
                                maxy = intersection_point[1]
                                maxwho = m
                            #elif(round(intersection_point[1],3) == round(y,3))and(round(intersection_point[1],3)))
                    elif(check == 1):
                        if(round(intersection_point[1],3) <= round(y,3)):
                            if(intersection_point[1]>=maxy):
                                maxx =  intersection_point[0]
                                maxy = intersection_point[1]
                                maxwho = m
                            
            else:              
                print("無限無限平行")
                continue
    return (maxwho,maxy,maxx)

def finddup(array):
    seen = set()
    result_list = []
    print("find",array)
    for element in array:
        if element not in seen:
            result_list.append(element)
            seen.add(element)
        else:
            result_list.remove(element)

    result_list.sort()

    return result_list

def pointToPoly(x):#丟進來的要是假的出來也是
    tmp = x
    for m in samepol:
        if(x>=m):
            tmp=tmp+1
    print("polyToPoint",x,tmp,"samepol",samepol)
    return tmp

def polyToPoint(x):#近來是假的出來也是假的
    tmp = x
    for m in samepol:
        if(x>m):
            tmp=tmp-1
        print("polyToPoint",x,tmp,"samepol",samepol)
    return tmp



def mergeTwoPolygon(i,t,j,array): #array代表真正的point號碼[1,2]
    global vertex
    global edge
    
    mergeprint()
    mergeEdge = copy.deepcopy(edge)
    mergePolygon = copy.deepcopy(polygon)
    mergeVertex = copy.deepcopy(vertex)
    mergeSamepol = copy.deepcopy(samepol)
    deletevertex = []
    preedge = -1
    


    print("mergeTwoPolygon")

    if(j-i+1<=3):
        edge = copy.deepcopy(mergeEdge)
        vertex = copy.deepcopy(mergeVertex)

    whoishs = 0 #分辨誰是最上面的convexhilledge

    ''''cobvexhill第一邊'''

    firstpolRightToPoint = array[0][1]
    firstpolLeftToPoint = array[0][0]

    firstrightPolOfHsX = point[array[0][1]][0]   #右邊pol之座標X
    firstrightPolOfHsY = point[array[0][1]][1]   #右邊pol之座標Y

    firstleftPolOfHsX = point[array[0][0]][0]     #左邊pol之座標X
    firstleftPolOfHsY = point[array[0][0]][1]     #左邊pol之座標Y

    firstmidofhsX = (firstrightPolOfHsX+firstleftPolOfHsX)/2    #左右pol之中點
    firstmidofhsY = (firstrightPolOfHsY+firstleftPolOfHsY)/2
    
    firsvectorOfHsX = -1*(firstrightPolOfHsY-firstleftPolOfHsY)
    firsvectorOfHsY = firstrightPolOfHsX - firstleftPolOfHsX

    firsvectorUp = (firsvectorOfHsX,firsvectorOfHsY)         #hs x->y左轉
    firsvectorDown = (-1*firsvectorOfHsX,-1*firsvectorOfHsY) #hs x->y右轉

    ''''cobvexhill第二邊'''
    secondpolRightToPoint = array[1][1]
    secondpolLeftToPoint = array[1][0]

    secondrightPolOfHsX = point[array[1][1]][0]   #右邊pol之座標X
    secondrightPolOfHsY = point[array[1][1]][1]   #右邊pol之座標Y

    secondleftPolOfHsX = point[array[1][0]][0]     #左邊pol之座標X
    secondleftPolOfHsY = point[array[1][0]][1]     #左邊pol之座標Y

    secondmidofhsX = (secondrightPolOfHsX+secondleftPolOfHsX)/2    #左右pol之中點
    secondmidofhsY = (secondrightPolOfHsY+secondleftPolOfHsY)/2
    
    secondvectorOfHsX = -1*(secondrightPolOfHsY-secondleftPolOfHsY)
    secondvectorOfHsY = secondrightPolOfHsX - secondleftPolOfHsX

    secondvectorUp = (secondvectorOfHsX,secondvectorOfHsY) 
    secondvectorDown = (-1*secondvectorOfHsX,-1*secondvectorOfHsY) #hs x->y右轉

    if(firstrightPolOfHsY >= secondrightPolOfHsY and firstleftPolOfHsY >= secondleftPolOfHsY):
        polLeftToPoint = pointToPoly(firstpolLeftToPoint+1)
        polRightToPoint = pointToPoly(firstpolRightToPoint+1)

        hpleft = pointToPoly(secondpolLeftToPoint+1)#secondpolLeftToPoint+1
        hpright = pointToPoly(secondpolRightToPoint+1)#secondpolRightToPoint+len(samepol)

        whoishs = 0
        mergeVertex.append([firsvectorUp[0],firsvectorUp[1],0])
        tmpvector = firsvectorUp
    else:
        polLeftToPoint = pointToPoly(secondpolLeftToPoint+1)
        polRightToPoint = pointToPoly(secondpolRightToPoint+1)

        hpleft = pointToPoly(firstpolLeftToPoint+1)#firstpolLeftToPoint+1
        hpright = pointToPoly(firstpolRightToPoint+1)# firstpolRightToPoint+len(samepol)

        mergeVertex.append([secondvectorUp[0],secondvectorUp[1],0])
        tmpvector = secondvectorUp
        whoishs = 1

    print("polLeftToPoint",polLeftToPoint,"polRightToPoint",polRightToPoint,"hpleft",hpleft,"hpright",hpright)

    '''找出左右POL的EDGE'''
    arrayleft = findAllEdgeOfPol(polLeftToPoint,0)#polLeftToPoint+1
    arrayright = findAllEdgeOfPol(polRightToPoint,0) #vertexToPol polRightToPoint+len(samepol)




    print("arrayleft",arrayleft)
    print("arrayRight",arrayright)

    if(whoishs==0):
        
        leftMaxEdge = findThehighestEdge(firsvectorUp,firstmidofhsX,firstmidofhsY,arrayleft,mergeVertex,0)#幾號edge最大(假的邊號)和y是多少
        rightMaxEdge = findThehighestEdge(firsvectorUp,firstmidofhsX,firstmidofhsY,arrayright,mergeVertex,0)
        if(leftMaxEdge and rightMaxEdge):
            if(leftMaxEdge[1]>rightMaxEdge[1]):
                topest = 0
            elif(leftMaxEdge[1]<rightMaxEdge[1]):
                topest = 1
            else:
                topest = 2
            

    elif(whoishs==1):
       
        leftMaxEdge = findThehighestEdge(secondvectorUp,secondmidofhsX,secondmidofhsY,arrayleft,mergeVertex,0)#幾號edge最大(假的邊號)和y是多少
        rightMaxEdge = findThehighestEdge(secondvectorUp,secondmidofhsX,secondmidofhsY,arrayright,mergeVertex,0)
        if(leftMaxEdge and rightMaxEdge):
            if(leftMaxEdge[1]>rightMaxEdge[1]):
                topest = 0
            elif(leftMaxEdge[1]<rightMaxEdge[1]):
                topest = 1
            else:
                topest = 2

    print("找網上找不到")
    if(leftMaxEdge[0]==-1 and rightMaxEdge[0]==-1):
        if(whoishs==0):
            
            leftMaxEdge = findThehighestEdge(firsvectorDown,firstmidofhsX,firstmidofhsY,arrayleft,mergeVertex,1)#幾號edge最大(假的邊號)和y是多少
            rightMaxEdge = findThehighestEdge(firsvectorDown,firstmidofhsX,firstmidofhsY,arrayright,mergeVertex,1)
            if(leftMaxEdge and rightMaxEdge):
                if(leftMaxEdge[1]>rightMaxEdge[1]):
                    topest = 0
                elif(leftMaxEdge[1]<rightMaxEdge[1]):
                    topest = 1
                else:
                    topest = 2
        elif(whoishs==1):
            leftMaxEdge = findThehighestEdge(secondvectorDown,secondmidofhsX,secondmidofhsY,arrayleft,mergeVertex,1)#幾號edge最大(假的邊號)和y是多少
            rightMaxEdge = findThehighestEdge(secondvectorDown,secondmidofhsX,secondmidofhsY,arrayright,mergeVertex,1)
            print("leftMaxEdge",leftMaxEdge,"rightMaxEdge",rightMaxEdge)
            if(leftMaxEdge and rightMaxEdge):
                if(leftMaxEdge[1]>rightMaxEdge[1]):
                    topest = 0
                elif(leftMaxEdge[1]<rightMaxEdge[1]):
                    topest = 1
                else:
                    topest = 2

    """如果都沒有撞到代表都平行"""
    if(leftMaxEdge[0]==-1 and rightMaxEdge[0]==-1):
        print("都平行")
        if(whoishs == 0):
            mergeEdge.append([polRightToPoint,polLeftToPoint,len(mergeVertex)+1,len(mergeVertex),-1,-1,-1,-1,1])
            mergeVertex.append([secondvectorDown[0],secondvectorDown[1],0])
        elif(whoishs == 1):
            mergeEdge.append([polRightToPoint,polLeftToPoint,len(mergeVertex)+1,len(mergeVertex),-1,-1,-1,-1,1])
            mergeVertex.append([firsvectorDown[0],firsvectorDown[1],0])
        topest = 3

    
    
    if(topest == 2):
        print("一樣高")
        mergeEdge.append([polRightToPoint,polLeftToPoint,len(mergeVertex)+1,len(mergeVertex),rightMaxEdge[0],leftMaxEdge[0],-1,-1,1])
    
    if(topest ==0 or topest==2): #代表左邊的edge是最上面的edge
        print("左邊的edge比較高是:",leftMaxEdge)

        edgetmp =    leftMaxEdge[0]
        
        b=(vertex[edge[edgetmp-1][3]-1][0]-vertex[edge[edgetmp-1][2]-1][0],vertex[edge[edgetmp-1][3]-1][1]-vertex[edge[edgetmp-1][2]-1][1])
        a=(tmpvector[0],tmpvector[1])


        if(topest == 0):
            mergeEdge.append([polRightToPoint,polLeftToPoint,len(mergeVertex)+1,len(mergeVertex),len(mergeEdge)+2,edgetmp,-1,-1,1])

       

        if(cross_productbymerge(a, b)<0): 
      
            print("改end")
            
            if (mergeVertex[mergeEdge[edgetmp-1][3]-1][2] == 0) and (mergeVertex[mergeEdge[edgetmp-1][2]-1][2] == 0):
                #mergeEdge[edgetmp-1][3] = mergeEdge[edgetmp-1][2]
                mergeVertex[mergeEdge[edgetmp-1][3]-1][0] = mergeVertex[mergeEdge[edgetmp-1][3]-1][0]*-1
                mergeVertex[mergeEdge[edgetmp-1][3]-1][1] = mergeVertex[mergeEdge[edgetmp-1][3]-1][1]*-1
                righttmp = mergeEdge[edgetmp-1][0]
                lefttmp = mergeEdge[edgetmp-1][1]
                startcw = mergeEdge[edgetmp-1][4]
                startccw = mergeEdge[edgetmp-1][5]
                endcw = mergeEdge[edgetmp-1][6]
                endccw = mergeEdge[edgetmp-1][7]
                mergeEdge[edgetmp-1][0] = lefttmp
                mergeEdge[edgetmp-1][1] = righttmp
                mergeEdge[edgetmp-1][4] = endcw
                mergeEdge[edgetmp-1][5] = endccw
                mergeEdge[edgetmp-1][6] = startcw
                mergeEdge[edgetmp-1][7] = startccw
                mergeEdge[edgetmp-1][7] = len(mergeEdge)+1
                mergeEdge[edgetmp-1][6] = len(mergeEdge)

                deletevertex.append([mergeEdge[edgetmp-1][3],0])#哪個vertex被刪掉
                mergeVertex.append([leftMaxEdge[2],leftMaxEdge[1],1])
                mergeEdge[edgetmp-1][2] = len(mergeVertex)
            else:
                mergeEdge[edgetmp-1][7] = len(mergeEdge)+1
                mergeEdge[edgetmp-1][6] = len(mergeEdge)

                deletevertex.append([mergeEdge[edgetmp-1][3],1])#哪個vertex被刪掉
                mergeVertex.append([leftMaxEdge[2],leftMaxEdge[1],1])
                mergeEdge[edgetmp-1][3] = len(mergeVertex)

        elif(cross_productbymerge(a, b)>0): 
            print("改start")

            mergeEdge[edgetmp-1][5] = len(mergeEdge)+1
            mergeEdge[edgetmp-1][4] = len(mergeEdge)
            
            deletevertex.append([mergeEdge[edgetmp-1][2],0])#哪個vertex被刪掉

            mergeVertex.append([leftMaxEdge[2],leftMaxEdge[1],1])

            mergeEdge[edgetmp-1][2] = len(mergeVertex)



            
            
        
        preedge = edgetmp

        
    if(topest == 1 or topest==2):
        print("右邊的edge比較高是:",rightMaxEdge)

        edgetmp =    rightMaxEdge[0]

        b=(vertex[edge[edgetmp-1][3]-1][0]-vertex[edge[edgetmp-1][2]-1][0],vertex[edge[edgetmp-1][3]-1][1]-vertex[edge[edgetmp-1][2]-1][1])
        a=(tmpvector[0],tmpvector[1])

        if(topest == 1):
            mergeEdge.append([polRightToPoint,polLeftToPoint,len(mergeVertex)+1,len(mergeVertex),edgetmp,len(mergeEdge)+2,-1,-1,1])
        
        #vertex[edge[edgetmp-1][3]-1][0]<rightMaxEdge[2]
        if(cross_productbymerge(a, b)>=0):#改end
            print("改end")

            if(mergeVertex[mergeEdge[edgetmp-1][3]-1][2] == 0) and (mergeVertex[mergeEdge[edgetmp-1][2]-1][2] == 0):
                #mergeEdge[edgetmp-1][3] = mergeEdge[edgetmp-1][2]
                mergeVertex[mergeEdge[edgetmp-1][3]-1][0] = mergeVertex[mergeEdge[edgetmp-1][3]-1][0]*-1
                mergeVertex[mergeEdge[edgetmp-1][3]-1][1] = mergeVertex[mergeEdge[edgetmp-1][3]-1][1]*-1
                righttmp = mergeEdge[edgetmp-1][0]
                lefttmp = mergeEdge[edgetmp-1][1]
                startcw = mergeEdge[edgetmp-1][4]
                startccw = mergeEdge[edgetmp-1][5]
                endcw = mergeEdge[edgetmp-1][6]
                endccw = mergeEdge[edgetmp-1][7]
                mergeEdge[edgetmp-1][0] = lefttmp
                mergeEdge[edgetmp-1][1] = righttmp
                mergeEdge[edgetmp-1][4] = endcw
                mergeEdge[edgetmp-1][5] = endccw
                mergeEdge[edgetmp-1][6] = startcw
                mergeEdge[edgetmp-1][7] = startccw
                mergeEdge[edgetmp-1][6] = len(mergeEdge)+1
                mergeEdge[edgetmp-1][7] = len(mergeEdge)

                deletevertex.append([mergeEdge[edgetmp-1][3],0])#哪個vertex被刪掉
                mergeVertex.append([rightMaxEdge[2],rightMaxEdge[1],1])
                mergeEdge[edgetmp-1][2] = len(mergeVertex)

            else:
                mergeEdge[edgetmp-1][6] = len(mergeEdge)+1
                mergeEdge[edgetmp-1][7] = len(mergeEdge)
                
            
                deletevertex.append([mergeEdge[edgetmp-1][3],1])#哪個vertex被刪掉

                mergeVertex.append([rightMaxEdge[2],rightMaxEdge[1],1])
                mergeEdge[edgetmp-1][3] = len(mergeVertex)


            
            
        elif(cross_productbymerge(a, b)<0):#改start
            print("改start")

            mergeEdge[edgetmp-1][5] = len(mergeEdge)
            mergeEdge[edgetmp-1][4] = len(mergeEdge)+1
            
            deletevertex.append([mergeEdge[edgetmp-1][3],0])#哪個vertex被刪掉

         

            mergeVertex.append([rightMaxEdge[2],rightMaxEdge[1],1])
            mergeEdge[edgetmp-1][2] = len(mergeVertex)

        preedge = edgetmp
    
    if(topest == 2):
        preedge = leftMaxEdge[0]*10+rightMaxEdge[0]
    
    """
    mergeprint()
    """
    mergeprintnew(mergeEdge,mergeVertex)

    #print("hspreedge",preedge)
    k=1
    """中間"""
    if(topest != 3):
        while(not((mergeEdge[len(mergeEdge)-1][0]==hpleft) and (mergeEdge[len(mergeEdge)-1][1]==hpright))):
            print("中間的preedge",preedge)
            edgeprepre = len(mergeEdge)
            if(topest == 2):
                tmpleft=  preedge//10
                tmpright = preedge%10
                #array = finddup([mergeEdge[tmpleft-1][0],mergeEdge[tmpleft-1][1],mergeEdge[tmpright-1][0],mergeEdge[tmpright-1][1]])#找到下一條中垂現在哪兩個pol 有三線共點的時候
                array=[mergeEdge[tmpleft-1][0],mergeEdge[tmpright-1][1]] 
            else:
                array = finddup([mergeEdge[edgeprepre-1][0],mergeEdge[edgeprepre-1][1],mergeEdge[preedge-1][0],mergeEdge[preedge-1][1]])#找到下一條中垂現在哪兩個pol
            print("下一條中垂現在哪兩個pol",array)
            #if((array[0] == hpleft) and (array[1] == hpright)):
            # print("因為找到下一條中垂腺跟hp一樣")
            # break

            leftpol = array[0]
            rightpol = array[1]
            leftpoint = polyToPoint(leftpol)#leftpol
            rightpoint = polyToPoint(rightpol)#rightpol-(len(samepol)-1)
            print("leftpoint",leftpoint,"rightpoint",rightpoint)
            
            leftpositionX = point[leftpoint-1][0]#左邊point x座標 y座標
            leftpositionY = point[leftpoint-1][1]

            if(k==1):
                print("地一次進",mergeEdge[edgeprepre-1][2],mergeVertex[mergeEdge[edgeprepre-1][2]-1])
                positionX = mergeVertex[mergeEdge[edgeprepre-1][2]-1][0]
                positionY = mergeVertex[mergeEdge[edgeprepre-1][2]-1][1]
            else:
                print("後來才進",mergeEdge[edgeprepre-1][3])
                positionX = mergeVertex[mergeEdge[edgeprepre-1][3]-1][0]
                positionY = mergeVertex[mergeEdge[edgeprepre-1][3]-1][1]
            

            rightpositionX = point[rightpoint-1][0]#左邊point x座標 y座標
            rightpositionY = point[rightpoint-1][1]

            midofX = (leftpositionX+rightpositionX)/2    #左右pol之中點
            midofY = (leftpositionY+leftpositionY)/2


            vector = (rightpositionY - leftpositionY,-1*(rightpositionX - leftpositionX))#向量向右轉

            arrayleft = findAllEdgeOfPol(array[0],0)
            arrayright = findAllEdgeOfPol(array[1],0) #vertexToPol
            print("arrayleft",arrayleft,"arrayright",arrayright)

            if(topest != 2):
                for m in range (len(arrayleft)):
                    if(arrayleft[m]==preedge):
                        arrayleft.pop(m)
                        break
            
                for m in range (len(arrayright)):
                    if(arrayright[m]==preedge):
                        arrayright.pop(m)
                        break
            if(topest ==2):
                for m in range (len(arrayleft)): 
                    if(arrayleft[m]==tmpleft):
                        arrayleft.pop(m)
                        break
            
                for m in range (len(arrayright)):
                    if(arrayright[m]==tmpright):
                        arrayright.pop(m)
                        break

            print("arrayleftsecond",arrayleft,"arrayrightsecond",arrayright)

            leftMaxEdge = findThehighestEdge(vector,positionX,positionY,arrayleft,mergeVertex,1)#幾號edge最大(假的邊號)和y是多少
            rightMaxEdge = findThehighestEdge(vector,positionX,positionY,arrayright,mergeVertex,1)

            
            print(leftMaxEdge,rightMaxEdge)

            if(leftMaxEdge[0] == -1 and rightMaxEdge[0]== -1 ):
                print("找不到交點left為",leftMaxEdge,"right為",rightMaxEdge)
                if(whoishs == 1): #hs是第二個 所以hp是第一個
                    mergeVertex.append([firsvectorDown[0],firsvectorDown[1],0])
                else:
                    mergeVertex.append([secondvectorDown[0],secondvectorDown[1],0])

                if(topest==1):
                    mergeEdge.append([hpleft,hpright,mergeEdge[edgeprepre-1][2 if k==1 else 3],len(mergeVertex),mergeEdge[preedge-1][7],preedge,-1,-1,1])
                elif(topest==0):
                    mergeEdge.append([hpleft,hpright,mergeEdge[edgeprepre-1][2 if k==1 else 3],len(mergeVertex),preedge,mergeEdge[preedge-1][6],-1,-1,1])
                elif(topest == 2):
                    mergeEdge.append([hpleft,hpright,mergeEdge[edgeprepre-1][2 if k==1 else 3],len(mergeVertex),mergeEdge[edgeprepre-1][5 if k==1 else 6],mergeEdge[edgeprepre-1][4 if k==1 else 7],-1,-1,1])
                break
            else:
                if(leftMaxEdge[1]>rightMaxEdge[1]):
                    topest = 0
                elif(leftMaxEdge[1]<rightMaxEdge[1]):
                    topest = 1
                else:
                    topest = 2
            
            print("top是誰",topest)

            if(topest == 2):
                mergeEdge.append([array[0],array[1],mergeEdge[edgeprepre-1][2 if k==1 else 3],len(mergeVertex)+1,mergeEdge[edgeprepre-1][5 if k==1 else 6],mergeEdge[edgeprepre-1][4 if k==1 else 7],leftMaxEdge[0],rightMaxEdge[0],1])

            if(topest == 1 or topest == 2): #撞右邊
                
                a = (vertex[edge[rightMaxEdge[0]-1][3]-1][0]-vertex[edge[rightMaxEdge[0]-1][2]-1][0],vertex[edge[rightMaxEdge[0]-1][3]-1][1]-vertex[edge[rightMaxEdge[0]-1][2]-1][1])
                b = vector

                if(topest == 1):
                        mergeEdge.append([array[0],array[1],mergeEdge[edgeprepre-1][2 if k==1 else 3],len(mergeVertex)+1,preedge,mergeEdge[preedge-1][6],rightMaxEdge[0],len(mergeEdge)+2,1])

                #vertex[edge[rightMaxEdge[0]-1][3]-1][0] < rightMaxEdge[2]
                if(cross_productbymerge(a,b)>=0): #改end
                    print("改end")
                    if(mergeVertex[mergeEdge[rightMaxEdge[0]-1][3]-1][2] == 0) and (mergeVertex[mergeEdge[rightMaxEdge[0]-1][2]-1][2] == 0):
                        #mergeEdge[rightMaxEdge[0]-1][3] = mergeEdge[rightMaxEdge[0]-1][2]
                        mergeVertex[mergeEdge[rightMaxEdge[0]-1][3]-1][0] = mergeVertex[mergeEdge[rightMaxEdge[0]-1][3]-1][0]*-1
                        mergeVertex[mergeEdge[rightMaxEdge[0]-1][3]-1][1] = mergeVertex[mergeEdge[rightMaxEdge[0]-1][3]-1][1]*-1
                        rightpoltmp = mergeEdge[rightMaxEdge[0]-1][0]
                        leftpoltmp = mergeEdge[rightMaxEdge[0]-1][1]
                        startcw = mergeEdge[rightMaxEdge[0]-1][4]
                        startccw = mergeEdge[rightMaxEdge[0]-1][5]
                        endcw = mergeEdge[rightMaxEdge[0]-1][6]
                        endccw = mergeEdge[rightMaxEdge[0]-1][7]
                        mergeEdge[rightMaxEdge[0]-1][0] = leftpoltmp
                        mergeEdge[rightMaxEdge[0]-1][1] = rightpoltmp
                        mergeEdge[rightMaxEdge[0]-1][4] = endcw
                        mergeEdge[rightMaxEdge[0]-1][5] = endccw
                        mergeEdge[rightMaxEdge[0]-1][6] = startcw
                        mergeEdge[rightMaxEdge[0]-1][7] = startccw
                        mergeEdge[rightMaxEdge[0]-1][6] = len(mergeEdge)+1
                        mergeEdge[rightMaxEdge[0]-1][7] = len(mergeEdge)

                        deletevertex.append([mergeEdge[rightMaxEdge[0]-1][3],0])#哪個vertex被刪掉
                        mergeVertex.append([rightMaxEdge[2],rightMaxEdge[1],1])
                        mergeEdge[rightMaxEdge[0]-1][2] = len(mergeVertex)
                    
                    else:
                        deletevertex.append([mergeEdge[rightMaxEdge[0]-1][3],0])#哪個vertex被刪掉

                        mergeVertex.append([rightMaxEdge[2],rightMaxEdge[1],1])
                        mergeEdge[rightMaxEdge[0]-1][3] = len(mergeVertex)


                        mergeEdge[rightMaxEdge[0]-1][6] = len(mergeEdge)+1
                        mergeEdge[rightMaxEdge[0]-1][7] = len(mergeEdge)



                elif(cross_productbymerge(a,b)<0):#改start
                    print("改start")
                   
                    deletevertex.append([mergeEdge[rightMaxEdge[0]-1][2],0])#哪個vertex被刪掉
                    
                    
                    
                    mergeVertex.append([rightMaxEdge[2],rightMaxEdge[1],1])
                    mergeEdge[rightMaxEdge[0]-1][2] = len(mergeVertex)

                    mergeEdge[rightMaxEdge[0]-1][5] = len(mergeEdge)
                    mergeEdge[rightMaxEdge[0]-1][4] = len(mergeEdge)+1
                    

                preedge = rightMaxEdge[0]

            if(topest == 0 or topest == 2):#撞左邊
                
                a = (vertex[edge[leftMaxEdge[0]-1][3]-1][0]-vertex[edge[leftMaxEdge[0]-1][2]-1][0],vertex[edge[leftMaxEdge[0]-1][3]-1][1]-vertex[edge[leftMaxEdge[0]-1][2]-1][1])
                b = vector

                if(topest == 0):
                    mergeEdge.append([array[0],array[1],mergeEdge[edgeprepre-1][2 if k==1 else 3],len(mergeVertex)+1,mergeEdge[preedge-1][7],preedge,len(mergeEdge)+2,leftMaxEdge[0],1])

                print(edge[leftMaxEdge[0]-1][2],vertex[edge[leftMaxEdge[0]-1][2]-1][0] ,leftMaxEdge[2])
                #vertex[edge[leftMaxEdge[0]-1][3]-1][0] > leftMaxEdge[2]
                if(cross_productbymerge(a,b)<0): #改end
                    print("改改end")
                    if(mergeVertex[mergeEdge[leftMaxEdge[0]-1][3]-1][2] == 0) and (mergeVertex[mergeEdge[leftMaxEdge[0]-1][2]-1][2] == 0):
                        #mergeEdge[leftMaxEdge[0]-1][3] = mergeEdge[leftMaxEdge[0]-1][2]
                        mergeVertex[mergeEdge[leftMaxEdge[0]-1][3]-1][0] = mergeVertex[mergeEdge[leftMaxEdge[0]-1][3]-1][0]*-1
                        mergeVertex[mergeEdge[leftMaxEdge[0]-1][3]-1][1] = mergeVertex[mergeEdge[leftMaxEdge[0]-1][3]-1][1]*-1
                        rightpoltmp = mergeEdge[leftMaxEdge[0]-1][0]
                        leftpoltmp = mergeEdge[leftMaxEdge[0]-1][1]
                        startcw = mergeEdge[leftMaxEdge[0]-1][4]
                        startccw = mergeEdge[leftMaxEdge[0]-1][5]
                        endcw = mergeEdge[leftMaxEdge[0]-1][6]
                        endccw = mergeEdge[leftMaxEdge[0]-1][7]
                        mergeEdge[leftMaxEdge[0]-1][0] = leftpoltmp
                        mergeEdge[leftMaxEdge[0]-1][0] = rightpoltmp
                        mergeEdge[leftMaxEdge[0]-1][4] = endcw
                        mergeEdge[leftMaxEdge[0]-1][5] = endccw
                        mergeEdge[leftMaxEdge[0]-1][6] = startcw
                        mergeEdge[leftMaxEdge[0]-1][7] = startccw
                        mergeEdge[leftMaxEdge[0]-1][6] = len(mergeEdge)+1
                        mergeEdge[leftMaxEdge[0]-1][7] = len(mergeEdge)

                        deletevertex.append([mergeEdge[leftMaxEdge[0]-1][3],0])#哪個vertex被刪掉
                        mergeVertex.append([leftMaxEdge[2],leftMaxEdge[1],1])
                        mergeEdge[leftMaxEdge[0]-1][2] = len(mergeVertex)
                    
                    else:


                        deletevertex.append([mergeEdge[leftMaxEdge[0]-1][3],1])#哪個vertex被刪掉

                        mergeVertex.append([leftMaxEdge[2],leftMaxEdge[1],1])
                        mergeEdge[leftMaxEdge[0]-1][3] = len(mergeVertex)
                    


                        mergeEdge[leftMaxEdge[0]-1][6] = len(mergeEdge)
                        mergeEdge[leftMaxEdge[0]-1][7] = len(mergeEdge)+1


                elif(cross_productbymerge(a,b)>=0):#改start
                    

                    deletevertex.append([mergeEdge[leftMaxEdge[0]-1][2],0])#哪個vertex被刪掉

                    

                    mergeVertex.append([leftMaxEdge[2],leftMaxEdge[1],1])
                    mergeEdge[leftMaxEdge[0]-1][2] = len(mergeVertex)

                    mergeEdge[leftMaxEdge[0]-1][4] = len(mergeEdge)
                    mergeEdge[leftMaxEdge[0]-1][5] = len(mergeEdge)+1

                preedge = leftMaxEdge[0]

            if(topest == 2):
                preedge = leftMaxEdge[0]*10 + rightMaxEdge[0]
            if k==1:k = 0
        
    mergeprintnew(mergeEdge,mergeVertex)

    "HP"
    #print("hppreedge",preedge)
    #midofX = mergeVertex[mergeEdge[preedge-1][3]-1][0]
    #midofY = vertex[edge[preedge-1][3]-1][1]
    edgeprepre = len(mergeEdge)
    print("edgeprepre",edgeprepre)


    print("'上面兩個pol跟下面兩pol",polLeftToPoint ,polRightToPoint ,hpleft ,hpright)

    
    if(topest!=3):
        arraytmp = findAllEdgeOfPol(polLeftToPoint,1)
        topleft = arraytmp[0]
        arraytmp = findAllEdgeOfPol(polRightToPoint,1)
        topright = arraytmp[0]
        
        arraytmp = findAllEdgeOfPol(hpleft,1)
        bottomleft = arraytmp[0]

        arraytmp = findAllEdgeOfPol(hpright,1)
        bottomright = arraytmp[0]

        print(topleft,topright,bottomleft,bottomright)

        mergeEdge[topleft-1][6] = topright#左上
        mergeEdge[topleft-1][7] = len(edge)+1
        mergeEdge[topleft-1][3] = mergeEdge[len(edge)][3]


        mergeEdge[topright-1][5] = topleft#右上
        mergeEdge[topright-1][4] = len(edge)+1
        mergeEdge[topright-1][2] = mergeEdge[len(edge)][3]

        mergeEdge[bottomleft-1][4] = len(mergeEdge)#左下
        mergeEdge[bottomleft-1][5] = bottomright
        mergeEdge[bottomleft-1][2] = mergeEdge[len(mergeEdge)-1][3]

        mergeEdge[bottomright-1][6] = bottomleft#右下
        mergeEdge[bottomright-1][7] = len(mergeEdge)
        mergeEdge[bottomright-1][3] = mergeEdge[len(mergeEdge)-1][3]
        
        mergeEdge[len(edge)][6] = topleft
        mergeEdge[len(edge)][7] = topright

        mergeEdge[len(mergeEdge)-1][7] = bottomleft
        mergeEdge[len(mergeEdge)-1][6] = bottomright

    elif(topest == 3):
        arraytmp = findAllEdgeOfPol(polLeftToPoint,1)
        topleft = arraytmp[0]
        arraytmp = findAllEdgeOfPol(polRightToPoint,1)
        topright = arraytmp[0]
        
        arraytmp = findAllEdgeOfPol(hpleft,1)
        bottomleft = arraytmp[0]
        arraytmp = findAllEdgeOfPol(hpright,1)
        bottomright = arraytmp[0]

        print(topleft,topright,bottomleft,bottomright)
        mergeEdge[topleft-1][6] = topright#左上
        mergeEdge[topleft-1][7] = len(edge)+1
        mergeEdge[topleft-1][3] = mergeEdge[len(edge)][3]


        mergeEdge[topright-1][5] = topleft#右上
        mergeEdge[topright-1][4] = len(edge)+1
        mergeEdge[topright-1][2] = mergeEdge[len(edge)][3]

        mergeEdge[bottomleft-1][5] = bottomright#左下
        mergeEdge[bottomleft-1][4] = len(mergeEdge)
        mergeEdge[bottomleft-1][2] = mergeEdge[len(mergeEdge)-1][3]

        mergeEdge[bottomright-1][6] = bottomleft#右下
        mergeEdge[bottomright-1][7] = len(mergeEdge)
        mergeEdge[bottomright-1][3] = mergeEdge[len(mergeEdge)-1][3]
        
        mergeEdge[len(edge)][7] = topleft
        mergeEdge[len(edge)][6] = topright

        mergeEdge[len(mergeEdge)-1][5] = bottomleft
        mergeEdge[len(mergeEdge)-1][4] = bottomright
        

    "處理多餘的邊"
    
    print("deletevertex",deletevertex)
    for n in deletevertex:
        mergeVertex[n[0]-1][2] = 0
        for m in range(len(edge)):
            if(mergeEdge[m-1][8]==1):
                if(n[1]==0):
                    if((mergeEdge[m-1][2] == n[0])):
                        mergeEdge[m-1][8] = 0
                elif(n[1]==1):
                    if((mergeEdge[m-1][3] == n[0])):
                        mergeEdge[m-1][8] = 0
   
   
    


    mergeprintnew(mergeEdge,mergeVertex)

    edge = copy.deepcopy(mergeEdge)
    vertex = copy.deepcopy(mergeVertex)

def mergeprint():
    print("mergeprint")
    print("edge")
    for m in range (len(edge)):
        print(m+1,edge[m])

    print("Vertex")
    for m in range (len(vertex)):
        print(m+1,vertex[m])

def mergeprintnew(mergeEdge,mergeVertex):
    print("mergeprintnew")
    print("mergeEdge")
    for m in range (len(mergeEdge)):
        print(m+1,mergeEdge[m])

    print("mergeVertex")
    for m in range (len(mergeVertex)):
        print(m+1,mergeVertex[m])

# run voronoi
def runVoronidiagram(i,k,j):
    global stepBysteparray

    print("runVoronidiagram",i,k,j)
    if(j-i+1<=3):#如果點數小於三 做暴力解
        doviolance(i,k,j)

        #print("edge",edge,"ploy",polygon,"vertex",vertex)
        samepol.append(len(polygon))
        #showdiagram(i,k,j)
        
        array = buildConvexHill(i,k,j)
        print('convexhill and hp',array[0],array[1])
    
        stepBysteparray.append([list(edge),list(vertex),list(array[1])])
        #print("stepBysteparray",stepBysteparray)
        '''
        showdiagram()
        showconvexhill(array[1])
        print("draw point and edge",point,edge)
        #outputfile()
        '''
        
       
    else:
        """左邊"""
        runVoronidiagram(i,(k+i)//2,k)
        

        """右邊"""
        runVoronidiagram(k+1,(k+1+j)//2,j)
        

        """全部"""
        array = buildConvexHill(i,k,j)
        print('convexhill and hp',array[0],array[1])
        mergeTwoPolygon(i,k,j,array[0])

        stepBysteparray.append([list(edge),list(vertex),list(array[1])])
        #outputtextfile() 
  
    return [list(edge),list(vertex),list(array[1])]

def buildConvexHill(i,k,j):
    convexhill = []
    convexhillarray = []
    stack = []
    rowavg = 0
    colavg = 0
    array = [] #hp
    print("buildConvexHill",i,k,j)
    if(j-i+1==2):
        convexhill.append([i,j])
        array = [i,j]
        resultarray = [array,convexhill]
        return resultarray

    else:
        for m in range(i,j+1):
            rowavg = rowavg + point[m][0]
            colavg = colavg + point[m][1]
        centerOfgravity = [int(rowavg/(j-i+1)),int(colavg/(j-i+1))]

        for m in range(i,j+1):
            origin = (centerOfgravity[0], centerOfgravity[1])

            point1 = (point[m][0], point[m][1])

            # 计算点与原点之间的 x 和 y 坐标差值
            delta_x1 = point1[0] - origin[0]
            delta_y1 = point1[1] - origin[1]
            
            # 使用 math.atan2 计算角度（以弧度表示）
            angle1 = math.atan2(delta_y1, delta_x1)

            # 将弧度转换为度数
            angle1_degrees = math.degrees(angle1)

            #("Point 1 相对于原点的角度（度数）:", angle1_degrees)
            if(angle1_degrees<0):
                angle1_degrees = angle1_degrees+360

            convexhillarray.append([round(angle1_degrees,2),m])
            #print(convexhullarray)

        #排列極值(做convexhill)
        #print('convexhullarray',convexhullarray)
        bias = 360 - convexhillarray[0][0]
        for m in convexhillarray:
            m[0] = m[0]+bias
            if(m[0]>=360):
                m[0] = m[0]-360

        convexhillarray.sort()

        #print('convexhillarray',convexhillarray)
        convexhillarray.append([0.0,i])
        stack.append(convexhillarray[0][1])#前兩個先放入stack
        stack.append(convexhillarray[1][1])

        for m in range(2,len(convexhillarray)):
            #print('stack',stack)
            # 計算內積
            flag1 = stack[-1]
            flag2 = stack[-2]
            temp2 =  convexhillarray[m][1] #拿經過排序後的點在inputarray的哪裡
            #print(flag2,flag1,temp2)
            x1 = point[flag1][0] - point[flag2][0]
            y1 = point[flag1][1] - point[flag2][1]
            x2 = point[temp2][0] - point[flag1][0]
            y2 = point[temp2][1] - point[flag1][1]

            dot_product = x1 * y2 - x2 * y1

        

            # 判斷向量的方向
            if dot_product > 0:
                #print("向左轉")
                stack.append(convexhillarray[m][1])
            elif dot_product < 0:
                #print("向右轉")
                stack.pop()
                stack.append(convexhillarray[m][1])
            else:
                #print("沒有轉向")
                stack.append(convexhillarray[m][1])
                #print()

            #print('stack',stack)


        for m in range (len(stack)-1):
            #print(stack[m],stack[m+1])
            maxstack = max(stack[m],stack[m+1])
            minstack = min(stack[m],stack[m+1])
            convexhill.append([minstack,maxstack])
            if(minstack<k and maxstack>k):
                array.append([minstack,maxstack])
            elif(minstack==k):
                array.append([minstack,maxstack])
        
        print('ConvexHill final return array',array)#上下邊
        resultarray = [array,convexhill]
    return resultarray


def checkOverlapPoint():
    global point
    # 使用集合（set）來去除重複的點
    unique_points = []
    seen = set()

    for p in point:
        # 將點轉換為元組，以便放入集合中
        point_tuple = tuple(p)

        if point_tuple not in seen:
            unique_points.append(list(point_tuple))  # 將元組轉換回列表
            seen.add(point_tuple)
    point = unique_points



# Function to be called when the "Run" button is clicked
def run_function():
    global turn 
    global stepBysteparray
    print("Run button clicked")
    checkOverlapPoint()
    point.sort()
    print(point)
    if(len(point)<=1):
        return 
    resultarray = runVoronidiagram(0,((0+len(point)-1)//2),len(point)-1)
    stepBysteparray.append([list(resultarray[0]),list(resultarray[1]),list(resultarray[2])])
    if(turn == 0):
        showdiagram(edge,vertex)
        showconvexhill(resultarray[2])
    #print(stepBysteparray)

# Function to be called when the "Step by Step" button is clicked
def step_by_step_function():
    global turn 
    global stepbystepcount
    turn = 1
    if(stepbystepcount == 0):
        run_function()
    result = recursive_function(len(point))
    print("地回幾次",result,len(stepBysteparray))

    if(stepbystepcount == result):
        canvas.delete("line")
        
        stepEdge = stepBysteparray[-1][0]
        stepVertex = stepBysteparray[-1][1]
        stepconvex = stepBysteparray[-1][2]
        mergeprintnew(stepEdge,stepVertex)
        showdiagram(stepEdge,stepVertex)
        showconvexhill(stepconvex)

    if(stepbystepcount<result):
        canvas.delete("line")
        stepEdge = stepBysteparray[stepbystepcount][0]
        stepVertex = stepBysteparray[stepbystepcount][1]
        stepconvex = stepBysteparray[stepbystepcount][2]
        mergeprintnew(stepEdge,stepVertex)
        showdiagram(stepEdge,stepVertex)
        showconvexhill(stepconvex)
        stepbystepcount+=1
    print("Step by Step button clicked")

# Function to be called when the "Clear" button is clicked
def clear_function():
    print("Clear button clicked")
    clearall()


# Function to be called when the canvas is clicked
def canvas_click(event):
    x, y = event.x, event.y
    x_scaled = (x / canvas.winfo_width()) * 600
    y_scaled = 600 - (y / canvas.winfo_height()) * 600
    x_scaled = round(x_scaled, 2)
    y_scaled = round(y_scaled, 2)
    canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="red")
    # Display the coordinates in the right_area from top to bottom
    right_area.create_text(10, right_area.y, text=f"({x_scaled}, {y_scaled})", anchor="nw")
    right_area.y += 20  # Increase the y-coordinate for the next point

    point.append([x_scaled,y_scaled])
    #print(point)

#讀檔後標點與座標
def drawcanvas(x,y):
    x_scaled = (x / canvas.winfo_width()) * 600
    y_scaled = 600 - (y / canvas.winfo_height()) * 600
    x_scaled = round(x_scaled, 2)
    y_scaled = round(y_scaled, 2)
    canvas.create_oval(x - 2, (600-y) - 2, x + 2, (600-y) + 2, fill="red")
    # Display the coordinates in the right_area from top to bottom
    right_area.create_text(10, right_area.y, text=f"({x}, {y})", anchor="nw")
    right_area.y += 20  # Increase the y-coordinate for the next point



# Function to be called when the "Read File" button is clicked
def read_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r",encoding="utf-8") as file:
            data = file.readlines()
        process_data(data)


# Process the data (example: print it)
def process_data(data):
    global stored_data
    global point

    for line in data:
        line = line.strip()  # Remove leading and trailing whitespace
        if line and not line.startswith('#'):  # 檢查行不是空的且不以 "#" 開頭:  # Check if the line is not empty
            filtered_line = re.sub(r'[^0-9. ]', '', line)
            if filtered_line:  # Check if the filtered line is not empty
                #print(len(filtered_line))
                if(len(filtered_line)<=2):
                    stored_data.append(int(filtered_line))
                else: 
                    tmp = filtered_line.split(' ')
                    stored_data.append([float(tmp[0]),float(tmp[1])])
                   
    
    tmp = stored_data[0]+1
    for i in range(0,stored_data[0]):
        #print(stored_data[i+1][0],stored_data[i+1][1],i)
        point.append(stored_data[i+1])
        drawcanvas(point[i][0],point[i][1])
    stored_data = stored_data[tmp:]
    print(point,stored_data)


def import_function():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.readlines()

        p_numbers = []  # 創建一個空列表來存放 'p' 開頭的數字
        e_numbers = []  # 創建一個空列表來存放 'e' 開頭的數字

        current_list = None  # 用於追蹤當前的列表

        for line in data:
            parts = line.split()  # 切分每一行的內容，以空格分隔
            if parts:
                if parts[0] == 'P':
                    if current_list != p_numbers:
                        current_list = p_numbers
                    current_list.append([float(parts[1]), float(parts[2])])
                elif parts[0] == 'E':
                    if current_list != e_numbers:
                        current_list = e_numbers
                    current_list.append([float(parts[1]), float(parts[2]),float(parts[3]),float(parts[4])])

        # 打印提取的 'p' 和 'h' 開頭的數字
        #print("p_numbers:", p_numbers)
        #print("e_numbers:", e_numbers)

        for m in p_numbers:
            drawcanvas(m[0],m[1])
        
        for m in e_numbers:
            start_x = m[0]
            start_y = m[1]
            end_x  = m[2]
            end_y = m[3]
            canvas.create_line(start_x, (600-start_y), end_x, (600-end_y), fill="blue", width=2)


    
# Function to be called when the "Next" button is clicked
def next_function():
    global stored_data
    global point
    # Implement the functionality for the "Next" button here
    print("Next button clicked")
    #print(stored_data)
    clearall()


    tmp = stored_data[0]+1
    if stored_data:
        if(stored_data[0]==0):
            right_area.create_text(10, right_area.y, text=f"end", anchor="nw")
        for m in range(0,stored_data[0]):
            point.append(stored_data[m+1])
            drawcanvas(point[m][0],point[m][1])
        stored_data = stored_data[tmp:]
       # print(point,stored_data)

def clearall():
    global point
    global edge
    global polygon
    global vertex
    global samepol
    global stepbystepcount
    global turn
    
    samepol.clear()
    point.clear()
    edge.clear()
    polygon.clear()
    vertex.clear()
    canvas.delete("all")
    right_area.delete("all")
    right_area.y =0
    stepBysteparray.clear()
    stepbystepcount =0
    turn =0

# Create a main window
root = tk.Tk()

# Set the window title
root.title("Voronoi Diagram")

# Set the window size to 900x900
root.geometry("900x900")

# Create "Run" button
run_button = tk.Button(root, text="Run", command=run_function, width=10)
run_button.pack()

# Create "Step by Step" button
step_by_step_button = tk.Button(root, text="Step by Step", command=step_by_step_function, width=10)
step_by_step_button.pack()

# Create "Clear" button
clear_button = tk.Button(root, text="Clear", command=clear_function, width=10)
clear_button.pack()

# Create a "Read File" button with fixed width and height
read_file_button = tk.Button(root, text="Read File", command=read_file, width=10)
read_file_button.pack()

# Create a "Read File" button with fixed width and height
next_button = tk.Button(root, text="Next", command=next_function, width=10)
next_button.pack()

# Create a "Import" button with fixed width and height
import_button = tk.Button(root, text="Import file", command=import_function, width=10)
import_button.pack()

# Create a canvas for the 600x600 area
canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

# Bind the click event to the canvas
canvas.bind("<Button-1>", canvas_click)

# Create an area to the right of the canvas with a size of 600x100
right_area = tk.Canvas(root, width=600, height=600, bg="white")
right_area.place(x=790, y=80, anchor="nw")
right_area.y = 10

# Create a list to store the data read from the file
stored_data = []

# Create a list (array) to store the points
point = []

# Start the main event loop
root.mainloop()


