from tkinter import *
from tkinter import messagebox


class BMI_Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("BMI calculator")
        self.master.geometry("220x100")
        self.master.configure(bg="#E7E3E3")

        self.height_label = Label(master, text="Height:", bg="#E7E3E3")
        self.height_label.grid(row=1, column=0, padx=7, pady=2)

        self.height_entry = Entry(master, width=4)
        self.height_entry.grid(row=1, column=1, padx=7, pady=2)

        self.height_units = Label(master, text="*in meters", bg="#E7E3E3")
        self.height_units.grid(row=1, column=2, padx=1, pady=2)

        self.weight_label = Label(master, text="Weight:", bg="#E7E3E3")
        self.weight_label.grid(row=2, column=0, padx=7, pady=2)

        self.weight_entry = Entry(master, width=4)
        self.weight_entry.grid(row=2, column=1, padx=7, pady=2)

        self.weight_units = Label(master, text="*in kilograms", bg="#E7E3E3")
        self.weight_units.grid(row=2, column=2, padx=1, pady=2)

        self.calculate_button = Button(master, text="Calculate", padx=7, pady=4, command=self.print_bmi)
        self.calculate_button.grid(row=3, column=0, columnspan=2)

    def calculate(self):
        height = float(self.height_entry.get())
        weight = float(self.weight_entry.get())

        bmi = weight / (height ** 2)

        return bmi

    def print_bmi(self):
        bmi = self.calculate()

        status = ""

        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi <= 24.9:
            status = "Normal"
        elif 25 <= bmi <= 29.9:
            status = "Overweight"
        elif 30 <= bmi <= 34.9:
            status = "Obese"
        else:
            status = "Extremely obese"

        messagebox.showinfo("BMI", f"Your BMI is {bmi:.1f}({status})")


def main():
    root = Tk()
    bmi_calculator = BMI_Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()