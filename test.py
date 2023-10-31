import tkinter as tk  
import numpy as np
import math
from sympy import symbols, Eq, solve

inputarray = []
VorronoiDiagramEdge = []
convexhilledge = []
crosspoint = []

#convexhill
def ConvexHull(inputarray,i,k,j):
    print('ConvexHill',i,k,j)
    stack = []
    angle = []
    convexhullarray = []
    rowavg = 0
    colavg = 0
    array = [] #記錄行跨兩圖之線
    #如果只有兩點
    if(j-i+1==2):
        array.append([i,j])
        print('ConvexHill final return array',array)
        return array


    #算convexhill重心
    for m in inputarray :
        rowavg = rowavg + m[0]
        colavg = colavg + m[1]
    centerOfgravity = np.array([int(rowavg/(j-i+1)),int(colavg/(j-i+1))])#重心
    #print('center of gravity' ,centerOfgravity)

    #到各點向量(算及座標來看要從誰開始)
    for m in range(0,j+1):

        origin = (centerOfgravity[0], centerOfgravity[1])

        # 定义其他点
        point1 = (inputarray[m][0], inputarray[m][1])

        # 计算点与原点之间的 x 和 y 坐标差值
        delta_x1 = point1[0] - origin[0]
        delta_y1 = point1[1] - origin[1]


        # 使用 math.atan2 计算角度（以弧度表示）
        angle1 = math.atan2(delta_y1, delta_x1)

        # 将弧度转换为度数
        angle1_degrees = math.degrees(angle1)

        # 打印点相对于原点的角度（以度数表示）
        #("Point 1 相对于原点的角度（度数）:", angle1_degrees)
        if(angle1_degrees<0):
            angle1_degrees = angle1_degrees+360

        convexhullarray.append([round(angle1_degrees,2),m])
        #print(convexhullarray)

    #排列極值(做convexhill)
    #print('convexhullarray',convexhullarray)
    bias = 360 - convexhullarray[0][0]
    for m in convexhullarray:
        m[0] = m[0]+bias
        if(m[0]>=360):
            m[0] = m[0]-360

    convexhullarray.sort()

    print('biasconvexhullarray',convexhullarray)
    convexhullarray.append([0.0,0])
    stack.append(convexhullarray[0][1])#前兩個先放入stack
    stack.append(convexhullarray[1][1])
    #print('stack',stack)
    for m in range(2,len(convexhullarray)):
        print('stack',stack)
        # 計算內積
        flag1 = stack[-1]
        flag2 = stack[-2]
        temp2 =  convexhullarray[m][1] #拿經過排序後的點在inputarray的哪裡
        print(flag2,flag1,temp2)
        x1 = inputarray[flag1][0] - inputarray[flag2][0]
        y1 = inputarray[flag1][1] - inputarray[flag2][1]
        x2 = inputarray[temp2][0] - inputarray[flag1][0]
        y2 = inputarray[temp2][1] - inputarray[flag1][1]

        dot_product = x1 * y2 - x2 * y1

        

        # 判斷向量的方向
        if dot_product > 0:
            print("向左轉")
            stack.append(convexhullarray[m][1])
        elif dot_product < 0:
            print("向右轉")
            stack.pop()
            stack.append(convexhullarray[m][1])
        else:
            print("沒有轉向")
            stack.append(convexhullarray[m][1])
            print()

        #print('stack',stack)


    for m in range (len(stack)-1): #算連接兩convex之上下邊
        print(stack[m],stack[m+1])
        maxstack = max(stack[m],stack[m+1])
        minstack = min(stack[m],stack[m+1])
        array.append([minstack,maxstack])
    print('ConvexHill final return array',array)
    return array



#找重複
def findDup(x,edge):
    for i in edge:
        if(i == x):
            return 0
    return 1
 
    

def findHsHp(convexhilledge,inputarray,i,k,j):
    print('findHsHp',i,k,j)
    hshp = []
    array = ConvexHull(inputarray,i,k,j)
    for m in array:
        if(findDup(m,convexhilledge)):
            convexhilledge.append(m)
        if(m[0]<k and m[1]>k):
            hshp.append([m[0],m[1]])
        elif(m[0]==k):
            hshp.append([m[0],m[1]])
    return hshp
    


def setVorronoiDiagramEdge(convexhilledge,hshpline):
    for i in convexhilledge:
        if(findDup(i,hshpline)):
            if findDup(i,VorronoiDiagramEdge):
                VorronoiDiagramEdge.append(i)


def buildmiddleline(edge):
    array = []
    for i in edge:
        x1 = inputarray[i[0]][0]
        x2 = inputarray[i[1]][0]
        y1 = inputarray[i[0]][1]
        y2 = inputarray[i[1]][1]
        
        slope = (y2 - y1) / (x2 - x1)
        perpendicular_slope = -1 / slope
        xmid = (x1 + x2) / 2
        ymid = (y1 + y2) / 2
        b = round(ymid - perpendicular_slope * xmid,2)
        array.append([round(perpendicular_slope,2),b,i[0],i[1]])
    return array


def findsol(hs,edgeset):
    print("findsol",hs,edgeset)
    maxy = 0 #再找相交點時取最高的
    maxx = 0
    maxnumber = 0 #看是誰最高要回去VorronoiDiagramEdge找
    tmp = 0
    # 定义符号
    x, y = symbols('x y')
    a1 = -1*hs[0]
    b1 = hs[1]
    equation1 = Eq(a1*x + y, b1)
    for m in edgeset:
        a2 = -1*m[0]
        b2 = m[1]
        # 定义两个方程
        equation2 = Eq(a2*x + y, b2)

        # 解决方程组
        solutions = solve((equation1, equation2), (x, y))
 
        print("方程1:", equation1)
        print("方程2:", equation2)
        print("方程组的解:", solutions)##找出相交點
        if(solutions[y]>=maxy):
            maxy = solutions[y]
            maxx = solutions[x]
            maxnumber = tmp
        tmp+=1

    print(edgeset)
    #crossbywho = [edgeset[maxnumber-1][2],edgeset[maxnumber-1][3]]
    #crosspoint.append([round(maxx,2),round(maxy,2),crossbywho])
    return 



#和並倆圖找出現
def mergetodiagram(VorronoiDiagramEdge,hshpline,k):
    print('mergetodiagram')
    array1 = buildmiddleline(VorronoiDiagramEdge) #找出中垂線之方程式y=ax+b
    array2 = buildmiddleline(hshpline)
    # array1 = buildmiddleline(VorronoiDiagramEdge) #找出中垂線之方程式y=ax+b
    print(array1[0],' ',array2) #找出hs與所有edge之交點取y最大當地一個碰到的
    

    tmp=array2[0]
    findsol(tmp,array1) #撞到哪條線

    







#vorronoi diagram
def RunVorronoiDiagram(VorronoiDiagramEdge,inputarray,i,j):
    print('RunVorronoiDiagram ',i,j)
    array = []
    if(i==j):
        return array
    
    resultRight = RunVorronoiDiagram(VorronoiDiagramEdge,inputarray,i,int((j+i)/2))
    resultLeft = RunVorronoiDiagram(VorronoiDiagramEdge,inputarray,int((j+i)/2)+1,j)
    hshpline = findHsHp(convexhilledge,inputarray,i,int((j+i)/2),j) #找出hshp 和convexhilledge

    print('convexedge',i,j,convexhilledge,'hshpline',hshpline)
    setVorronoiDiagramEdge(convexhilledge,hshpline)#不包含hshp兩edge中點
    print('VorronoiDiagramEdge',VorronoiDiagramEdge)
    mergetodiagram(VorronoiDiagramEdge,hshpline,int((j+i)/2))
    
        


    


#點到的座標
def motion(event):
    print(event.x,600-event.y)
    row = int(event.x)
    col = int(600-event.y)
    if(event.x<=600 and event.x>=0 and event.y<=600 and event.y>=0):
        inputarray.append([row,col])
        canvas.create_rectangle(event.x, event.y, event.x+5, event.y+5,fill='#000')
        if(event.x>=500):
            canvas.create_text(event.x-50, event.y+6, text='('+str(event.x)+','+str(600-event.y)+')', anchor='nw')
        else:
            canvas.create_text(event.x, event.y+6, text='('+str(event.x)+','+str(600-event.y)+')', anchor='nw')
    
        
#案GUI上的按鈕
def pressrunbtn():
    print('pressrunbtn')
    inputarray.sort()
    print(inputarray)
    RunVorronoiDiagram(VorronoiDiagramEdge,inputarray,0,len(inputarray)-1)

    
def pressstepbystepbtn():
    print('pressstepbystepbtn')

def pressclearbtn():
    print('pressclearbtn')
    canvas.delete("all")

#設定GUI
win = tk.Tk()        
win.title("tkinter test")
win.geometry("800x800")
win.maxsize(800,800)


#生成run and step bt step按鈕
runbtn = tk.Button(win, text = "Run",command=pressrunbtn)
runbtn.config(width='20', height='2')

stepbystepbtn = tk.Button(win, text = "Step by step",command=pressstepbystepbtn)
stepbystepbtn.config(width='20', height='2')
runbtn.pack()
stepbystepbtn.pack()

#clear 網格
clearbtn = tk.Button(win, text = "Clear",command=pressclearbtn)
clearbtn.config(width='20', height='2')
clearbtn.pack()

#600*600網格
frame = tk.Frame(bg="white",height=600,width=600)
frame.pack()

canvas = tk.Canvas(frame, bg="white",width=600, height=600)
canvas.bind('<Button>', motion)
canvas.pack()


win.mainloop() 

