from tkinter import *
from tkinter import ttk
root = Tk()
root.title("NISSAN Calculator")
root.geometry("450x400")

label = Label(text="Калькулятор для Автомобиля Nissan Almera g15 (2015)") # создаем текстовую метку
label.pack()    # размещаем метку в окне
root.resizable(False, False)
root.iconbitmap(default="favicon.ico")

#Для начала нужно сделать чтение всех текстовых файлов со значениями их установки


'''Сохраняет значение из Entry в txt. файл'''
def count():
    with open("probeg.txt", "w") as file:
        file.write(entry.get())
        #Тут должны быть расчеты
        # Моторное масло и маслянный фильтр
        with open("motor_oil.txt", "r") as file:
            motor_oil = int(file.read()) + 7000
        # Ремень ГРМ
        GRM = 156000 + 50000
        # Сальник
        oil_seal = 156000 + 50000
        # Водяной насос
        pump = 156000 + 90000
        # Задние тормозные колодки
        brake_pads_back = 156700 + 50000
        label["text"] = (f"Замена моторного масла и маслянного фильтра через: {motor_oil - int(entry.get())} км\n"
                          f"Замена задних колодок через: {brake_pads_back - int(entry.get())} км\n"
                         f"Замена приводного и ГРМ ремней через: {GRM - int(entry.get())} км\n"
                         f"Замена сальников через:{oil_seal - int(entry.get())} км\n"
                         f"Замена водяного насоса через:{pump - int(entry.get())} км\n")

entry = ttk.Entry(root, justify="center") #justify центрует вводимый текст
entry.pack(anchor=N, padx=6, pady=6)
btn = ttk.Button(text="Рассчитать", command=count)
btn.pack(anchor=N, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=N, padx=6, pady=6)

root.mainloop()