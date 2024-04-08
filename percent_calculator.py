from tkinter import *
from tkinter import messagebox


class Percent_Calculatror:
    def __init__(self, master):
        self.master = master
        self.master.title("Percent Calculator")
        self.master.geometry("400x400")
        self.master.configure(bg="#8d99ae")

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

        self.calculate_button = Button(master, text="Calculate", padx=7, pady=3, command=self.calculate_amount)
        self.calculate_button.grid(row=0, column=5, padx=20, pady=2)

        self.clear_button = Button(master, text="Clear", pady=3, command=self.clear_all)
        self.clear_button.grid(row=2, column=0, pady=2)

    def calculate_amount(self):
        if self.percent_entry.get() == "" or self.amount_entry.get() == "":
            messagebox.showerror("Error", "Please fill in all the fields!")
        else:
            percent = float(self.percent_entry.get())
            amount = float(self.amount_entry.get())

            result = amount * (percent / 100)

            self.first_result_entry.insert(0, f"{result:.2f}")


    def clear_all(self):
        if self.first_result_entry.get() == "":
            messagebox.showerror("Error", "There is nothing to remove.")


def main():
    root = Tk()
    percent_calculator = Percent_Calculatror(root)
    root.mainloop()


if __name__ == "__main__":
    main()
