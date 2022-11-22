from entities.user import User

class Workout:
    """Class for a one workout object. 
    
    Attributes: 
        - Workout name
        - Workout repetition
            - Weekly or monthly
        - Workout type
            - Weight lifting or cardio
        - Workout details, weight lifting
            - Progressive or maintaining
            - Sets
                - Name
                - Repetitions
                - Weights
        - Workout details, cardio
            - Type: Running, Swimming, Cycling, Walking or User defined
            - Duration
            - Heart rate zone
                - Moderate activity
                - Weight Control
                - Aerobic
                - Anaerobic
                - VO2 Maximum    
    """
    def __init__(self, name: str, repetition: bool, workout_type: str, workout_id:None):

        self.workout_name = name
        self.workout_repetition = repetition #Weekly: True, Monthly: False
        self.workout_type = workout_type
        self.workout_details_weight_lifting = {}
        self.workout_sets_weight_lifting = {}
        self.workout_details_cardio = {}
        self.workout_id = workout_id

    def add_weight_lifting_set(self, name, repetitions, weight):
        self.workout_sets_weight_lifting[name] = (repetitions, weight)



