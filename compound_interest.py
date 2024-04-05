from tkinter import *
from tkinter import messagebox


class Compound_Interest:
    def __init__(self, master):
        self.master = master
        self.master.title("Compound Interest Calculator")
        self.master.geometry("310x250")
        self.master.configure(bg="#E7E3E3")

        self.principal_label = Label(master, text="Principal Amount:", bg="#DBD7D2")
        self.principal_label.grid(row=0, column=0, padx=7, pady=2)

        self.principal_entry = Entry(master, width=15)
        self.principal_entry.grid(row=0, column=1, padx=7, pady=6)

        self.rate_label = Label(master, text="Rate(%):", bg="#DBD7D2")
        self.rate_label.grid(row=1, column=0, padx=7, pady=2)

        self.rate_entry = Entry(master, width=15)
        self.rate_entry.grid(row=1, column=1, padx=7, pady=6)

        self.time_label = Label(master, text="Time(in years):", bg="#DBD7D2")
        self.time_label.grid(row=2, column=0, padx=7, pady=2)

        self.time_entry = Entry(master, width=15)
        self.time_entry.grid(row=2, column=1, padx=7, pady=6)

        self.calculate_button = Button(master, text="Calculate", padx=7, pady=3, command=self.calculate_compound)
        self.calculate_button.grid(row=3, column=1)

        self.compound_interest_label = Label(master, text="Compound Interest:", bg="#DBD7D2")
        self.compound_interest_label.grid(row=4, column=0, padx=7, pady=2)

        self.compound_interest_entry = Entry(master, width=15)
        self.compound_interest_entry.grid(row=4, column=1, padx=7, pady=15)

        self.clear_button = Button(master, text="Clear", width=7, command=self.clear_compound)
        self.clear_button.grid(row=5, column=1)

    def is_it_valid(self):
        if self.principal_entry.get() == "" or self.rate_entry.get() == "" or self.time_entry.get() == "":
            messagebox.showerror("Error", "Please fill all the fields!")
            return False
        else:
            return True

    def calculate_compound(self):
        if self.is_it_valid():
            principal = float(self.principal_entry.get())
            rate = float(self.rate_entry.get())
            time = float(self.time_entry.get())

            compound = principal * (pow((1 + rate / 100), time))

            self.compound_interest_entry.insert(0, f"{compound:.2f}")

    def clear_compound(self):
        self.compound_interest_entry.delete(0, END)


def main():
    root = Tk()
    compound_interest = Compound_Interest(root)
    root.mainloop()


if __name__ == "__main__":
    main()