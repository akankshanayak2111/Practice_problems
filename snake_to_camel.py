def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name."""

    new_str = variable_name.split("_")

    for i in range(1, len(new_str)):
        new_str[i] = new_str[i].capitalize()

    return "".join(new_str)
        
        