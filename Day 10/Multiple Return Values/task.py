def format_name(f_name, l_name):

    if f_name == "" or l_name == "":
        return "You didn't provide valid input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("f_name:"), input("l_name:")))
