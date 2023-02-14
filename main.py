from tkinter import *
screen = Tk()
screen.title("miles to km converter")
screen.config(padx = 50, pady =50)

def miles_to_kilometer():
    miles = float(miles_input.get())
    km_value = miles*1.609
    output_kilometers.config(text=f"{km_value}")


miles_input = Entry(width=50)
miles_input.grid(column =1,row =0)

miles_label = Label(text="Miles")
miles_label.grid(column =2,row =0)

is_equal = Label(text="is equal")
is_equal.grid(column =0,row =1)

output_kilometers = Label(text="0")
output_kilometers.grid(column =1,row =1)

km = Label(text="Km")
km.grid(column =2,row =1)

button = Button(text="Calculate", command= miles_to_kilometer)
button.grid(column =1,row =2)
screen.mainloop()