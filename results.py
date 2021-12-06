import tkinter
from functools import partial
from tkinter import font
from tkinter import Label
from tkinter import Button
from tkinter import Tk


import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")

# Output chart on screen
def show_charts(num_chart):
    if num_chart == 1:
        with open('case_1a_result.txt', 'r') as input_file:
            d2_heap_res, d3_heap_res, vertex_count = [], [], []
            for line in input_file:
                d2_heap_res.append(float(line.split()[0]))
                d3_heap_res.append(float(line.split()[1]))
                vertex_count.append(int(line.split()[2]))
        plt.scatter(vertex_count, d2_heap_res, color="b",  label="2-куча")
        plt.scatter(vertex_count, d3_heap_res, c="r", label="3-куча")
        plt.xlabel('Количество вершин')
        plt.ylabel('Время')
        plt.title('Случай 1.а')
        plt.legend()
        plt.show()

    elif num_chart == 2:
        with open('case_1b_result.txt', 'r') as input_file:
            d2_heap_res, d3_heap_res, vertex_count = [], [], []
            for line in input_file:
                d2_heap_res.append(float(line.split()[0]))
                d3_heap_res.append(float(line.split()[1]))
                vertex_count.append(int(line.split()[2]))
        plt.scatter(vertex_count, d2_heap_res, color="b", linestyle="o",  label="2-куча")
        plt.scatter(vertex_count, d3_heap_res, "ro", label="3-куча")
        plt.xlabel('Количество вершин')
        plt.ylabel('Время')
        plt.title('Случай 1.b')
        plt.legend()

    elif num_chart == 3:
        with open('case_2a_result.txt', 'r') as input_file:
            d2_heap_res, d3_heap_res, vertex_count = [], [], []
            for line in input_file:
                d2_heap_res.append(float(line.split()[0]))
                d3_heap_res.append(float(line.split()[1]))
                vertex_count.append(int(line.split()[2]))
        plt.scatter(vertex_count, d2_heap_res, c="b", label="2-куча")
        plt.scatter(vertex_count, d3_heap_res, c="r", label="3-куча")
        plt.xlabel('Количество вершин')
        plt.ylabel('Время')
        plt.title('Случай 2.а')
        plt.legend()

    elif num_chart == 4:
        with open('case_2b_result.txt', 'r') as input_file:
            d2_heap_res, d3_heap_res, vertex_count = [], [], []
            for line in input_file:
                d2_heap_res.append(float(line.split()[0]))
                d3_heap_res.append(float(line.split()[1]))
                vertex_count.append(int(line.split()[2]))
        plt.scatter(vertex_count, d2_heap_res, c="b", label="2-куча")
        plt.scatter(vertex_count, d3_heap_res, c="r", label="3-куча")
        plt.xlabel('Количество вершин')
        plt.ylabel('Время')
        plt.title('Случай 2.b')
        plt.legend()

    elif num_chart == 5:
        with open('case_3_result.txt', 'r') as input_file:
            d2_heap_res, d3_heap_res, edges_count = [], [], []
            for line in input_file:
                d2_heap_res.append(float(line.split()[0]))
                d3_heap_res.append(float(line.split()[1]))
                edges_count.append(int(line.split()[2]))
        plt.scatter(edges_count, d2_heap_res, c="b", label="2-куча")
        plt.scatter(edges_count, d3_heap_res, c="r", label="3-куча")
        plt.xlabel('Количество ребер')
        plt.ylabel('Время')
        plt.title('Случай 3')
        plt.legend()

    elif num_chart == 6:
        with open('case_4a_result.txt', 'r') as input_file:
            d2_heap_res, d3_heap_res, weight = [], [], []
            for line in input_file:
                d2_heap_res.append(float(line.split()[0]))
                d3_heap_res.append(float(line.split()[1]))
                weight.append(int(line.split()[2]))
        plt.scatter(weight, d2_heap_res, c="b", label="2-куча")
        plt.scatter(weight, d3_heap_res, c="r", label="3-куча")
        plt.xlabel('Максимальные вес')
        plt.ylabel('Время')
        plt.title('Случай 4.a')
        plt.legend()

    elif num_chart == 7:
        with open('case_4b_result.txt', 'r') as input_file:
            d2_heap_res, d3_heap_res, weight = [], [], []
            for line in input_file:
                d2_heap_res.append(float(line.split()[0]))
                d3_heap_res.append(float(line.split()[1]))
                weight.append(int(line.split()[2]))
        plt.scatter(weight, d2_heap_res, c="b", label="2-куча")
        plt.scatter(weight, d3_heap_res, c="r", label="3-куча")
        plt.xlabel('Максимальные вес')
        plt.ylabel('Время')
        plt.title('Случай 4.b')
        plt.legend()

def destroy():
    window.destroy()

if __name__ == "__main__":
    global window
    window = Tk()
    window.geometry('1200x650')
    window.title("Результаты работы алгоритма Дейкстры на 2,3-кучах")
    global_background = "MediumAquamarine"
    window.configure(background = global_background)
    fontStyle = font.Font(family="lucida grande bold", size = 18)
    fontStyle_coordinate = font.Font(family = "Arial", size = 12)

    Label_introdution = Label(window, text="Укажите тест, результаты которого необходимо вывести", font = fontStyle)
    Label_introdution.place(x = 10, y = 10)
    Label_introdution.configure(background = global_background)
    Button_exit = Button(window,
                            text = "Завершить",
                            command = destroy,
                            width = 10,
                            height = 2,
                            compound = tkinter.CENTER,
                            font = fontStyle,
                            background = "LimeGreen",
                            highlightbackground = "black",
                            relief = "solid")
    Button_exit.place(x = 100, y = 550)
    Buttons_num_test = []
    for i in range(7):
        Buttons_num_test.append(Button(window, text=str(i+1), command=partial(show_charts, i+1), width=10, height=2,
                                compound=tkinter.CENTER, font = fontStyle, background = "LimeGreen",
                                highlightbackground="black", relief="solid"))
        Buttons_num_test[-1].place(x = 10 + (i % 4) * 150, y = 50 + 80 * (i // 4))
    window.mainloop()
