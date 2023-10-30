from mappers.BoxMapper import mapInputToBox
from models.Box import Box
from utils import option_chooser_until_valid
"""
Pulbic Methods
"""


def run() -> tuple[list[Box], int, dict]:
    """
    This function will prompt user input and generate appropriate data based on user command.

    Possible values:
        (1) Manually input all values of boxes + its important
        (2) Use default values of the boxes
    """
    input_choice = _get_box_options()
    box_list = []

    match (input_choice):
        case 1:
            box_list = _get_user_input_box_values()
        case 2:
            box_list = _auto_generate_bag_values()

    end_condition_choice = _get_end_condition_choice()
    end_condition_setting = _get_end_condition_settings(end_condition_choice)
    

    return box_list, end_condition_choice, end_condition_setting


"""
Private Methods
"""

def _auto_generate_bag_values() -> list[Box]:
    return [
            Box(20, 6),
            Box(30, 5),
            Box(60, 8),
            Box(90, 7),
            Box(50, 6),
            Box(70, 9),
            Box(30, 4),
            Box(30, 5),
            Box(70, 4),
            Box(20, 9),
            Box(20, 2),
            Box(60, 1)
    ]

def _get_box_options() -> int:
    param_options = (
        "Pick an option: \n"
        + "(1): Manually input the values of bags\n"
        + "(2): Use default values for boxes\n"
        + "Your choice: "
    )

    command = option_chooser_until_valid.run(param_options, [1,2])

    return int(command)


def _get_user_input_box_values() -> list[Box]:
    splitted_vals = []

    while True:
        values = input("Enter the values of each bag in the form (w,v), separated by spaces: ")
        splitted_vals = values.strip().split()
        try:
            return list(map(mapInputToBox, splitted_vals))
        except Exception as e:
            print(e)

def _get_end_condition_choice():
    param_options = (
        "How do you want to end the algorithm? Pick an option: \n"
        + "(1): End with specified generations\n"
        + "(2): End after a specified seconds\n"
        + "(3): End after population converge\n"
        + "Your choice: "
    )

    command = option_chooser_until_valid.run(param_options, [1,2,3])
    return int(command)

def _get_end_condition_settings(end_condition_choice):
    
    match(end_condition_choice):
        case 1:
            generation_count = _get_number_input("Please enter the number of generation: ")
            return {"generations" : generation_count}
        case 2: 
            miliseconds = _get_number_input("Please enter the duration of the algorithm run: ")
            return {"run_period_in_ms": miliseconds}
        case _:
            return {}


def _get_number_input(message: str):
    while True:
        try:
            generation_count = int(input(message))
            return generation_count
        except Exception as e:
            print(e)

