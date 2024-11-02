from tkinter import *
from PIL import Image, ImageTk
from random import choice as chc


def distribution_bombs(j_open, i_open):
    size_x = xyb[0]
    size_y = xyb[1]
    number_bombs = xyb[2]
    matrix_ = [['_' for _ in range(size_x)] for _ in range(size_y)]
    matrix_[i_open][j_open] = 0
    if i_open == 0:
        if j_open == 0:
            shifts = [[0, 1], [1, 1], [1, 0]]
        elif j_open == len(matrix_[i_open]) - 1:
            shifts = [[0, -1], [1, 0], [1, -1]]
        else:
            shifts = [[0, -1], [0, 1], [1, 1], [1, 0], [1, -1]]
    elif i_open == len(matrix_) - 1:
        if j_open == 0:
            shifts = [[-1, 0], [-1, 1], [0, 1]]
        elif j_open == len(matrix_[i_open]) - 1:
            shifts = [[0, -1], [-1, -1], [-1, 0]]
        else:
            shifts = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]
    elif j_open == 0 and 0 < i_open < len(matrix_) - 1:
        shifts = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0]]
    elif j_open == len(matrix_[i_open]) - 1 and 0 < i_open < len(matrix_) - 1:
        shifts = [[0, -1], [-1, -1], [-1, 0], [1, 0], [1, -1]]
    else:
        shifts = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
    for k in shifts:
        matrix_[i_open + k[0]][j_open + k[1]] = ' '
    cells = []
    for i in range(size_y):
        for j in range(size_x):
            if matrix_[i][j] == '_':
                cells.append([i, j])
    for i in range(number_bombs):
        bomb_cell = chc(cells)
        matrix_[bomb_cell[0]][bomb_cell[1]] = 'B'
        cells.remove(bomb_cell)
    return matrix_


def distribution_hints(matrix_):
    for i in range(len(matrix_)):
        for j in range(len(matrix_[i])):
            if matrix_[i][j] != 'B':
                bomb_count = 0
                if i == 0:
                    if j == 0:
                        shifts = [[0, 1], [1, 1], [1, 0]]
                    elif j == len(matrix_[i]) - 1:
                        shifts = [[0, -1], [1, 0], [1, -1]]
                    else:
                        shifts = [[0, -1], [0, 1], [1, 1], [1, 0], [1, -1]]
                elif i == len(matrix_) - 1:
                    if j == 0:
                        shifts = [[-1, 0], [-1, 1], [0, 1]]
                    elif j == len(matrix_[i]) - 1:
                        shifts = [[0, -1], [-1, -1], [-1, 0]]
                    else:
                        shifts = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]
                elif j == 0 and 0 < i < len(matrix_) - 1:
                    shifts = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0]]
                elif j == len(matrix_[i]) - 1 and 0 < i < len(matrix_) - 1:
                    shifts = [[0, -1], [-1, -1], [-1, 0], [1, 0], [1, -1]]
                else:
                    shifts = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
                for k in shifts:
                    if matrix_[i + k[0]][j + k[1]] == 'B':
                        bomb_count += 1
                matrix_[i][j] = bomb_count
    x = xyb[0]
    y = xyb[1]
    len_y = len(matrix)
    len_x = len(matrix[0])
    if x > len_x:
        for i in range(len_y):
            for _ in range(x - len_x):
                matrix[i].append(0)
    elif x < len_x:
        for i in range(len_y):
            del matrix[i][:len_x - x]
    if y > len_y:
        for _ in range(y - len_y):
            matrix.append([0 for _ in range(x)])
    elif y < len_y:
        del matrix[:len_y - y]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix_[i][j]


def left_click(event):
    j = (root.winfo_pointerx() - root.winfo_rootx())
    i = (root.winfo_pointery() - root.winfo_rooty())
    if xyb[0] < 10:
        j -= 25 * (10 - xyb[0])
    i -= 80
    j //= 50
    i //= 50
    if 0 <= j < xyb[0] and 0 <= i < xyb[1]:
        sum_matrix = 0
        for list_ in matrix_opened_cells:
            sum_matrix += sum(list_)
        if sum_matrix == 0:
            distribution_hints(distribution_bombs(j, i))
        lbl = Label(master=frm_2, image=Images[matrix[i][j]])
        lbl.place(x=j * 50, y=i * 50, width=50, height=50)
        matrix_opened_cells[i][j] = 1
        matrix_flags[i][j] = 0
        if matrix[i][j] == 'B':
            lbl_result.configure(text='Вы проиграли!', bg='red')
            for i_ in range(len(matrix)):
                for j_ in range(len(matrix[i_])):
                    if matrix[i_][j_] == 'B' and matrix_flags[i_][j_] == 0:
                        lbl = Label(master=frm_2, image=Images['B'])
                        lbl.place(x=j_ * 50, y=i_ * 50, width=50, height=50)
            return
        ij_list = [[i, j]]
        if matrix[i][j] == 0:
            ij = 0
            while ij < len(ij_list):
                i = ij_list[ij][0]
                j = ij_list[ij][1]
                if i == 0:
                    if j == 0:
                        shifts = [[0, 1], [1, 1], [1, 0]]
                    elif j == len(matrix[i]) - 1:
                        shifts = [[0, -1], [1, 0], [1, -1]]
                    else:
                        shifts = [[0, -1], [0, 1], [1, 1], [1, 0], [1, -1]]
                elif i == len(matrix) - 1:
                    if j == 0:
                        shifts = [[-1, 0], [-1, 1], [0, 1]]
                    elif j == len(matrix[i]) - 1:
                        shifts = [[0, -1], [-1, -1], [-1, 0]]
                    else:
                        shifts = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]
                elif j == 0 and 0 < i < len(matrix) - 1:
                    shifts = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0]]
                elif j == len(matrix[i]) - 1 and 0 < i < len(matrix) - 1:
                    shifts = [[0, -1], [-1, -1], [-1, 0], [1, 0], [1, -1]]
                else:
                    shifts = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
                for k in shifts:
                    if matrix_opened_cells[i + k[0]][j + k[1]] == 0:
                        lbl = Label(master=frm_2, image=Images[matrix[i + k[0]][j + k[1]]])
                        lbl.place(x=(j + k[1]) * 50, y=(i + k[0]) * 50, width=50, height=50)
                        matrix_opened_cells[i + k[0]][j + k[1]] = 1
                        matrix_flags[i + k[0]][j + k[1]] = 0
                        if matrix[i + k[0]][j + k[1]] == 0:
                            ij_list.append([i + k[0], j + k[1]])
                ij += 1
        sum_matrix = 0
        for list_ in matrix_opened_cells:
            sum_matrix += sum(list_)
        if xyb[0] * xyb[1] - sum_matrix == xyb[2]:
            lbl_result.configure(text='Вы выиграли!', bg='green')
        sum_matrix_flags = 0
        for list_ in matrix_flags:
            sum_matrix_flags += sum(list_)
        lbl_b.configure(text=f'Осталось бомб: {xyb[2] - sum_matrix_flags}')


def right_click(event):
    j = (root.winfo_pointerx() - root.winfo_rootx())
    i = (root.winfo_pointery() - root.winfo_rooty())
    if xyb[0] < 10:
        j -= 25 * (10 - xyb[0])
    i -= 80
    j //= 50
    i //= 50
    if 0 <= j < xyb[0] and 0 <= i < xyb[1]:
        if matrix_buttons[i][j]['image'] == 'pyimage11':
            matrix_buttons[i][j]['image'] = Images['F']
            matrix_flags[i][j] = 1
        else:
            matrix_buttons[i][j]['image'] = Images['G']
            matrix_flags[i][j] = 0
        sum_matrix_flags = 0
        for list_ in matrix_flags:
            sum_matrix_flags += sum(list_)
        lbl_b.configure(text=f'Осталось бомб: {xyb[2] - sum_matrix_flags}')


def get_xyb():
    try:
        x = int(spn_x.get())
    except ValueError:
        x = 4
        spn_x.delete(0, END)
        spn_x.insert(0, x)
    if x < 4:
        x = 4
        spn_x.delete(0, END)
        spn_x.insert(0, x)
    elif x > 30:
        x = 30
        spn_x.delete(0, END)
        spn_x.insert(0, x)
    xyb[0] = x
    try:
        y = int(spn_y.get())
    except ValueError:
        y = 4
        spn_y.delete(0, END)
        spn_y.insert(0, y)
    if y < 4:
        y = 4
        spn_y.delete(0, END)
        spn_y.insert(0, y)
    elif y > 14:
        y = 14
        spn_y.delete(0, END)
        spn_y.insert(0, y)
    xyb[1] = y
    try:
        b = int(spn_b.get())
    except ValueError:
        b = 1
        spn_b.delete(0, END)
        spn_b.insert(0, b)
    if b > x * y - 9:
        b = x * y - 9
        spn_b.delete(0, END)
        spn_b.insert(0, b)
    elif b < 1:
        b = 1
        spn_b.delete(0, END)
        spn_b.insert(0, b)
    xyb[2] = b


def new_game():
    get_xyb()
    x = xyb[0]
    y = xyb[1]
    lbl_result.configure(text='', bg='#FFFFFF')
    frm_2.configure(width=50 * x, height=50 * y)
    len_y = len(matrix_buttons)
    len_x = len(matrix_buttons[0])
    if x > len_x:
        for i in range(len_y):
            for _ in range(x - len_x):
                matrix_buttons[i].append(Button())
                matrix_opened_cells[i].append(0)
                matrix_flags[i].append(0)
    elif x < len_x:
        for i in range(len_y):
            del matrix_buttons[i][:len_x - x]
            del matrix_opened_cells[i][:len_x - x]
            del matrix_flags[i][:len_x - x]
    if y > len_y:
        for _ in range(y - len_y):
            matrix_buttons.append([Button() for _ in range(x)])
            matrix_opened_cells.append([0 for _ in range(x)])
            matrix_flags.append([0 for _ in range(x)])
    elif y < len_y:
        del matrix_buttons[:len_y - y]
        del matrix_opened_cells[:len_y - y]
        del matrix_flags[:len_y - y]
    for i in range(y):
        for j in range(x):
            matrix_buttons[i][j] = Button(master=frm_2, image=Images['G'], borderwidth=5, relief=RIDGE)
            matrix_buttons[i][j].place(x=50 * j, y=50 * i, width=50, height=50)
            matrix_opened_cells[i][j] = 0
            matrix_flags[i][j] = 0


root = Tk()
root.title('Игра Сапёр')
img_1 = ImageTk.PhotoImage(Image.open('images_minesweeper/1.png'))
img_2 = ImageTk.PhotoImage(Image.open('images_minesweeper/2.png'))
img_3 = ImageTk.PhotoImage(Image.open('images_minesweeper/3.png'))
img_4 = ImageTk.PhotoImage(Image.open('images_minesweeper/4.png'))
img_5 = ImageTk.PhotoImage(Image.open('images_minesweeper/5.png'))
img_6 = ImageTk.PhotoImage(Image.open('images_minesweeper/6.png'))
img_7 = ImageTk.PhotoImage(Image.open('images_minesweeper/7.png'))
img_8 = ImageTk.PhotoImage(Image.open('images_minesweeper/8.png'))
img_bomb = ImageTk.PhotoImage(Image.open('images_minesweeper/bomb.png'))
img_flag = ImageTk.PhotoImage(Image.open('images_minesweeper/flag.png'))
img_grey = ImageTk.PhotoImage(Image.open('images_minesweeper/grey.png'))
img_white = ImageTk.PhotoImage(Image.open('images_minesweeper/white.png'))
Images = {0: img_white, 1: img_1, 2: img_2, 3: img_3, 4: img_4, 5: img_5, 6: img_6, 7: img_7, 8: img_8, 'B': img_bomb,
          'F': img_flag, 'G': img_grey, 'W': img_white}
xyb = [4, 4, 1]
matrix_buttons = [[Button() for _ in range(4)] for _ in range(4)]
matrix_opened_cells = [[0 for _ in range(4)] for _ in range(4)]
matrix = [[0 for _ in range(4)] for _ in range(4)]
matrix_flags = [[0 for _ in range(4)] for _ in range(4)]

frm_1 = Frame(master=root, width=500, height=80, bg='#FFFFFF')
frm_1.pack()
frm_1.grid_propagate(0)

Label(master=frm_1, text='x = ', font=20).grid(row=0, column=0, sticky=E)
spn_x = Spinbox(master=frm_1, width=2, from_=4, to=30, font=20)
spn_x.grid(row=0, column=1, sticky=W)

Label(master=frm_1, text='y = ', font=20).grid(row=0, column=2, sticky=E)
spn_y = Spinbox(master=frm_1, width=2, from_=4, to=14, font=20)
spn_y.grid(row=0, column=3, sticky=W)

Label(master=frm_1, text='бомб = ', font=20).grid(row=0, column=4, sticky=E)
spn_b = Spinbox(master=frm_1, width=3, from_=1, to=999, font=20)
spn_b.grid(row=0, column=5, sticky=W)

lbl_b = Label(master=frm_1, text='Осталось бомб: 1', font=20)
lbl_b.grid(row=0, column=6)

frm_2 = Frame(master=root, width=50 * 4, height=50 * 4)
frm_2.pack()

Button(master=frm_1, text='Новая игра?', font=20, command=new_game).grid(row=1, column=0, sticky=W, columnspan=4,
                                                                         padx=5, pady=5)
lbl_result = Label(master=frm_1, font=20, bg='#FFFFFF')
lbl_result.grid(row=1, column=4, columnspan=2)

root.bind('<Button-1>', left_click)
root.bind('<Button-3>', right_click)

root.mainloop()
