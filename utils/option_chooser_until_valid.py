from validators import is_valid_choice

def run(input_message: str, possible_values: list[int]) -> str:
    is_valid_command, command = False, None
    while not is_valid_command:
        command = input(input_message)
        is_valid_command = is_valid_choice(command, possible_values)

    return command
