from tkinter import ttk, constants
from services.user_service import user_service
from repositories.user_repository import user_repository

class NewUserWindow:
    def __init__(self, root, handle_goodbye):
        self._root = root
        self._handle_goodbye = handle_goodbye
        self._frame = None
        self._new_password = None
        self._new_username = None
        self._error_message = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        "Method initilalizes Create New User window"


        self._frame = ttk.Frame(master=self._root) 
        label = ttk.Label(master=self._frame, text="Create New User")
        
        username_label = ttk.Label(master=self._frame, text="Enter new username:")
        self._new_username = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Enter password:")
        self._new_password = ttk.Entry(master=self._frame)

        "When button is pressed and "
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
        self._new_username.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        password_label.grid(row=3, column=0, padx=5, pady=5)
        self._new_password.grid(row=3, column=1, sticky=(constants.E, constants.W) , padx=5, pady=5)
        create_user_button.grid(row=4, columnspan= 2, column=1, padx=5, pady=5)
        exit_button.grid(row=5, column=1, columnspan=2, padx=5, pady= 5)

        self._frame.grid_columnconfigure(1, weight = 1, minsize=400)
   
    def _handle_create_new_user(self):

        _username_to_database = self._new_username.get()
        _password_to_database = self._new_password.get()
        _username_exist = user_repository.check_if_username_exist(_username_to_database)

        if _username_exist == False:

            password_to_database_hashed = user_service.hash_password(_password_to_database)
            user_service.create_user(_username_to_database, password_to_database_hashed)
        
        elif _username_exist == True:
            print("Username already in use, choose another.")

        self._new_username.delete(0, "end")
        self._new_password.delete(0, "end")



        


