user_input = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [user_input[i+1] for i in range(0, len(user_input)-1) if user_input[i+1] > user_input[i]]
print(new_list)
