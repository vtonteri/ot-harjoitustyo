from tkinter import ttk, Tk, constants
from tkinter import *
from tkcalendar import Calendar
from services.user_service import user_service
from services.workout_service import workout_service

class MainWindow:
    def __init__(self, root, handle_exit, handle_new_workout):
        self._root = root
        self._handle_exit = handle_exit
        self._handle_create_new_workout = handle_new_workout
        self._frame = None
        self._username = user_service.get_logged_in_username()

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
        
        selected_workout_canvas = Canvas(master=self._frame,  height=3)

        button_stop_application = ttk.Button(master=self._frame, 
                            text='Log out',
                            width=15, 
                            command=self._handle_exit)

        button_create_new_workout = ttk.Button(master=self._frame,
                            text="Create new workout",
                            width=30,
                            command=self._handle_create_new_workout)

        button_update_workouts = ttk.Button(master=self._frame,
                            text="Update workouts to calendar",
                            width=30,
                            command=self._update_workouts
                            )

        self._workout_calendar = Calendar(master=self._frame)
       
        heading_label.grid(row=0, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        #username_label.grid(row=2, column=0, padx=5, pady=5)

        #if workout_service.get_workouts(self._username) is not None:
        #    workout_to_canvas = workout_service.get_workouts(self._username)
        #    selected_workout_canvas.create_text(300, 50, text=workout_to_canvas, fill="black")

        selected_workout_canvas.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        button_create_new_workout.grid(row=5, columnspan=2, column=0, padx=5, pady=5)

        button_update_workouts.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
       
        button_stop_application.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
        
        self._workout_calendar.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight = 1, minsize=400)

    def _press_create_new_workout(self):
        self._handle_create_new_workout(self._username)

    def _update_workouts(self):
        workouts = workout_service.get_workouts(self._username)
        for row in workouts:
            print(row[0])
            print(row[1])
            print(row[2])
            print(row[3])
            print(row[4])
            print(row[5])
            print(row[6])
            print(row[7])
            
            
