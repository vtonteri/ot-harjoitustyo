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
        self.dates = ["YYYY-MM-DD"]
        self.workouts_to_calendar = {}
        self.id_s_dates = []

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
        """Method hides current view"""
        self._frame.destroy()

    def _initialize(self):
        
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text="Welcome to Workout Diarys main view, here you view and edit your workouts!")
        
        self.selected_workout_text_box = Text(master=self._frame,  height = 7, width=50)

        button_stop_application = ttk.Button(master=self._frame, 
                            text='Log out',
                            width=15, 
                            command=self._handle_exit)

        button_create_new_workout = ttk.Button(master=self._frame,
                            text="Create new workout",
                            width=30,
                            command=self._handle_create_new_workout)

        button_update_workouts = ttk.Button(master=self._frame,
                            text="Update workouts from database",
                            width=30,
                            command=self._update_workouts
                            )

        
        self._show_workouts_menu_button()
     
        heading_label.grid(row=0, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        button_create_new_workout.grid(row=5, columnspan=2, column=0, padx=5, pady=5)

        button_update_workouts.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
       
        button_stop_application.grid(row=11, column=0, columnspan=2, padx=5, pady=5)

        self.selected_workout_text_box.grid(row=10, column=0, columnspan=2, padx=5, pady=5)
       
        self._frame.grid_columnconfigure(1, weight = 1, minsize=400)
        
    def _press_create_new_workout(self):
        self._handle_create_new_workout(self._username)

    def _show_workouts_menu_button(self):
        _show_workouts_menu = StringVar(self._frame, "Select date")
        button_show_workouts = OptionMenu(self._frame, _show_workouts_menu, *self.dates, command=self._show_workouts)
        button_show_workouts.grid(row=8, column=1, columnspan=2, padx=5, pady=5)
        

    def _update_workouts(self):
        workouts_from_database = workout_service.get_workouts(self._username)

        for row in workouts_from_database:
            if row[0] in self.workouts_to_calendar.keys():
                pass

            elif row[0] not in self.workouts_to_calendar.keys():
                self.workouts_to_calendar[row[0]] = [row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
                self.id_s_dates.append([row[0],row[3]])
                self.dates.append(str(row[3]))
        
        self._show_workouts_menu_button()

    def _show_workouts(self, selected_date):
        self.selected_workout_text_box.delete(1.0, END)
        for i in self.id_s_dates:
            if i[1] == selected_date:
                self.selected_workout_text_box.insert(END, "Workout name: " + self.workouts_to_calendar[i[0]][1] + "\n")
                self.selected_workout_text_box.insert(END, "Workout type: " + self.workouts_to_calendar[i[0]][4] + "\n")
                self.selected_workout_text_box.insert(END, "Workout sets: " + self.workouts_to_calendar[i[0]][5] + "\n")
                self.selected_workout_text_box.insert(END, "Workout details: " + self.workouts_to_calendar[i[0]][6] + "\n")        


