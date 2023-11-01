import tkinter as tk
from tkinter import filedialog

edge = []
polygon = []
vertex = []

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

    if(k-i+1==2):
    
        edge.append([2,1,1,2,2,3,3,2,1])#最後一bit 線是真還是無窮遠 e1
        edge.append([3,2,1,2,2,3,3,2,0])#e2
        edge.append([1,3,1,2,2,3,3,2,0])#e3
        
        polygon.append([1])#poligon1
        polygon.append([1])#poligon2
        polygon.append([2])#poligon3
        '''
        xavg = (x1+x3)/2
        yavg = (y1+y3)/2

        v1 = x3-x1
        v2 = y3-y1
        v2_x = -1*v2
        v2_y = v1
        d=10
        V_x = xavg + d * v2_x
        V_y = yavg + d * v2_y
        VV_x = xavg - d * v2_x
        VV_y = yavg - d * v2_y
        '''
        v1 = x3-x1 #正向量
        v2 = y3-y1
        v2_x = -1*v2
        v2_y = v1


        vertex.append([v2_x,v2_y,0,1]) #vertex1
        vertex.append([-1*v2_x,-1*v2_y,0,1]) #vertex2
        print(vertex)
    
    elif(k-i+1==3):
        print()

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
            if(vertex[v1][2]==0):
                start_x, start_y =middleOfTwoPointX,middleOfTwoPointY
                # 定义向量的坐标
                vector_x, vector_y = vertex[v1][0],vertex[v1][1]
                # 计算终点坐标
                end_x = start_x + 10*vector_x
                end_y = start_y + 10*vector_y
                # 在Canvas上绘制向量
                canvas.create_line(start_x, start_y, end_x, end_y, fill="blue", width=2,arrow=tk.LAST)
            if(vertex[v2][2]==0):
                start_x, start_y =middleOfTwoPointX,middleOfTwoPointY
                # 定义向量的坐标
                vector_x, vector_y = vertex[v2][0],vertex[v2][1]
                # 计算终点坐标
                end_x = start_x + 10*vector_x
                end_y = start_y + 10*vector_y
                # 在Canvas上绘制向量
                canvas.create_line(start_x, start_y, end_x, end_y, fill="blue", width=2,arrow=tk.LAST)

    return

# run voronoi
def runVoronidiagram(i,k,j):
    if(j-i+1<=3):#如果點數小於三 做暴力解
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

    point.append([x,y])
    print(point)

#讀檔後標點與座標
def drawcanvas(x,y):
    canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="red")
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
    stored_data = stored_data[tmp:]
    print(point,stored_data)
    drawcanvas(point[0][0],point[0][1])
    drawcanvas(point[1][0],point[1][1])

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


