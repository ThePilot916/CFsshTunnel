from typing import List


def box_equal_border(text: str) -> None:
    """
        Adds a box border made of "=" around the passed text
    """
    print("\n")
    text_split = text.split(sep='\n')
    if len(text_split[len(text_split) - 1]) == 0:
        text_split.pop(len(text_split) - 1)
    max_text_length = len(str(max(text_split, key=len)))
    print("+" + "=" * (max_text_length) + "+")
    for row in text_split:
        print("| " + row + " |")
    print("+" + "=" * (max_text_length) + "+")
    print("\n")


def seperator_config_border(config: List[str]) -> None:
    """
        Adds a seperator border made of "-" above and below the passed text, appended with "#" at the start
    """
    max_text_length = len(str(max(config, key=len)))
    print("#" + "-" * (max_text_length - 1))
    for row in config:
        print(row)
    print("#" + "-" * (max_text_length - 1))


def seperator_command_border(command: str) -> None:
    """
        Adds a seperator border made of "-" above and below the passed text
    """
    max_text_length = len(command)
    print("-" * (max_text_length))
    print(command)
    print("-" * (max_text_length))
