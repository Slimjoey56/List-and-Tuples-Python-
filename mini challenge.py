generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
values = "".join(generated_list)
print(values)
values_list = values.split()
print(values_list)
# use a loop to produce a list of ints,rather than strings.
# You can create either modify the contents of the 'values_list' list in place,
# or create a new list of ints.
# replace the values in place
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

print(values_list)

#create a new list
integer_values = []
for value in values_list:
    integer_values.append(int(value))
print(integer_values)
