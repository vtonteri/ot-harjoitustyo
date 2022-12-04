from tkinter import ttk, constants
from entities.user import User
import bcrypt

class NewUserWindow:
    def __init__(self, root, handle_goodbye):
        self._root = root
        self._handle_goodbye = handle_goodbye
        self._frame = None
        self._new_password = None
        self._new_username = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Create New User")
        
        username_label = ttk.Label(master=self._frame, text="Enter new username:")
        username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Enter password:")
        new_password = ttk.Entry(master=self._frame)

        self._new_password = new_password.get()
        self._new_username = username_entry.get()

        create_user_button = ttk.Button(
            master=self._frame,
            text="Create new user",
            command=self._handle_create_new_user
        )

        exit_button = ttk.Button(
            master=self._frame,
            text="Exit",
            command=self._handle_goodbye
        )


        label.grid(row=0, column=0, padx=5, pady=5)
        username_label.grid(row=2, column=0, padx=5, pady=5)
        username_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        password_label.grid(row=3, column=0, padx=5, pady=5)
        new_password.grid(row=3, column=1, sticky=(constants.E, constants.W) , padx=5, pady=5)
        create_user_button.grid(row=4, columnspan= 2, column=1, padx=5, pady=5)
        exit_button.grid(row=5, column=1, columnspan=2, padx=5, pady= 5)

        self._frame.grid_columnconfigure(1, weight = 1, minsize=400)

    def _hash_password(self):
        self._new_password = str(self._new_password).encode('utf-8')
        print(f"has func: {self._new_password}")
        self._new_password_hashed = bcrypt.hashpw(self._new_password, bcrypt.gensalt(10))
    
    def _handle_create_new_user(self):

        try:
            self._new_password = self._initialize.new_password.get()
            self._new_username = self._initialize.username_entry.get()
        except:
            print("Enter username and password")

        print(f"password {self._new_password}")
        
        self._hash_password()
        new_user = User(self._new_username, self._new_password_hashed)
        print(new_user)
        
        


