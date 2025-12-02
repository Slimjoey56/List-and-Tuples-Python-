#Python List Slicing: Replacing Subsets of List Elements
computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
print(computer_parts)

# computer_parts [3] = "trackball"

print(computer_parts[3:])
computer_parts[3:] = ["trackball"]
print(computer_parts)
