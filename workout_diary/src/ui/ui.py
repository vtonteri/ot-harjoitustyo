from tkinter import Tk, ttk, constants
from repositories.user_repository import UserRepository
from ui.new_user_window import NewUserWindow

class UI:
    def __init__(self, root):
        self._root = root
        self._login_username = None
        self._login_password = None
        self._current_view = None
    
    def start(self):
        heading_label = ttk.Label(master=self._root, text="Welcome to Workout Diary!")
        
        login_label = ttk.Label(master=self._root, text="Login:")

        username_label = ttk.Label(master=self._root, text="Username")
        self._username_entry = ttk.Entry(master=self._root)

        password_label = ttk.Label(master=self._root, text="Password")
        self._login_password = ttk.Entry(master=self._root)

        button_stop_application = ttk.Button(master=self._root, text='Stop application',
                            width=15, command=self._root.destroy)

        button_create_user = ttk.Button(master=self._root, text="Create New User",
                            width=15, command=UI._create_user_window(self))

        button_login_user = ttk.Button(master=self._root, text="Login",
                            width=15, command=UI._main_window)
        
        heading_label.grid(row=0, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        login_label.grid(row=1, column=0, sticky=constants.W, padx=5, pady=5)

        username_label.grid(row=2, column=0, padx=5, pady=5)
        self._username_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label.grid(row=3, column=0, padx=5, pady=5)
        self._login_password.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        button_login_user.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        button_create_user.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        
        button_stop_application.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight = 1)

    def _handle_new_user(self):
        print("Class creates new user")

    def _create_user_window(self):
        self._current_view = NewUserWindow(self._root, self._handle_new_user)
        #self._current_view.pack()


    def _main_window(self):

        pass

window = Tk()
window.title("WORKOUT DIARY APPLICATION")
window.geometry("350x230")


ui = UI(window)
ui.start()
window.mainloop()