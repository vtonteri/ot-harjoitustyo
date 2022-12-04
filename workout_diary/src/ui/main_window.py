from tkinter import ttk, Tk, constants
from tkinter import *
from tkcalendar import Calendar

class MainWindow:
    def __init__(self, root, handle_exit, handle_new_workout):
        self._root = root
        self._handle_exit = handle_exit
        self._handle_create_new_workout = handle_new_workout
        self._frame = None

        self._initialize()

        """
        Args:
        root: passed from ui_final.py Tk ()
        handle_exit: passed from ui_final.py: _handle_exit_main_window (changes the view to login view)
        self._initialize initializes the main_view
        """

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text="Welcome to Workout Diarys main view, here you view and edit your workouts!")
        
        selected_workout_label = ttk.Label(master=self._frame, text="Workout:")
        selected_workout_canvas = Canvas(master=self._frame, height=3)

        password_label = ttk.Label(master=self._frame, text="Calendar")
        self._login_password = ttk.Entry(master=self._frame)

        button_stop_application = ttk.Button(master=self._frame, 
                            text='Log out',
                            width=15, 
                            command=self._handle_exit)

        button_create_new_workout = ttk.Button(master=self._frame,
                            text="Create new workout",
                            width=15,
                            command=self._handle_create_new_workout)

        self._workout_calendar = Calendar(master=self._frame)
       
        heading_label.grid(row=0, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        #username_label.grid(row=2, column=0, padx=5, pady=5)
        selected_workout_canvas.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label.grid(row=3, column=0, padx=5, pady=5)
        self._login_password.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
       
        button_stop_application.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        
        self._workout_calendar.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight = 1, minsize=400)