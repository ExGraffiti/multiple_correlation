import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from PyQt5 import uic
import tkinter as tk
from PyQt5.QtWidgets import QApplication
from tkinter import filedialog

Form, Window = uic.loadUiType("practice.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

path = ''


def open_file():
    try:
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        path = file_path
        file = open(file_path, 'r')
        form.plainTextEdit.clear()
        form.plainTextEdit.insertPlainText(str(file.read()))

        with open(file_path) as f:
            reader = csv.DictReader(f, delimiter=';')
            a = []
            b = []
            for row in reader:
                a.append(float(row['X']))
                b.append(float(row['Y']))

            ts = correlation(np.array(a), np.array(b))
            form.plainTextEdit_2.insertPlainText(str(ts))
            graph(np.array(a), np.array(b))


    except:
        form.plainTextEdit.clear()
        form.plainTextEdit.insertPlainText(str('Извините, данный формат не поддерживается'))




def graph(xs, ys):
    pd.DataFrame(np.array([xs,ys]).T).plot.scatter(0, 1, s=12, grid=True)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def variance(xs):
    x_hat = xs.mean()
    n = len(xs)
    n = n - 1 if n in range(1, 30) else n
    return sum((xs - x_hat) ** 2) / n



def correlation(xs, ys):

    return covariance(xs, ys) / (np.sqrt(variance(xs)) *
                                 np.sqrt(variance(ys)))
def covariance(xs, ys):

    dx = xs - xs.mean()
    dy = ys - ys.mean()
    return (dx * dy).sum() / (len(dx) - 1)





form.pushButton.clicked.connect(open_file)
form.pushButton_2.clicked.connect(exit)
form.pushButton_3.clicked.connect(built_graph)
app.exec_()
