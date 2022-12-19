from tkinter import Tk, ttk, constants, OptionMenu, StringVar
from entities.user import User
from services.user_service import user_service
from repositories.user_repository import user_repository
from services.workout_service import workout_service
from tkcalendar import Calendar, DateEntry
import datetime


class CreateNewWorkoutWindow:
    def __init__(self, root, handle_exit):
        self._root = root
        self._handle_exit = handle_exit
        self._user = None
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()

    def _initialize(self):

        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Create new workout")

        workout_name = ttk.Label(master=self._frame, text="Enter workout name")
        self._workout_name = ttk.Entry(master=self._frame)

        date_and_time = ttk.Label(master=self._frame, text="Choose date: ")
        self._date_and_time = DateEntry(master=self._frame)

        repetition = ttk.Label(master=self._frame, text="Workout repetition: ")
        self._repetition_menu = StringVar()
        self._repetition = OptionMenu(self._frame, self._repetition_menu, "Weekly", "Monthly")

        workout_type = ttk.Label(master=self._frame, text="Workout type: ")
        self._workout_type_menu = StringVar()
        self._workout_type = OptionMenu(self._frame, self._workout_type_menu, "Weight-lift", "Cardio")

        workout_sets = ttk.Label(master=self._frame, text="Enter workout sets: ")
        self._workout_sets = ttk.Entry(master=self._frame)

        workout_details = ttk.Label(master=self._frame, text="Enter workout details")
        self._workout_details = ttk.Entry(master=self._frame)

        create_workout_button = ttk.Button(
            master=self._frame,
            text="Create new workout",
            command=self._handle_create_new_workout
        )

        exit_button = ttk.Button(
            master=self._frame,
            text="Exit",
            command=self._handle_exit
        )
        
        label.grid(row=0, column=0, padx=5, pady=5)

        workout_name.grid(row=1, column=0, padx=5, pady=5)
        self._workout_name.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        date_and_time.grid(row=2, column=0, padx=5, pady=5)
        self._date_and_time.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        repetition.grid(row=3, column=0, padx=5, pady=5)
        self._repetition.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        workout_type.grid(row=4, column=0, padx=5, pady=5)
        self._workout_type.grid(row=4, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        workout_sets.grid(row=5, column=0, padx=5, pady=5)
        self._workout_sets.grid(row=5, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        workout_details.grid(row=6, column=0, padx=5, pady=5)
        self._workout_details.grid(row=6, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        create_workout_button.grid(row=7, columnspan=2, column=1, padx=5, pady=5)

        exit_button.grid(row=8, columnspan=2, column=2, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=400)


    def _handle_create_new_workout(self):
        
        workout_name_to_database = self._workout_name.get()
        workout_username_to_database = user_service.get_logged_in_username()
        workout_date_to_database = self._date_and_time.get_date()
        workout_repetition_to_database = self._repetition_menu.get()
        workout_type_to_database = self._workout_type_menu.get()
        workout_sets_to_database = self._workout_sets.get()
        workout_details_to_database = self._workout_details.get()

        if workout_repetition_to_database == "weekly":
            workout_repetition_to_database = True
        elif workout_repetition_to_database == "monthly":
            workout_repetition_to_database = False

        print(f"{workout_name_to_database} {workout_username_to_database} {workout_date_to_database} {workout_repetition_to_database} {workout_type_to_database} {workout_sets_to_database} {workout_details_to_database}")

        workout_service.create_workout(workout_name_to_database, workout_username_to_database, workout_date_to_database, 
        workout_repetition_to_database, workout_type_to_database, workout_sets_to_database, workout_details_to_database)


