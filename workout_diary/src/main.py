from ui.ui import UI
from tkinter import Tk
from initialize_database import initialize_database

def main():
    window = Tk()
    ui = UI(window)
    ui.start_login()
    window.title("WORKOUT DIARY")
    window.mainloop()

if __name__ == "__main__":
    initialize_database()
    main()
