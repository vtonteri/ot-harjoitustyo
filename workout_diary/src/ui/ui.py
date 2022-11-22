import tkinter as tk

class Ui:
    def __init__(self):
        pass

    def main_window():
        window = tk.Tk()
        window.title("Workout diary")
        window.geometry("1000x300")

        T = tk.Text(window, height=5, width=62)
        l = tk.Label(window, text="You have just started Ville Tonteri's first program - Workout Diary!")
        l.config(font=("Courier", 14))

        Fact = """Program doesn't yet have anything to show, except this window. 
        More to follow on coming weeks - stay tuned!"""

        
        button = tk.Button(window, text='Stop application', width=15, command=window.destroy)
        
        button.pack()
        l.pack()
        T.pack()
        T.place(x=280, y=150)
        l.place(x=120, y=80)
        button.place(x=450, y=250)
        T.insert(tk.END, Fact)
        window.mainloop()

