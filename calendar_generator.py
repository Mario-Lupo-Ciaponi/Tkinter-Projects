from tkinter import *
import calendar


class Calendar:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendar generator")
        self.master.geometry("400x150")
        self.master.configure(bg="grey")

        self.calendar_label = Label(master, text="Calendar generator", font=("Arial", 20), bg="grey", fg="#FFFFFA")
        self.calendar_label.pack(pady=15)

        self.enter_year_label = Label(master, text="Enter year:", bg="grey")
        self.enter_year_label.pack()

        self.enter_year_entry = Entry(master, width=10)
        self.enter_year_entry.pack()

        self.get_calendar_button = (
            Button(master, text="Generate calendar",
                   command=lambda: self.generate_calendar(self.enter_year_entry.get())))
        self.get_calendar_button.pack(pady=10)

    def generate_calendar(self, year):
        calendar_of_year_window = Toplevel()

        calendar_of_year = Label(calendar_of_year_window, text=f"{calendar.calendar(int(year))}")
        calendar_of_year.pack()


def main():
    root = Tk()
    calendar = Calendar(root)
    root.mainloop()


if __name__ == "__main__":
    main()
