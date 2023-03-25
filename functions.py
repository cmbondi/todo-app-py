FILEPATH = "files/todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read text file and return list of
    to-dp items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-dp items list in the text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


"""
the __name__ variable == __main__ when this file is executed directly
If the cli.py file is executed then the __name__ variable here will
be equal to the script name, in this case functions so the code below
will not run
"""
if __name__ == "__main__":
    print("Do not execute the functions file directly!")
