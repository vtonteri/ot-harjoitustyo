from tkinter import Tk, ttk, constants
from repositories.user_repository import UserRepository

class NewUserWindow:
    
    def __init__(self, root, handle_new_user):
        self._root = root
        self._handle_new_user = handle_new_user
        self._frame = None

        self._create_user_window()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy_window(self):
        self._frame.destroy()

    def _create_user_window(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Hello")

        button = ttk.Button(
            master=self._frame,
            text="Say hello",
            command=self._handle_new_user
        )

        label.grid(row=0, column=0)
        button.grid(row=1, column=1)
        """
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Create New User")
        new_username_label = ttk.Label(master=self._frame, text="Enter new username")
        new_username_entry = ttk.Entry(master=self._frame)
        new_password_label = ttk.Label(master=self._frame, text="Enter password")
        new_password_entry = ttk.Entry(master=self._frame)
        label.grid(row=1, column=1, padx=5, pady=2)
        new_username_label.grid(row=2, column=0, padx=5, pady=2)
        new_username_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=2)
        new_password_label.grid(row=3, column=0, padx=5, pady=2)
        new_password_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=2)"""