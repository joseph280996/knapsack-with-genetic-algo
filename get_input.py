from validators import is_valid_choice

"""
Pulbic Methods
"""


def get_inputs() -> tuple[list[int], int]:
    """
    This function will prompt user input and generate appropriate data based on user command.

    Possible values:
        (1) Manually input all values of boxes + its important
        (2) Auto generate the boxes values

    Notes:
        For manual, if the input is not in range from 1-10, it will continuously ask the user to reinput until success
    """
    input_choice = _get_box_values()
    unordered_pancakes_stack = []

    match (input_choice):
        case 1:
            unordered_pancakes_stack = _get_user_input_box_values()
        case 2:
            unordered_pancakes_stack = _generate_unsorted_continuous_values(10, 1, 10)

    algo_choice = _get_algo_choice()
    return unordered_pancakes_stack, algo_choice


"""
Private Methods
"""

def _is_list_has_non_digit_str(str_list: list[str]) -> bool:
    return any(list(map(lambda s: not s.isdigit(), str_list)))

def _auto_generate_bag_values():


def _get_box_values() -> int:
    param_options = (
        "Pick an option: \n"
        + "(1): Manually input the values of bags\n"
        + "(2): Auto generate values of bags\n"
        + "Your choice: "
    )

    is_valid_command, input_choice = False, 0
    while not is_valid_command:
        command = input(param_options)
        is_valid_command = is_valid_choice(command, [1, 2])

    if is_valid_command:
        input_choice = int(command)

    return input_choice


def _get_user_input_box_values() -> list[int]:
    is_user_input_valid, splitted_vals = False, []

    while not is_user_input_valid:
        values = input("Enter the numbers, separated by spaces: ")
        splitted_vals = values.strip().split()
        is_user_input_valid = _is_list_has_non_digit_str(
            splitted_vals
        ) and _is_valid_list(splitted_vals)

    return list(map(int, splitted_vals))
