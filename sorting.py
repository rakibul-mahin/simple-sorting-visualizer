'''
This only works for bubble sort, please check later for other algorithms
'''

from tkinter import *
from tkinter import ttk
import random

from sorting_algos import bubble_sort_algo

algo_list = ['Bubble Sort', 'Merge Sort', 'Quick Sort']
data = []

def generate():

    global data

    print("New Data Generated")

    min_value = int(min_val.get())
    max_value = int(max_val.get())
    array_size = int(size_val.get())
    

    data = []
    for data_elemnt in range(array_size):
        random_value = random.randrange(min_value, max_value + 1)
        data.append(random_value)

    draw_data(data, ['#466df0' for c in range(len(data))])

def draw_data(data, color_array):

    canvas.delete("all")

    canvas_height = 450
    canvas_width = 870
    x_width = canvas_width / (len(data) + 1)
    offset = 10
    spacing_between_rect = 5
    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        
        x0 = i * x_width + offset + spacing_between_rect
        y0 = canvas_height - height * 400

        x1 = (i + 1) * x_width
        y1 = canvas_height
        
        canvas.create_rectangle(x0, y0, x1, y1, fill = color_array[i])
        canvas.create_text(
                            x0 + 2,
                            y0,
                            anchor = SW, 
                            text = str(data[i]), 
                            font = ("new roman", 15, "bold"), 
                            fill = "orange"
                        )

    root.update_idletasks()

def start_algo():
    global data
    print("Algorithm: " + select_algo.get())
    sort_speed = int(speed_val.get())
    bubble_sort_algo(data, draw_data, sort_speed)

root = Tk()

root.title('Sorting Visualizer')
root.geometry('900x600+200+80')
root.config(bg='#262729')

selected_algo = StringVar()

algo_label = Label(
                    root, 
                    text = "Sorting Algorithm: ", 
                    font = ("new roman", 12, "bold"), 
                    bg="#909296", 
                    width = 15, 
                    fg = "red", 
                    relief= GROOVE, 
                    bd = 3
                )
algo_label.place(x = 1, y = 1)

select_algo = ttk.Combobox(
                            root, 
                            width = 15, 
                            font = ("new roman", 14, "italic"), 
                            textvariable = selected_algo, 
                            values = algo_list
                        )
select_algo.place(x = 160, y = 1)
select_algo.current(0)

gen_bars = Button(
                    root, 
                    text = "Generate", 
                    bg = "#D31E15", 
                    font = ("new roman", 12, "bold"), 
                    relief= GROOVE, 
                    activebackground = "#37C11E", 
                    bd = 3, 
                    width = 7, 
                    command = generate
                )
gen_bars.place(x = 755, y = 1)

size_label = Label(
                    root, 
                    text = "Size: ", 
                    font = ("new roman", 12, "bold"), 
                    bg="#909296", 
                    width = 5, 
                    fg = "#E0EEDD", 
                    relief= GROOVE, 
                    bd = 3
                )
size_label.place(x = 1, y = 55)

size_val = Scale(
                    root, 
                    from_ = 0, 
                    to = 20, 
                    resolution = 1, 
                    orient = HORIZONTAL, 
                    font = ("new roman", 12, "bold"), 
                    relief = GROOVE, 
                    width = 15
                )
size_val.place(x = 65, y = 55)

min_label = Label(
                    root, 
                    text = "Minimum Value: ", 
                    font = ("new roman", 12, "bold"), 
                    bg="#909296", 
                    width = 13, 
                    fg = "#E0EEDD", 
                    relief= GROOVE, 
                    bd = 3
                )
min_label.place(x = 180, y = 55)

min_val = Scale(
                    root, 
                    from_ = 0, 
                    to = 10, 
                    resolution = 1, 
                    orient = HORIZONTAL, 
                    font = ("new roman", 12, "bold"), 
                    relief = GROOVE, 
                    width = 15
                )
min_val.place(x = 325, y = 55)

max_label = Label(
                    root, 
                    text = "Maximum Value: ", 
                    font = ("new roman", 12, "bold"), 
                    bg="#909296", 
                    width = 14, 
                    fg = "#E0EEDD", 
                    relief= GROOVE, 
                    bd = 3
                )
max_label.place(x = 440, y = 55)

max_val = Scale(
                    root, 
                    from_ = 0, 
                    to = 100, 
                    resolution = 1, 
                    orient = HORIZONTAL, 
                    font = ("new roman", 12, "bold"), 
                    relief = GROOVE, 
                    width = 15
                )
max_val.place(x = 600, y = 55)

speed_label = Label(
                    root, 
                    text = "Speed: ", 
                    font = ("new roman", 12, "bold"), 
                    bg="#909296", 
                    width = 10, 
                    fg = "#E0EEDD", 
                    relief= GROOVE, 
                    bd = 3
                )
speed_label.place(x = 360, y = 1)

speed_val = Scale(
                    root, 
                    from_ = 0.1, 
                    to = 2, 
                    resolution = 0.1, 
                    orient = HORIZONTAL, 
                    font = ("new roman", 12, "bold"), 
                    relief = GROOVE,
                    width = 15,
                )
speed_val.place(x = 475, y = 1)

start_algo = Button(
                    root, 
                    text = "Start", 
                    bg = "#D31E15", 
                    font = ("new roman", 12, "bold"), 
                    relief= GROOVE, 
                    activebackground = "#37C11E", 
                    bd = 3, 
                    width = 5,
                    command = start_algo 
                )
start_algo.place(x = 755, y = 55)

canvas = Canvas(
                root,
                width = 870,
                height = 450,
                bg = "#0B0F4B"
            )
canvas.place(x = 10, y = 130)

root.mainloop()