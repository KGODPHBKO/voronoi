import tkinter as tk
from tkinter import filedialog
import math
import re

edge = []
polygon = []
vertex =[]

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


#暴力解
def doviolance(i,k,j):
  
    global edge
    global polygon
    global vertex
   
    reverseline = 1; #法向量方向

    x1=point[i][0]
    y1=point[i][1]
    x2=point[k][0]
    y2=point[k][1]
    x3=point[j][0]
    y3=point[j][1]

    if(j-i+1==2):
    
        edge.append([2,1,1,2,2,3,2,3,1])#最後一bit 線是真還是無窮遠 e1
        edge.append([3,2,1,2,3,1,1,3,0])#e2
        edge.append([1,3,1,2,1,2,2,1,0])#e3
        
        polygon.append([1])#poligon1
        polygon.append([1])#poligon2
        polygon.append([2])#poligon3
       

        v1 = x3-x1 #正向量
        v2 = y3-y1
        v2_x = -1*v2
        v2_y = v1

        vertex.append([v2_x,v2_y,0,1]) #vertex1
        vertex.append([-1*v2_x,-1*v2_y,0,1]) #vertex2
        print(vertex)
    
    elif(j-i+1==3):
        if(are_points_collinear(x1,y1,x2,y2,x3,y3)):
            edge.append([2,1,1,2,3,5,4,5,1]) # e1-e6
            edge.append([3,2,3,4,6,3,6,4,1])
            edge.append([2,4,1,3,5,1,3,2,0])
            edge.append([4,2,4,2,6,2,1,5,0])
            edge.append([4,1,2,1,4,1,1,3,0])
            edge.append([4,3,3,4,2,6,2,4,0])
        
            polygon.append([1])#poligon1-4
            polygon.append([1])#poligon1
            polygon.append([2])#poligon1
            polygon.append([6])#poligon1


            v1 = x2-x1 #正向量
            v2 = y2-y1
            v2_x = -1*v2
            v2_y = v1

            vertex.append([v2_x,v2_y,0,1]) #vertex1
            vertex.append([-1*v2_x,-1*v2_y,0,1]) #vertex2

            v1 = x3-x2 #正向量
            v2 = y3-y2
            v2_x = -1*v2
            v2_y = v1

            vertex.append([v2_x,v2_y,0,1]) #vertex3
            vertex.append([-1*v2_x,-1*v2_y,0,1]) #vertex4


        else:
            edge.append([3,1,1,2,3,2,4,5,1]) # e1-e6
            edge.append([1,2,1,3,1,3,5,6,1])
            edge.append([2,3,1,4,2,1,6,4,1])
            edge.append([4,3,4,2,6,3,1,5,0])
            edge.append([1,4,2,3,1,4,2,6,0])
            edge.append([4,2,3,4,5,2,3,4,0])

            polygon.append([1])#poligon1-4
            polygon.append([2])#poligon1
            polygon.append([1])#poligon1
            polygon.append([1])#poligon1 

            circumcenter = calculate_circumcenter(x1, y1, x2, y2, x3, y3)
            print(f"外心座標：{circumcenter}")
            x = circumcenter[0]
            y = circumcenter[1]
            vertex.append([x,y,1,1]) #vertex1

            if(cross_product(x1, y1, x2, y2, x3, y3)==2):
                print("case1")
                reverseline = 1
            else:
                print("case2")
                reverseline = -1

            v1 = x3-x1 #正向量
            v2 = y3-y1
            v2_x = -1*v2
            v2_y = v1
    
            vertex.append([reverseline*v2_x,reverseline*v2_y,0,1]) #vertex2
          
           

            v1 = x1-x2 #正向量
            v2 = y1-y2
            v2_x = -1*v2
            v2_y = v1
            vector_A = (v1,v2)
            vector_B = (v2_x,v2_y)
            vertex.append([reverseline*v2_x,reverseline*v2_y,0,2]) #vertex3

            v1 = x2-x3 #正向量
            v2 = y2-y3
            v2_x = -1*v2
            v2_y = v1
            vector_A = (v1,v2)
            vector_B = (v2_x,v2_y)
            vertex.append([reverseline*v2_x,reverseline*v2_y,0,3]) #vertex4)
    






        





def showdiagram():
    for m in edge:
        if(m[8]==1):#線真實存在
            v1 = m[2]-1 #startvertex
            v2 = m[3]-1 #endvertex
            rightpologon = m[0]-1 #pologon代表的是第幾個point
            leftpologon = m[1]-1
            middleOfTwoPointX =(point[rightpologon][0]+ point[leftpologon][0])/2
            middleOfTwoPointY =(point[rightpologon][1]+ point[leftpologon][1])/2
            print(point[rightpologon],point[leftpologon],middleOfTwoPointX,middleOfTwoPointY)

            if(vertex[v1][2]==0):#vertex start不是真的(代表式向量)

                if(vertex[v2][2]==0):#vertex end也不是真的(代表式向量)
                    start_x, start_y =middleOfTwoPointX,middleOfTwoPointY

                elif(vertex[v2][2]==1):#vertex end是真的(代表式向量)
                    start_x, start_y =vertex[v2][0],vertex[v2][1]

                # 定义向量的坐标
                vector_x, vector_y = vertex[v1][0],vertex[v1][1]
                # 计算终点坐标
                end_x = start_x + 50*vector_x
                end_y = start_y + 50*vector_y
                # 在Canvas上绘制向量
                #canvas.create_oval(start_x - 2, (600-start_y) - 2, start_x + 2, (600-start_y) + 2, fill="red")
                canvas.create_line(start_x, (600-start_y), end_x, (600-end_y), fill="blue", width=2,arrow=tk.LAST)


            if(vertex[v2][2]==0):
                if(vertex[v1][2]==0):
                    start_x, start_y =middleOfTwoPointX,middleOfTwoPointY

                elif(vertex[v1][2]==1):
                    start_x, start_y =vertex[v1][0],vertex[v1][1]
                

                # 定义向量的坐标
                vector_x, vector_y = vertex[v2][0],vertex[v2][1]
                # 计算终点坐标
                end_x = start_x + 30*vector_x
                end_y = start_y + 30*vector_y
                # 在Canvas上绘制向量
                print('vector',vector_x,vector_y,v1,v2)
                canvas.create_line(start_x, (600-start_y), end_x, (600-end_y), fill="blue", width=2,arrow=tk.LAST)
            
            
            if(vertex[v1][2]==1 and vertex[v2][2]==1):
                start_x, start_y = vertex[v1][0],vertex[v1][1]
                end_x,end_y = vertex[v2][0],vertex[v2][1]
                
                canvas.create_line(start_x, (600-start_y), end_x, (600-end_y), fill="blue", width=2,arrow=tk.LAST)

    return

#畫convexhill
def showconvexhill(array):
    global point
    for m in array:
        p1 = m[0]
        p2 = m[1]
        print(p1,p2)
        startx = point[p1-1][0]
        starty = point[p1-1][1]
        endx = point[p2-1][0]
        endy = point[p2-1][1]

        canvas.create_line(startx, (600-starty), endx, (600-endy), fill="green", width=2)


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


# run voronoi
def runVoronidiagram(i,k,j):
    
    if(j-i+1<=3):#如果點數小於三 做暴力解
        doviolance(i,k,j)
        array = buildConvexHill(i,k,j)
        print('convexhill and hp',array[0],array[1])
        showdiagram()
        showconvexhill(array[1])
        print(point,edge)
        outputfile()
    else:
        print()
    
    #outputtextfile()

def buildConvexHill(i,k,j):
    convexhill = []
    convexhillarray = []
    stack = []
    rowavg = 0
    colavg = 0
    array = [] #hp

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

        for m in range(0,j+1):
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
        convexhillarray.append([0.0,0])
        stack.append(convexhillarray[0][1])#前兩個先放入stack
        stack.append(convexhillarray[1][1])

        for m in range(2,len(convexhillarray)):
            print('stack',stack)
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
            print(stack[m],stack[m+1])
            maxstack = max(stack[m],stack[m+1])
            minstack = min(stack[m],stack[m+1])
            convexhill.append([minstack+1,maxstack+1])
            if(minstack<k and maxstack>k):
                array.append([minstack+1,maxstack+1])
            elif(minstack==k):
                array.append([minstack+1,maxstack+1])
        
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
    print("Run button clicked")
    checkOverlapPoint()
    point.sort()
    print(point)
    if(len(point)<=1):
        return 
    runVoronidiagram(0,(0+len(point)//2),len(point)-1)

# Function to be called when the "Step by Step" button is clicked
def step_by_step_function():
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
    print(point)

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
            filtered_line = re.sub(r'[^0-9\s]', '', line)
            if filtered_line:  # Check if the filtered line is not empty
                #print(len(filtered_line))
                if(len(filtered_line)<=2):
                    stored_data.append(int(filtered_line))
                else: 
                    tmp = filtered_line.split(' ')
                    stored_data.append([int(tmp[0]),int(tmp[1])])
    #print(stored_data)
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
        print("p_numbers:", p_numbers)
        print("e_numbers:", e_numbers)

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
    point.clear()
    edge.clear()
    polygon.clear()
    vertex.clear()
    canvas.delete("all")
    right_area.delete("all")
    right_area.y =0

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


