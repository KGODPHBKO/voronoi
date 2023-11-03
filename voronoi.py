import tkinter as tk
from tkinter import filedialog

edge = []
polygon = []
vertex = []

#看左轉右轉
def is_left_turn(vector_A, vector_B):
    dot_product = vector_A[0] * vector_B[1] + vector_A[1] * vector_B[0]
    print('轉彎',vector_A,vector_B)
    if dot_product > 0: #左轉
        print('左轉')
        return 1
    elif dot_product < 0: #右轉
        print('右轉')
        return 2
    else:
        return 0
    
#算外心
def calculate_circumcenter(x1, y1, x2, y2, x3, y3):
    #// 計算分母D，以確保不會除以零
    D = 2 * ((x1 - x2) * (y2 - y3) - (y1 - y2) * (x2 - x3))
    # // 計算外心的x和y座標
    x = ((y2 - y3) * (x1 * x1 + y1 * y1 - x2 * x2 - y2 * y2) -(y1 - y2) * (x2 * x2 + y2 * y2 - x3 * x3 - y3 * y3)) / D

    y = ((x1 - x2) * (x2 * x2 + y2 * y2 - x3 * x3 - y3 * y3) -(x2 - x3) * (x1 * x1 + y1 * y1 - x2 * x2 - y2 * y2)) / D


    return (x, y)


#暴力解
def doviolance(i,k,j):
    global edge
    global polygon
    global vertex

    x1=point[i][0]
    y1=point[i][1]
    x2=point[k][0]
    y2=point[k][1]
    x3=point[j][0]
    y3=point[j][1]

    if(j-i+1==2):
    
        edge.append([2,1,1,2,2,3,3,2,1])#最後一bit 線是真還是無窮遠 e1
        edge.append([3,2,1,2,2,3,3,2,0])#e2
        edge.append([1,3,1,2,2,3,3,2,0])#e3
        
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
        if(x1==x2==x3) or (y1==y2==y3):
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

            v1 = x3-x1 #正向量
            v2 = y3-y1
            v2_x = -1*v2
            v2_y = v1
            vector_A = (v1,v2)
            vector_B = (v2_x,v2_y)
            vertex.append([v2_x,v2_y,0,1]) #vertex2
          
           

            v1 = x1-x2 #正向量
            v2 = y1-y2
            v2_x = -1*v2
            v2_y = v1
            vector_A = (v1,v2)
            vector_B = (v2_x,v2_y)
            vertex.append([v2_x,v2_y,0,2]) #vertex3

            v1 = x2-x3 #正向量
            v2 = y2-y3
            v2_x = -1*v2
            v2_y = v1
            vector_A = (v1,v2)
            vector_B = (v2_x,v2_y)
            vertex.append([v2_x,v2_y,0,3]) #vertex4)






        





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
                end_x = start_x + 10*vector_x
                end_y = start_y + 10*vector_y
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
                end_x = start_x + 10*vector_x
                end_y = start_y + 10*vector_y
                # 在Canvas上绘制向量
                print('vector',vector_x,vector_y,v1,v2)
                canvas.create_line(start_x, (600-start_y), end_x, (600-end_y), fill="blue", width=2,arrow=tk.LAST)
            
            
            if(vertex[v1][2]==1 and vertex[v2][2]==1):
                start_x, start_y = vertex[v1][0],vertex[v1][1]
                end_x,end_y = vertex[v2][0],vertex[v2][1]
                
                canvas.create_line(start_x, (600-start_y), end_x, (600-end_y), fill="blue", width=2,arrow=tk.LAST)

    return

# run voronoi
def runVoronidiagram(i,k,j):
    
    if(j-i+1<=3):#如果點數小於三 做暴力解
        point.sort()
        doviolance(i,k,j)
        showdiagram()
    else:
        print()

# Function to be called when the "Run" button is clicked
def run_function():
    print("Run button clicked")
    runVoronidiagram(0,(0+len(point)//2),len(point)-1)

# Function to be called when the "Step by Step" button is clicked
def step_by_step_function():
    print("Step by Step button clicked")

# Function to be called when the "Clear" button is clicked
def clear_function():
    print("Clear button clicked")
    canvas.delete("all")  # Clears all items on the canvas\
    point.clear()


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
        with open(file_path, "r") as file:
            data = file.readlines()
        process_data(data)
    
                        
# Process the data (example: print it)
def process_data(data):
    global stored_data
    global point
    for line in data:
        line = line.strip()  # Remove leading and trailing whitespace
        if line:  # Check if the line is not empty
            if(len(line)==1):
                stored_data.append(int(line))
            else: 
                tmp = line.split(' ')
                stored_data.append([int(tmp[0]),int(tmp[1])])
    #print(stored_data)
    tmp = stored_data[0]+1
    for i in range(0,stored_data[0]):
        #print(stored_data[i+1][0],stored_data[i+1][1],i)
        point.append(stored_data[i+1])
        drawcanvas(point[i][0],point[i][1])
    stored_data = stored_data[tmp:]
    print(point,stored_data)
    '''
    drawcanvas(point[0][0],point[0][1])
    drawcanvas(point[1][0],point[1][1])
    '''


    
# Function to be called when the "Next" button is clicked
def next_function():
    global stored_data
    global point
    # Implement the functionality for the "Next" button here
    print("Next button clicked")
    #print(stored_data)
    point.clear()
    tmp = stored_data[0]+1
    if stored_data:
        if(stored_data[0]==0):
            right_area.create_text(10, right_area.y, text=f"end", anchor="nw")
        for m in range(0,stored_data[0]):
            point.append(stored_data[m+1])
        stored_data = stored_data[tmp:]
       # print(point,stored_data)



# Create a main window
root = tk.Tk()

# Set the window title
root.title("GUI with Buttons and Clickable Area")

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


