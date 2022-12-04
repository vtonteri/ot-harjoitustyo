from tkinter import ttk, constants

class LoginWindow:
    def __init__(self, root, handle_exit, handle_create_user, handle_login_user):
        self._root = root
        self._handle_exit = handle_exit
        self._handle_create_user = handle_create_user
        self._handle_login_user = handle_login_user
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text="Welcome to Workout Diary!")
        
        login_label = ttk.Label(master=self._frame, text="Login:")

        username_label = ttk.Label(master=self._frame, text="Username:")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password:")
        self._login_password = ttk.Entry(master=self._frame)

        button_stop_application = ttk.Button(master=self._frame, 
                            text='Stop application',
                            width=15, 
                            command=self._handle_exit)

        button_create_user = ttk.Button(master=self._frame, 
                            text="Create New User",
                            width=15, 
                            command=self._handle_create_user)

        button_login_user = ttk.Button(master=self._frame, 
                            text="Login",
                            width=15, 
                            command=self._handle_login_user)
        
        heading_label.grid(row=0, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        login_label.grid(row=1, column=0, sticky=constants.W, padx=5, pady=5)

        username_label.grid(row=2, column=0, padx=5, pady=5)
        self._username_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label.grid(row=3, column=0, padx=5, pady=5)
        self._login_password.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        button_login_user.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        button_create_user.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        
        button_stop_application.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight = 1, minsize=400)