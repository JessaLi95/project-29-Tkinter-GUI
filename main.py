from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Entry
mile = Entry(width=10)
mile.grid(column=2, row=1)
mile.insert(END, string="0")


# Label
label1 = Label(text="is equal to")
label1.grid(column=1, row=2)

def button_clicked():
    mi = float(mile.get())
    km = round(mi / 0.62137)
    label2.config(text=km)

label2 = Label(text=0)
label2.grid(column=2, row=2)

label3 = Label(text="Miles")
label3.grid(column=3, row=1)

label4 = Label(text="Km")
label4.grid(column=3, row=2)


# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)


window.mainloop()