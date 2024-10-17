# def format_change(f_name,l_name):
#
#     return f"{f_name.title()} {l_name.title()}"
#
# print(format_change("Simran","taMang"))

def fun_1(text):
    return text + text

def fun2(text):
    return text.title()

output = fun2(fun_1("hello"))
print(output)