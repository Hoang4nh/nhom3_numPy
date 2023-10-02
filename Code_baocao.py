import tkinter as tk
from tkinter import END, Scrollbar, Text, messagebox
import matplotlib.pyplot as plt
import pandas as pd
from numpy import array
import numpy as np

df = pd.read_csv('diemPython.csv', index_col=0, header=0)
in_data = array(df.iloc[:, :])
def hienthidanhsach():
    result_text.insert(END, "Danh sách sinh viên:\n")
    result_text.insert(END, str(in_data) + "\n\n")

def tongsinhvien():
    sv = in_data[:, 1]
    tongsv=np.sum(sv)
    result_text.insert(END, "Tổng số sinh viên đi thi:\n")
    result_text.insert(END, str(tongsv) + "\n\n")


def sosinhvientruot():
    svtruot = in_data[:, 10]
    tongsvtruot = np.sum(svtruot)
    result_text.insert(END, "Tổng số sinh viên trượt môn:")
    result_text.insert(END, str(tongsvtruot) + "\n\n")

    categories1 = ['Lớp 1', 'Lớp 2', 'Lớp 3', 'Lớp 4', 'Lớp 5', 'Lớp 6', 'Lớp 7', 'Lớp 8', 'Lớp 9']
    values1 = in_data[:, 10]

    plt.figure(1)
    plt.bar(categories1, values1, color='red', label="Sinh viên trượt")
    plt.title('Biểu đồ số sinh viên trượt của các lớp')
    plt.ylabel('Số sinh viên')
    plt.legend(loc='upper right')
    plt.show()


def sosinhviendat():
    sv = in_data[:, 1]
    tongsv = np.sum(sv)
    svtruot = in_data[:, 10]
    tongsvtruot = np.sum(svtruot)
    tongsvdat = tongsv - tongsvtruot
    result_text.insert(END, "Tổng số sinh viên qua môn:")
    result_text.insert(END, str(tongsvdat) + "\n\n")

    categories2 = ['Lớp 1', 'Lớp 2', 'Lớp 3', 'Lớp 4', 'Lớp 5', 'Lớp 6', 'Lớp 7', 'Lớp 8', 'Lớp 9']
    values2 = np.sum(in_data[0:9, 2:10], axis=1).flatten()

    plt.figure(1)
    plt.bar(categories2, values2, color='green', label="Sinh viên đạt")
    plt.title('Biểu đồ số sinh viên đạt của các lớp')
    plt.ylabel('Số sinh viên')
    plt.legend(loc='upper right')
    plt.show()


def sinhvienA():
    diemA = in_data[:, 3]
    maxa = diemA.max()
    i = np.argmax(diemA)
    result_text.insert(END, 'Lớp có nhiều sinh viên điểm A là {0} có {1} sinh viên đạt điểm A \n'
                       .format(in_data[i, 0], maxa))

    categories1 = ['Lớp 1', 'Lớp 2', 'Lớp 3', 'Lớp 4', 'Lớp 5', 'Lớp 6', 'Lớp 7', 'Lớp 8', 'Lớp 9']
    values1 = in_data[:, 3]

    plt.figure(3)
    plt.bar(categories1, values1, label="Sinh viên đạt điểm A")
    plt.title('Biểu đồ số sinh viên đạt điểm A của các lớp')
    plt.ylabel('Số sinh viên')
    plt.legend(loc='upper right')
    plt.show()
def phodiem():
    diemA = in_data[:, 3]
    diemBc = in_data[:, 4]
    diemB = in_data[:, 5]
    diemCc = in_data[:, 6]
    diemC = in_data[:, 7]
    diemDc = in_data[:, 8]
    diemD = in_data[:, 9]
    diemF = in_data[:, 10]
    plt.figure(2)
    plt.plot(range(len(diemA)), diemA, 'r-', label="Diem A")
    plt.plot(range(len(diemBc)), diemBc, 'g-', label="Diem B +")
    plt.plot(range(len(diemB)), diemB, 'y-', label="Diem B")
    plt.plot(range(len(diemCc)), diemCc, 'b-', label="Diem C +")
    plt.plot(range(len(diemC)), diemC, 'o-', label="Diem C")
    plt.plot(range(len(diemDc)), diemDc, 'k-', label="Diem D +")
    plt.plot(range(len(diemD)), diemD, 'p-', label="Diem D")
    plt.plot(range(len(diemF)), diemF, 'd-', label="Diem F")
    plt.xlabel('Lơp')
    plt.ylabel(' So sv dat diem ')
    plt.legend(loc='upper right')
    plt.show()
def reset_result():
    result_text.delete(1.0, END)

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Ứng dụng báo cáo")

# Tạo các nút chức năng
htdanhsach_button = tk.Button(window, text="Hiển thị danh sách", command=hienthidanhsach)
tongsinhvien_button = tk.Button(window, text="Tổng sinh viên đi thi", command=tongsinhvien)
sinhvientruot_button = tk.Button(window, text="Số sinh viên trượt", command=sosinhvientruot)
sinhviendat_button = tk.Button(window, text="Số sinh viên đạt", command=sosinhviendat)
sinhvienA_button = tk.Button(window, text="Sinh viên đạt điểm A", command=sinhvienA)
phodiem_button = tk.Button(window, text="Phổ điểm", command=phodiem)
reset_button = tk.Button(window, text="Reset", command=reset_result)

# Tạo ô văn bản để hiển thị kết quả
result_text = Text(window, wrap="word", height=15, width=100)
result_text_scrollbar = Scrollbar(window, command=result_text.yview)
result_text.config(yscrollcommand=result_text_scrollbar.set)

# Đặt vị trí các phần tử trên cửa sổ
htdanhsach_button.pack()
tongsinhvien_button.pack()
sinhviendat_button.pack()
sinhvientruot_button.pack()
sinhvienA_button.pack()
phodiem_button.pack()
reset_button.pack()
result_text.pack()
result_text_scrollbar.pack(side="right", fill="y")

# Chạy ứng dụng
window.mainloop()
