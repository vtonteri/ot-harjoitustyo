from ui.ui_final import UI
from tkinter import Tk


def main():
    window = Tk()
    ui = UI(window)
    ui.start_login()
    window.title("WORKOUT DIARY")
    window.mainloop()

if __name__ == "__main__":
    main()
