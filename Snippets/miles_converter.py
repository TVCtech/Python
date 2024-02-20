from tkinter import *

def miles_to_km():

    miles = (miles_input.get())
    if miles == '.':
        miles = '0.'
    try:
        _ = float(miles)
    except ValueError:
        entry_var.set('')
        miles_input.config(textvariable=entry_var)
        window.after(1000, miles_to_km)
        return

    km = float(miles) * 1.609
    km_result_label.config(text=f'{km:.3f}')
    window.after(1000, miles_to_km)


window = Tk()
window.title('Miles to Km ')
window.config(padx=20,pady=20)

entry_var = StringVar()
entry_var.set('')




miles_input = Entry(width=5,textvariable='')
miles_input.grid(column=1,row=0)
miles_input.focus()

miles_label = Label(text='Miles')
miles_label.grid(column=2,row=0)

km_result_label = Label(text='-')
km_result_label.grid(column=1,row=1)

is_equal_label = Label(text='=') 
is_equal_label.grid(column=0,row=1)

km_label = Label(text='Km')
km_label.grid(column=2,row=1)

# calculate_button = Button(text='Calculate',command=miles_to_km)
# calculate_button.grid(column=1,row=2)



miles_to_km()
window.mainloop()