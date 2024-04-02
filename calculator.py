from tkinter import *
from math import *


class Calculator:
    f_number = 0
    sign = ""

    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Creating widgets
        self.entry = Entry(master, width=32, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.button_1 = Button(master, text="1", padx=30, pady=10, command=lambda: self.click_button(1))
        self.button_2 = Button(master, text="2", padx=30, pady=10, command=lambda: self.click_button(2))
        self.button_3 = Button(master, text="3", padx=30, pady=10, command=lambda: self.click_button(3))
        self.button_4 = Button(master, text="4", padx=29, pady=10, command=lambda: self.click_button(4))
        self.button_5 = Button(master, text="5", padx=30, pady=10, command=lambda: self.click_button(5))
        self.button_6 = Button(master, text="6", padx=30, pady=10, command=lambda: self.click_button(6))
        self.button_7 = Button(master, text="7", padx=30, pady=10, command=lambda: self.click_button(7))
        self.button_8 = Button(master, text="8", padx=30, pady=10, command=lambda: self.click_button(8))
        self.button_9 = Button(master, text="9", padx=30, pady=10, command=lambda: self.click_button(9))
        self.button_0 = Button(master, text="0", padx=30, pady=10, command=lambda: self.click_button(0))

        self.clear_button = Button(master, text="Clear", padx=73, pady=10, command=self.clear_numbers)
        self.equal_button = Button(master, text="=", padx=84, pady=10,
                                   command=lambda: self.equal_command(self.entry.get()))

        # signs
        self.plus_sign = Button(master, text="+", padx=30, pady=10,
                                command=lambda: self.add_number(self.entry.get()))
        self.minus_sign = Button(master, text="-", padx=30, pady=10,
                                 command=lambda: self.subtract_number(self.entry.get()))
        self.multiplication_sign = Button(master, text="X", padx=30, pady=10,
                                          command=lambda: self.multiplication_number(self.entry.get()))
        self.division_sign = Button(master, text="/", padx=32, pady=10,
                                    command=lambda: self.divide_number(self.entry.get()))
        self.square_root_sign = Button(master, text="\u221A", padx=30, pady=10,
                                       command=lambda: self.square_root_number(self.entry.get()))

        # Adding widgets to the root
        self.button_1.grid(row=1, column=0)
        self.button_2.grid(row=1, column=1)
        self.button_3.grid(row=1, column=2)

        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)

        self.button_7.grid(row=3, column=0)
        self.button_8.grid(row=3, column=1)
        self.button_9.grid(row=3, column=2)

        self.button_0.grid(row=4, column=0)
        self.equal_button.grid(row=4, column=1, columnspan=2)

        self.plus_sign.grid(row=5, column=0)
        self.minus_sign.grid(row=5, column=1)
        self.multiplication_sign.grid(row=5, column=2)
        self.division_sign.grid(row=6, column=0)
        self.square_root_sign.grid(row=7, column=0)

        self.clear_button.grid(row=6, column=1, columnspan=2)

    def click_button(self, number):
        current = self.entry.get()

        self.entry.delete(0, END)
        self.entry.insert(0, str(current) + str(number))

    def clear_numbers(self):
        self.entry.delete(0, END)

    def add_number(self, first_number):
        Calculator.f_number = int(first_number)
        Calculator.sign = "+"
        self.entry.delete(0, END)

    def subtract_number(self, first_number):
        Calculator.f_number = int(first_number)
        Calculator.sign = "-"
        self.entry.delete(0, END)

    def multiplication_number(self, first_number):
        Calculator.f_number = int(first_number)
        Calculator.sign = "*"
        self.entry.delete(0, END)

    def divide_number(self, first_number):
        Calculator.f_number = int(first_number)
        Calculator.sign = "/"
        self.entry.delete(0, END)

    def square_root_number(self, first_number):
        Calculator.f_number = int(first_number)
        self.entry.delete(0, END)

        if sqrt(Calculator.f_number).is_integer():
            self.entry.insert(0, int(sqrt(Calculator.f_number)))
        else:
            self.entry.insert(0, sqrt(Calculator.f_number))

    def equal_command(self, second_number):
        self.entry.delete(0, END)
        second_number = int(second_number)

        if Calculator.sign == "+":
            self.entry.insert(0, Calculator.f_number + second_number)
        elif Calculator.sign == "-":
            self.entry.insert(0, Calculator.f_number - second_number)
        elif Calculator.sign == "*":
            self.entry.insert(0, Calculator.f_number * second_number)
        elif Calculator.sign == "/":
            if Calculator.f_number % second_number == 0:
                self.entry.insert(0, Calculator.f_number // second_number)
            else:
                self.entry.insert(0, Calculator.f_number / second_number)



def main():
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
