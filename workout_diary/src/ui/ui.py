import tkinter as tk
from repositories.user_repository import UserRepository

class Ui:
    def __init__(self):
        pass

    def main_window():
        window = tk.Tk()
        window.title("Workout diary")
        window.geometry("1000x300")

        T = tk.Text(window, height=5, width=62)
        l = tk.Label(
            window, text="You have just started Ville Tonteri's first program - Workout Diary!")
        l.config(font=("Courier", 14))

        Fact = """Program doesn't yet have anything to show, except this window. 
        More to follow on coming weeks - stay tuned!"""

        button_stop_application = tk.Button(window, text='Stop application',
                           width=15, command=window.destroy)

        button_create_user = tk.Button(window, text="Create New User",
                            width=15, command=Ui._create_user_window)

        button_stop_application.pack()
        l.pack()
        T.pack()
        T.place(x=280, y=150)
        l.place(x=120, y=80)
        button_stop_application.place(x=450, y=250)
        button_create_user.place(x=450, y=200)
        T.insert(tk.END, Fact)
        window.mainloop()

    def _create_user_window(self):
        pass