# Adding Items to a List with Append: Python By Exampl
available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable",
                   "dvd drive"
                   ]
# valid_choices = [str(i) for i in range(len(available_parts)+1)]
# print(valid_choices)
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
current_choice = "-"
computer_parts = []

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_parts = available_parts[index]
        if chosen_parts in computer_parts:
            #its already in, so remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_parts)
        else:
            computer_parts.append(chosen_parts)
        print("Your List now contains: {} ".format(computer_parts))


    else:
        print("Please add options from the list below  ")
        for number, parts in enumerate(available_parts):
            print("{0}:\t{1}".format(number + 1, parts))

    current_choice = input()

print(computer_parts)
