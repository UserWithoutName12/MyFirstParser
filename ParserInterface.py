from fractions import Fraction
from functools import lru_cache
from time import perf_counter
import requests
import time
import os
import tkinter as tk
def kodstatusa_and_time():
    filepath = entry1.get()
    path_url = base_ent.get()
    current_time = time.strftime("%H:%M:%S", time.localtime())
    kodstatusa = requests.get(path_url)
    kod = kodstatusa.text
    file_path = os.path.join(filepath, "output.txt")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f'Текущее время: {current_time}\n')
        f.write(f'Код статуса: {kodstatusa}\n')
        f.write(f'Код страницы\n{kod}')
    print("Файл успешно сохранен!")
    end = perf_counter()
    preobrend = end / 60
    end1 = round(preobrend, 1)
    preobrend1 = Fraction(end1)
    print(f"Время выполнения: {preobrend1} сек")
root = tk.Tk()
root.title("Parser")
root.geometry("500x200")
frame = tk.Frame(root)
frame.pack(expand=True)
method_lbl = tk.Label(frame, text="Вас приветствует программа для парсинга сайтов")
method_lbl.grid(row=1, column=0)
label1 = tk.Label(frame, text="Введите путь до каталога, где нужно сохранить код:")
label1.grid(row=2, column=0)
entry1 = tk.Entry(frame)
entry1.grid(row=3, column=0)
label2 = tk.Label(frame, text="Введите ссылку на сайт:")
label2.grid(row=4, column=0)
base_ent = tk.Entry(frame)
base_ent.grid(row=5, column=0)
base_ent.focus()
button1 = tk.Button(root, text="Начать работу", command=kodstatusa_and_time)
button1.pack()
root.mainloop()