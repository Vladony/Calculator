from tkinter import *

root = Tk()
root.title("My Calculator")

display = Entry(root, width=40, borderwidth=5)
display.grid(row=0, column=0, columnspan=5)


def button_clear():
    display.delete(0, END)


def button_plus():
    first_num = display.get()
    global num_1
    global var
    var = "plus"
    num_1 = int(first_num)
    display.delete(0, END)


def button_minus():
    first_num = display.get()
    global num_1
    global var
    var = "minus"
    num_1 = int(first_num)
    display.delete(0, END)


def button_multy():
    first_num = display.get()
    global num_1
    global var
    var = "multy"
    num_1 = int(first_num)
    display.delete(0, END)


def button_divide():
    first_num = display.get()
    global num_1
    global var
    var = "divide"
    num_1 = int(first_num)
    display.delete(0, END)


def button_equal():
    second_num = display.get()
    display.delete(0, END)
    if var == "plus":
        display.insert(0, num_1 + int(second_num))
    elif var == "minus":
        display.insert(0, num_1 - int(second_num))
    if var == "multy":
        display.insert(0, num_1 * int(second_num))
    if var == "divide":
        display.insert(0, num_1 / int(second_num))


def button_click(number):
    current_number = display.get()
    display.delete(0, END)
    display.insert(0, str(current_number)+str(number))


# creating the buttons
button_1 = Button(root, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=10, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=10, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=10, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=75, pady=10, command=lambda: button_click(0))
button_plus = Button(root, text="+", padx=23, pady=10, command=button_plus)
button_minus = Button(root, text="-", padx=19, pady=10, command=button_minus)
button_multiply = Button(root, text="*", padx=25, pady=10, command=button_multy)
button_divide = Button(root, text="/", padx=19, pady=10, command=button_divide)
button_equal = Button(root, text="=", padx=49, pady=10, command=button_equal)
button_clear = Button(root, text="Clear", padx=40, pady=10, command=button_clear)
# visualize the buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0, columnspan=3)
button_plus.grid(row=1, column=3)

button_minus.grid(row=1, column=4)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=2, column=4)
button_equal.grid(row=3, column=3, columnspan=2)
button_clear.grid(row=4, column=3, columnspan=2)

root.mainloop()
