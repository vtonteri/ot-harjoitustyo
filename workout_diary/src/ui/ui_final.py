from tkinter import Tk, ttk, constants
from ui.login_window import LoginWindow
from ui.new_user_window import NewUserWindow
from ui.main_window import MainWindow
from ui.new_workout import CreateNewWorkout

class UI:
    def __init__(self, root) -> None:
        self._root = root
        self._current_view = None

        """Args:
        
        root = Tk()
        
        Class starts Workout Diary Application
        """

    def start_login(self): #function starts the application 
        self._show_login_view()

    def _hide_current_view(self): #function hides current view
        if self._current_view:
            self._current_view.destroy()
        
        self._current_view = None

    def _stop_application(self): #function stops application, is passed to _show_login_window. Used when "stop application" is pressed
        self._current_view.destroy()
        self._root.destroy()

    def _handle_exit_create_user(self): #Changes the _current_view
        if self._current_view:
            self._current_view.destroy()
        self._show_login_view()

    def _handle_exit_main_window(self): #Changes the _current_view
        if self._current_view:
            self._current_view.destroy()
        
        self._show_login_view()
    
    def _handle_exit_create_workout(self):
        if self._current_view:
            self._current_view.destroy()
        
        self._show_main_view()

    def _show_login_view(self): # Shows login view
        self._hide_current_view()
        self._current_view = LoginWindow(
            self._root,
            self._stop_application,
            self._show_create_user_view,
            self._show_main_view
        )
        self._current_view.pack()

    def _show_create_user_view(self): #Shows view, where user can create a new user
        self._hide_current_view()
        self._current_view = NewUserWindow(
            self._root,
            self._handle_exit_create_user,
        )
        self._current_view.pack()

    def _show_main_view(self): #Main view, showed after a user has logged in to application
        self._hide_current_view()
        self._current_view = MainWindow(
            self._root,
            self._handle_exit_main_window,
            self._show_create_new_workout,
        )
        self._current_view.pack()

    def _show_create_new_workout(self):
        self._hide_current_view()
        self._current_view = CreateNewWorkout(
            self._root,
            self._handle_exit_create_workout
        )
