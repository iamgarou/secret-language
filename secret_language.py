import string  # Import string module for string constants
import random  # Import random module for generating random choices

# Display options for the user
print("1. To make a coded message.")
print("2. To decode your secret message.")

# Get user choice with error handling
try:
    user_choice = int(input("Your choice: "))
    if user_choice < 1 or user_choice > 2:
        print("Choose from given options 1/2.")
except ValueError:
    print("Input should be a integer.")

# If the user chooses to create a coded message
if user_choice == 1:
    user_msg = input("Write your message: ")  # Prompt for user message
    split_msg = user_msg.split(" ")  # Split message into words
    new_msg = []  # Initialize a list for the coded message
    for msg in split_msg:
        if len(msg) >= 4:  # Check if the word has 4 or more characters
            word1 = "".join(random.choices(string.ascii_letters, k=2))  # Generate 2 random letters
            new_word = word1 + msg[1:] + msg[0]  # Create new word by rearranging and adding random letters
            new_msg.append(new_word)  # Append to the new message list
        else:
            new_word = msg[::-1]  # Reverse the word if it has less than 4 characters
            new_msg.append(new_word)  # Append reversed word

    coded_msg = " ".join(new_msg)  # Join the new words into a single message
    print(coded_msg)  # Print the coded message

# If the user chooses to decode a message
if user_choice == 2:
    user_msg = input("Write your message: ")  # Prompt for user message
    split_msg = user_msg.split(" ")  # Split message into words
    new_msg = []  # Initialize a list for the decoded message
    for msg in split_msg:
        if len(msg) >= 4:  # Check if the word has 4 or more characters
            new_word = msg[len(msg) - 1] + msg[2:len(msg) - 1]  # Rearrange the characters to decode
            new_msg.append(new_word)  # Append to the new message list
        else:
            new_word = msg[::-1]  # Reverse the word if it has less than 4 characters
            new_msg.append(new_word)  # Append reversed word

    decoded_msg = " ".join(new_msg)  # Join the new words into a single message
    print(decoded_msg)  # Print the decoded message
