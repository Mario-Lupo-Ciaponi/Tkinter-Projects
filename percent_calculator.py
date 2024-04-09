from tkinter import *
from tkinter import messagebox


class Percent_Calculatror:
    def __init__(self, master):
        self.master = master
        self.master.title("Percent Calculator")
        self.master.geometry("365x120")
        self.master.configure(bg="#8d99ae")

        # First part
        self.percent_entry = Entry(master, width=5)
        self.percent_entry.grid(row=0, column=0, pady=2)

        self.percent_label = Label(master, text="% of", bg="#8d99ae")  # the text label "[percent] % of [amount] = [result]"
        self.percent_label.grid(row=0, column=1, padx=1.5, pady=2)

        self.amount_entry = Entry(master, width=5)  # The amount you want to take the percentage of.
        self.amount_entry.grid(row=0, column=2, pady=2)

        self.first_equal_label = Label(master, text="=", bg="#8d99ae")  # "=" sign.
        self.first_equal_label.grid(row=0, column=3, padx=1.5, pady=2)

        self.first_result_entry = Entry(master, width=5)  # When clicked "calculate" it will give the result in this entry.
        self.first_result_entry.grid(row=0, column=4, pady=2)

        self.first_calculate_button = Button(master, text="Calculate", padx=7, pady=3, command=self.calculate_amount)
        self.first_calculate_button.grid(row=0, column=5, padx=20, pady=2)

        # second part

        self.amount_to_take = Entry(master, width=5)  # The amount to take from the total amount.
        self.amount_to_take.grid(row=1, column=0, pady=2)

        self.second_percent_label = Label(master, text="of", bg="#8d99ae")  # The word "of".
        self.second_percent_label.grid(row=1, column=1, padx=1.5, pady=2)

        self.total_amount = Entry(master, width=5) # The total amount that will be needed to calculate the percentage.
        self.total_amount.grid(row=1, column=2, pady=2)

        self.second_equal_label = Label(master, text="=", bg="#8d99ae")  # The "=" sign.
        self.second_equal_label.grid(row=1, column=3, padx=1.5, pady=2)

        self.second_result_entry = Entry(master, width=5)  # When clicked "calculate" it will give the result in this entry.
        self.second_result_entry.grid(row=1, column=4, pady=2)

        self.second_calculate_button = Button(master, text="Calculate", padx=7, pady=3, command=self.calculate_percentage)
        self.second_calculate_button.grid(row=1, column=5, padx=20, pady=2)

        self.clear_button = Button(master, text="Clear", width=3, pady=3, command=self.clear_all)
        self.clear_button.grid(row=2, column=0, pady=2)

    def calculate_amount(self):
        if self.percent_entry.get() == "" or self.amount_entry.get() == "":
            messagebox.showerror("Error", "Please fill in all the fields!")
        else:
            percent = float(self.percent_entry.get())
            amount = float(self.amount_entry.get())

            result = amount * (percent / 100)

            self.first_result_entry.insert(0, f"{result:.2f}")

    def calculate_percentage(self):
        if self.amount_to_take.get() == "" or self.total_amount.get() == "":
            messagebox.showerror("Error", "Please fill in all the fields!")
        else:
            amount_to_take = float(self.amount_to_take.get())
            total_amount = float(self.total_amount.get())

            result = amount_to_take / total_amount * 100

            self.second_result_entry.insert(0, f"{result:.2f}%")

    def clear_all(self):
        if self.first_result_entry.get() == "":
            messagebox.showerror("Error", "There is nothing to remove.")
        else:
            self.first_result_entry.delete(0, END)
            self.second_result_entry.delete(0, END)


def main():
    root = Tk()
    percent_calculator = Percent_Calculatror(root)
    root.mainloop()


if __name__ == "__main__":
    main()
