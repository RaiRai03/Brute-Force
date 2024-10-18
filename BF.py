def brute_force(password_length, chars):
    # Initialize a list to hold the current combination
    result = [''] * password_length
    total_chars = len(chars)

    # Use a loop to generate combinations
    while True:
        # Print the current combination
        print(''.join(result))

        # Find the rightmost character to increment
        for i in range(password_length - 1, -1, -1):
            if result[i] == '':
                result[i] = chars[0]  # Start with the first character
                break
            elif result[i] == chars[-1]:
                result[i] = ''  # Reset to empty if at the last character
            else:
                # Move to the next character
                result[i] = chars[chars.index(result[i]) + 1]
                break
        else:
            # If we finished all combinations, exit the loop
            break

# User Input
password_length = int(input("Enter the password length: "))
chars = input("Enter the characters to use: ")
brute_force(password_length, chars)