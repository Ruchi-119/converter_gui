import tkinter

window = tkinter.Tk()
window.title("Converter(Miles to KM)")
window.minsize(width=500, height=300)
window.config(padx=100, pady=50)

label1 = tkinter.Label(text="Miles")
label1.grid(column=2, row=0)



label3 = tkinter.Label(text="Km")
label3.grid(column=2, row=1)

label4 = tkinter.Label(text=0)
label4.grid(column=1, row=1)


def calc():
    miles = int(entry.get())
    km = round(miles * 1.609)
    label4.config(text=f"{km}")


button = tkinter.Button(text="Calculate", command=calc)
button.grid(column=1, row=2)


entry = tkinter.Entry()
entry.grid(column=1, row=0)


window.mainloop()
