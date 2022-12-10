from tkinter import ttk, constants

class GoodbyeView:

    def __init__(self, root, handle_hello):
        self._root = root
        self._handle_hello = handle_hello
        self._frame = None
        self._entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Goodbye")

        button = ttk.Button(
            master=self._frame,
            text="Say hello",
            command=self._handle_hello
        )
        label.grid(row=0, column=0)
        button.grid(row=1, column=0)

        self._entry = ttk.Entry(master=self._frame)
        button1 = ttk.Button(master=self._frame, 
            text="Button1",
            command=self._handle_button_click
        )

        self._entry.grid(row=3, column=0)
        button1.grid(row=4, column=0)

        button_a = ttk.Button(
            master=self._frame,
            text="Button_A",
            command=lambda: self._handle_button_a_click("button_a")
        )
        button_a.grid(row=5, column=1)

        button_b = ttk.Button(
            master=self._frame,
            text="Button_B",
            command=lambda: self._handle_button_b_click("button_b")

        )
        button_b.grid(row=6, column=2)

    def _handle_button_click(self):
        entry_value = self._entry.get()
        print(f"VAlue of entry is {entry_value}")

    def _handle_button_a_click(self, value):
        entry_button_a = value
        print(f"Value = {entry_button_a}")

    def _handle_button_b_click(self, value):
        entry_button_b = value
        print(f"Value = {entry_button_b}")