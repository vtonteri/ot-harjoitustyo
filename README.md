# **Workout Diary**

One can create, save and follow a workout. Multiple users can use the application, with their own workouts.  

## **Notification about Python versions**

Application is tested with Python 3.9.7. There might be some problems especially with older Python versions.

## **Documentation**

**[Workout Diary Manual](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/manual.md)**

**[Requirements specification](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/vaatimusmaarittely.md)**

**[Testing document, still under construction](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/testing_document.md)**

**[Working diary](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/tuntikirjanpito.md)**

**[Changelog](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/changelog.md)**

**[Architecture](https://github.com/vtonteri/ot-harjoitustyo/blob/main/workout_diary/dokumentaatio/architecture.md)**


# **Workout diary manual**

## **How to start the application**

Application can be started by running *main.py* file, it is located in the src-directory's root.

Ways to run the *main.py* file:

- go to *workout_diary* -directory in a command shell or command prompt and type: **poetry install** and then **poetry run invoke start**

OR

- go to *workout_diary/src* -directory in a command shell or command prompt and type: **python3 main.py**

## **What the application does?**

At the moment application opens only a window, and tells user interesting information.

## **How to stop the application**

You can press *Stop application* button or just close the window.

## **How to run tests**

Tests can be run in the following way: 
- go to *workout_diary* -directory in a command shell or command prompt and type: **poetry run invoke test**