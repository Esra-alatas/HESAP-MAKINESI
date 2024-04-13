import tkinter as tk   # tkinter aracını import etmek
from tkinter import ttk  # tkinterda combobox kullanmak için ttk'yı import etme
h, w, l, t = 500, 500, 50, 50
calculator = tk.Tk()                 #pencerenin boyutlarını ve ismini belirleyelim
calculator.title("Hesap Makinesi")
calculator.geometry("%sx%s+%s+%s"%(h,w,l,t))

title = tk.Label(text="Hesap Makinesi", font=("Arial", 18))
title.pack(side="top")
lblnumber1 = tk.Label(text="İlk sayıyı giriniz:")
lblnumber1.place(x=25, y=70)

tbNumber1 = tk.Entry()
tbNumber1.place(x=170, y=70)

lblnumber2 = tk.Label(text="İkinci sayıyı giriniz:")
lblnumber2.place(x=25, y=110)

tbNumber2 = tk.Entry()
tbNumber2.place(x=170, y=110)

choice = tk.Label(text="Yapılacak işlemi seçiniz:")
choice.place(x=25,y=145)
choiceMenu = ["Toplama", "Çıkarma", "Çarpma", "Bölme"]
cmbChoice = ttk.Combobox(values=choiceMenu, state="readonly")
cmbChoice.set("--İşlem seçiniz--")
cmbChoice.place(x=170,y=150)
result = tk.Label(text="Sonuç:")
result.place(x=110,y=222)

tbResult = tk.Entry(state="disabled")
tbResult.place(x=170,y=225)
def selectedChoice():
    select = cmbChoice.get()
    number1 = int(tbNumber1.get())
    number2 = int(tbNumber2.get())
    if select == "Toplama":
        toplama = number1 + number2
        tbResult.config(state="normal")
        tbResult.delete(0, tk.END)
        tbResult.insert(0, toplama)
        tbResult.config(state="disabled")
    elif select == "Çıkarma":
        cikarma = number1 - number2
        tbResult.config(state="normal")
        tbResult.delete(0, tk.END)
        tbResult.insert(0, cikarma)
        tbResult.config(state="disabled")

    elif select == "Çarpma":
        carpma = number1 * number2
        tbResult.config(state="normal")
        tbResult.delete(0, tk.END)
        tbResult.insert(0, carpma)
        tbResult.config(state="disabled")

    elif select == "Bölme":
        bolme = float(number1 / number2)
        tbResult.config(state="normal")
        tbResult.delete(0, tk.END)
        tbResult.insert(0, bolme)
        tbResult.config(state="disabled")

btnCalculate = tk.Button(text="Hesapla", command=selectedChoice)
btnCalculate.place(x=170,y=185)








tk.mainloop()








