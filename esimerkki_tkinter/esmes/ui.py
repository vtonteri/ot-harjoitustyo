from tkinter import Tk, ttk
from helloview import HelloView
from goodbyeview import GoodbyeView

class UI:
    def __init__(self, root):
        self._root = root
        self._entry = None
        self._current_view = None

    def start(self):
        self._show_hello_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _handle_button_click(self):
        entry_value = self._entry.get()
        print(f"VAlue of entry is {entry_value}")

    def _handle_button_a_click(self, value):
        entry_button_a = value
        print(f"Value = {entry_button_a}")

    def _handle_button_b_click(self, value):
        entry_button_b = value
        print(f"Value = {entry_button_b}")

    def _handle_goodbye(self):
        self._show_goodbye_view()

    def _handle_hello(self):
        self._show_hello_view()

    def _show_hello_view(self):
        self._hide_current_view()
        self._current_view = HelloView(
            self._root,
            self._handle_goodbye
        )
        self._current_view.pack()

    def _show_goodbye_view(self):
        self._hide_current_view()
        self._current_view = GoodbyeView(
            self._root,
            self._handle_hello
        )
        self._current_view.pack()

window = Tk()
window.title("TkInter example")

ui = UI(window)
ui.start()

window.mainloop()


"""
        self._entry = ttk.Entry(master=self._root)
        button = ttk.Button(master=self._root, 
            text="Button",
            command=self._handle_button_click
        )

        self._entry.grid(row=0, column=0)
        button.grid(row=1, column=0)

        button_a = ttk.Button(
            master=self._root,
            text="Button_A",
            command=lambda: self._handle_button_a_click("button_a")
        )
        button_a.grid(row=2, column=1)

        button_b = ttk.Button(
            master=self._root,
            text="Button_B",
            command=lambda: self._handle_button_b_click("button_b")

        )
        button_b.grid(row=3, column=2)
"""