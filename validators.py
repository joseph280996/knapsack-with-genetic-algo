def is_valid_choice(command: str, allowed_list: list[int]) -> bool:
    return command.isdigit() and int(command) in allowed_list

