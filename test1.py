import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("绘制向量")

# 创建Canvas，设置宽度和高度
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# 定义起点坐标
start_x, start_y = 225, 150

# 定义向量的坐标
vector_x, vector_y = -100, 50  # 以向右为正方向，向上为正方向

# 计算终点坐标
end_x = start_x + vector_x
end_y = start_y + vector_y  # 这里向上为正方向，所以要减去向量y坐标

# 在Canvas上绘制向量
canvas.create_line(start_x, 600 - start_y, end_x, 600 - end_y, fill="blue", width=2, arrow=tk.LAST)

# 启动主循环
root.mainloop()
