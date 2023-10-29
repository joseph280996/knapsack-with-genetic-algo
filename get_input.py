from mappers.BoxMapper import mapInputToBox
from models.Box import Box
from utils import option_chooser_until_valid
"""
Pulbic Methods
"""


def run() -> list[Box]:
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

    return box_list


"""
Private Methods
"""

def _auto_generate_bag_values() -> list[Box]:
    return [Box(20, 6), Box(30, 5), Box(60, 8), Box(90, 7), Box(50, 6), Box(70, 9), Box(30, 4), Box(30, 5), Box(70, 4), Box(20, 9), Box(20, 2), Box(60, 1)]

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
        values = input("Enter the values of each bag in the form (w, v), separated by spaces: ")
        splitted_vals = values.strip().split()
        try:
            return list(map(mapInputToBox, splitted_vals))
        except Exception as e:
            print(e)
