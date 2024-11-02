from random import choice
from tkinter import *
from PIL import ImageTk, Image


def up(event):
    C = []
    for i in range(4):
        B = []
        for j in range(4):
            if matrix[j][i] > 0:
                B.append(matrix[j][i])
        j = 0
        while len(B) > j + 1:
            if B[j] == B[j + 1]:
                B[j] *= 2
                del B[j + 1]
            j += 1
        if len(B) < 4:
            for j in range(4):
                if j >= len(B):
                    matrix[j][i] = 0
                    C.append(4 * j + i)
                else:
                    matrix[j][i] = B[j]
    if len(C) > 0:
        chc = choice(C)
        matrix[chc // 4][chc % 4] = choice(random_list)
    else:
        game_over()
    update_matrix_labels()


def down(event):
    C = []
    for i in range(4):
        B = []
        for j in range(3, -1, -1):
            if matrix[j][i] > 0:
                B.append(matrix[j][i])
        j = 0
        while len(B) > j + 1:
            if B[j] == B[j + 1]:
                B[j] *= 2
                del B[j + 1]
            j += 1
        if len(B) < 4:
            for j in range(3, -1, -1):
                if abs(j - 3) >= len(B):
                    matrix[j][i] = 0
                    C.append(4 * j + i)
                else:
                    matrix[j][i] = B[abs(j - 3)]
    if len(C) > 0:
        chc = choice(C)
        matrix[chc // 4][chc % 4] = choice(random_list)
    else:
        game_over()
    update_matrix_labels()


def left(event):
    C = []
    for i in range(4):
        B = []
        for j in range(4):
            if matrix[i][j] > 0:
                B.append(matrix[i][j])
        j = 0
        while len(B) > j + 1:
            if B[j] == B[j + 1]:
                B[j] *= 2
                del B[j + 1]
            j += 1
        if len(B) < 4:
            for j in range(4):
                if j >= len(B):
                    matrix[i][j] = 0
                    C.append(4 * i + j)
                else:
                    matrix[i][j] = B[j]
    if len(C) > 0:
        chc = choice(C)
        matrix[chc // 4][chc % 4] = choice(random_list)
    else:
        game_over()
    update_matrix_labels()


def right(event):
    C = []
    for i in range(4):
        B = []
        for j in range(3, -1, -1):
            if matrix[i][j] > 0:
                B.append(matrix[i][j])
        j = 0
        while len(B) > j + 1:
            if B[j] == B[j + 1]:
                B[j] *= 2
                del B[j + 1]
            j += 1
        if len(B) < 4:
            for j in range(3, -1, -1):
                if abs(j - 3) >= len(B):
                    matrix[i][j] = 0
                    C.append(4 * i + j)
                else:
                    matrix[i][j] = B[abs(j - 3)]
    if len(C) > 0:
        chc = choice(C)
        matrix[chc // 4][chc % 4] = choice(random_list)
    else:
        game_over()
    update_matrix_labels()


def game_over():
    lbl_result.configure(text='Вы проиграли!', bg='red')


def update_matrix():
    for i in range(4):
        for j in range(4):
            matrix[i][j] = 0
    A = [i for i in range(16)]
    for i in range(2):
        chc = choice(A)
        A.remove(chc)
        matrix[chc // 4][chc % 4] = choice(random_list)
    return matrix


def update_matrix_labels():
    for i in range(4):
        for j in range(4):
            matrix_labels[i][j].configure(image=Images[matrix[i][j]])
            if matrix[i][j] == 2048:
                lbl_result.configure(text='Вы выиграли!', bg='green')


def new_game():
    lbl_result.configure(text='', bg='#FFFFFF')
    update_matrix()
    update_matrix_labels()


root = Tk()
img_bg = ImageTk.PhotoImage(Image.open('images_2048/background.png'))
img_2 = ImageTk.PhotoImage(Image.open('images_2048/2.png'))
img_4 = ImageTk.PhotoImage(Image.open('images_2048/4.png'))
img_8 = ImageTk.PhotoImage(Image.open('images_2048/8.png'))
img_16 = ImageTk.PhotoImage(Image.open('images_2048/16.png'))
img_32 = ImageTk.PhotoImage(Image.open('images_2048/32.png'))
img_64 = ImageTk.PhotoImage(Image.open('images_2048/64.png'))
img_128 = ImageTk.PhotoImage(Image.open('images_2048/128.png'))
img_256 = ImageTk.PhotoImage(Image.open('images_2048/256.png'))
img_512 = ImageTk.PhotoImage(Image.open('images_2048/512.png'))
img_1024 = ImageTk.PhotoImage(Image.open('images_2048/1024.png'))
img_2048 = ImageTk.PhotoImage(Image.open('images_2048/2048.png'))
img_4096 = ImageTk.PhotoImage(Image.open('images_2048/4096.png'))
Images = {0: img_bg, 2: img_2, 4: img_4, 8: img_8, 16: img_16, 32: img_32, 64: img_64, 128: img_128, 256: img_256,
          512: img_512, 1024: img_1024, 2048: img_2048, 4096: img_4096}

frm_1 = Frame(master=root)
frm_1.pack()
Button(master=frm_1, text='Новая игра?', font=20, command=new_game).grid(row=0, column=0, pady=10)
lbl_result = Label(master=frm_1, font=20, bg='#FFFFFF')
lbl_result.grid(row=0, column=1, pady=10)
frm_2 = Frame(master=root)
frm_2.pack()

matrix = [[0 for _ in range(4)] for __ in range(4)]
A_ = [i_ for i_ in range(16)]
random_list = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
for i_ in range(2):
    chc_ = choice(A_)
    A_.remove(chc_)
    matrix[chc_ // 4][chc_ % 4] = choice(random_list)
matrix_labels = [[] for _ in range(4)]

for i_ in range(4):
    for j_ in range(4):
        matrix_labels[i_].append(Label(master=frm_2, image=Images[matrix[i_][j_]]))
        matrix_labels[i_][j_].grid(row=i_, column=j_)

root.bind('<Up>', up)
root.bind('<Down>', down)
root.bind('<Left>', left)
root.bind('<Right>', right)
root.mainloop()
