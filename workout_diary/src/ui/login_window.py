from tkinter import ttk, constants, StringVar
from services.user_service import user_service, InvalidCredentialsError
from entities.user import User

class LoginWindow:
    def __init__(self, root, handle_exit, handle_create_user, show_main_view):
        self._root = root
        self._handle_exit = handle_exit
        self._handle_create_user = handle_create_user
        self._show_main_view = show_main_view
        self._frame = None
        self._error_message = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text="Welcome to Workout Diary!")
        
        self._error_message = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_message,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        login_label = ttk.Label(master=self._frame, text="Login:")

        username_label = ttk.Label(master=self._frame, text="Enter username:")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Enter password:")
        self._password_entry = ttk.Entry(master=self._frame)

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
        self._password_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        button_login_user.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        button_create_user.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        
        button_stop_application.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight = 1, minsize=400)

        self._hide_error()

    def _handle_login_user(self):

        self._login_username = self._username_entry.get()
        self._login_password = self._password_entry.get()

        try:
            user_service.login_user(self._login_username, self._login_password)
            self._show_main_view()
        except (InvalidCredentialsError):
            self._show_error("Invalid username or password222")

    def _show_error(self, message):
        self._error_message.set(message)
        self._error_label.grid()

        #user_logged_in = user_service.login_user(self._login_username, self._login_password_hashed)
        #user_logged_in = user_service.login_user(self._login_username, self._login_password)
        