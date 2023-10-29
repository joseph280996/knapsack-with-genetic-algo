def is_valid_choice(command: str, allowed_list: list[int]) -> bool:
    """
    This function will check if the user choice in the range of the given expected values

    Args:
        command: The user input
        allowed_list: The allowed list of values that the user can input

    Returns:
        A boolean indicating the validity of the user input
    """
    return command.isdigit() and int(command) in allowed_list

