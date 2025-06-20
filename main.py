from tkinter import *
from tkinter import ttk
root = Tk()
root.title("NISSAN Calculator")
root.geometry("450x370")

label = Label(text="Калькулятор для Автомобиля Nissan Almera g15 (2015)") # создаем текстовую метку
label.pack()    # размещаем метку в окне
root.resizable(False, False)
root.iconbitmap(default="favicon.ico")

GRM_data = 0
motor_oil_data = 0
oil_seal_data = 0
brake_pads_back_data = 0
pump_data = 0

#Чтение всех текстовых файлов со значениями их установки
def reader():
    with open("GRM.txt", "r") as file:
        global GRM_data
        GRM_data = int(file.read())
    with open("motor_oil.txt", "r") as file:
        global motor_oil_data
        motor_oil_data = int(file.read())
    with open("oil_seal.txt", "r") as file:
        global oil_seal_data
        oil_seal_data = int(file.read())
    with open("brake_pads_back.txt", "r") as file:
        global brake_pads_back_data
        brake_pads_back_data = int(file.read())
    with open("pump.txt", "r") as file:
        global pump_data
        pump_data = int(file.read())
reader()

def count():
    with open("probeg.txt", "w") as file:
        file.write(entry.get()) #Сохраняет значение из Entry в txt. файл
        #Расчеты
        motor_oil = motor_oil_data + 7000 # Моторное масло и маслянный фильтр
        GRM = GRM_data + 50000 # Ремень ГРМ
        oil_seal = oil_seal_data + 50000 # Сальник
        pump = pump_data + 90000 # Водяной насос
        brake_pads_back = brake_pads_back_data + 50000 # Задние тормозные колодки
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



label_correct = ttk.Label(text="Замена произведена на следующем пробеге: ")
label_correct.place(x=100, y=190)

label_motor_oil = ttk.Label(text="Масло и маслянный насос: ")
label_motor_oil.place(x=10, y=220)

entry_motor_oil = ttk.Entry(root, justify="center") #justify центрует вводимый текст
entry_motor_oil.place(x=170,y=220)

label_GRM = ttk.Label(text="Приводной и ГРМ ремни: ")
label_GRM.place(x=10, y=250)

entry_GRM = ttk.Entry(root, justify="center") #justify центрует вводимый текст
entry_GRM.place(x=170,y=250)

label_oil_seal = ttk.Label(text="Маслянные сальники: ")
label_oil_seal.place(x=10, y=280)

entry_oil_seal = ttk.Entry(root, justify="center") #justify центрует вводимый текст
entry_oil_seal.place(x=170,y=280)

label_pump = ttk.Label(text="Водяной насос: ")
label_pump.place(x=10, y=310)

entry_pump = ttk.Entry(root, justify="center") #justify центрует вводимый текст
entry_pump.place(x=170,y=310)

label_brake_pads_back = ttk.Label(text="Задние тормоза: ")
label_brake_pads_back.place(x=10, y=340)

entry_brake_pads_back = ttk.Entry(root, justify="center") #justify центрует вводимый текст
entry_brake_pads_back.place(x=170,y=340)


root.mainloop()