import requests
import time
import os
def kodstatusa_and_time():
    print("Введите путь до файла")
    print("Для OC Windows диск:\\каталог, для Linux /home/имя учетки/") # Примечание для правильного ввода пути сохранения
    filepath = input("Введите путь сохранения файла:") # Ввод необходимых переменных
    path_url = input("Введите путь сайта:") 
    current_time = time.localtime() 
    current_time = time.strftime("%H:%M:%S", current_time) # Узнаем текущее время
    kodstatusa = requests.get(path_url) # Делаем .get запрос на страницу, для кода статуса
    kod = kodstatusa.text # Записываем в переменную код страницы
    file_path = os.path.join(filepath, "output.txt") # функция для работы с файловой системой, где прописан путь сохранения и название файла
    with open(file_path, 'w', encoding='utf-8') as f: # Записываем в файл переменные выше
        f.write(f'Текущее время:{current_time}\n')
        f.write(f'Код статуса:{kodstatusa}\n')
        f.write(f'Код страницы\n{kod}')
        print("Файл успешно сохранен!")
kat = kodstatusa_and_time()