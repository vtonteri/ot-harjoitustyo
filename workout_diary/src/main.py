from tkinter import Tk
from ui.ui import UI

def main():
    """Starts Workout application"""
    window = Tk()
    ui = UI(window)
    ui.start_login()
    window.title("WORKOUT DIARY")
    window.mainloop()

if __name__ == "__main__":
    main()
