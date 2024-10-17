programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    # "Loop": "The action of doing something over and over again",
}
print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

#wipe existing dictionary

# programming_dictionary = {}
# print(programming_dictionary)

#edit
programming_dictionary["Bug"] = "Moth value"
print(programming_dictionary)

#loop
for key in programming_dictionary:
    print(f"{key}: {programming_dictionary[key]}")
