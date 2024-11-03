import string
import random 
        
print("1. To make a coded message.")
print("2. To decode your secret message.")

try:
    user_choice = int(input("Your choice: "))
    if user_choice<1 or user_choice>2:
        print("Choose from given options 1/2.")
except ValueError:
    print("Input should be a integer.")

if user_choice==1:
    user_msg = input("Write your message: ")
    split_msg = user_msg.split(" ")
    new_msg = []
    for msg in split_msg:
        if len(msg)>=4:
            word1 = "".join(random.choices(string.ascii_letters, k=2))
            new_word = word1 + msg[1:] + msg[0]
            new_msg.append(new_word)
        else:
            new_word = msg[::-1]
            new_msg.append(new_word)
    
    coded_msg = " ".join(new_msg)
    print(coded_msg)

if user_choice == 2:
    user_msg = input("Write your message: ")
    split_msg = user_msg.split(" ")
    new_msg = []
    for msg in split_msg:
        if len(msg)>=4:
            new_word = msg[len(msg)-1] + msg[2:len(msg)-1]
            new_msg.append(new_word)
        else:
            new_word = msg[::-1]
            new_msg.append(new_word)
    
    decoded_msg = " ".join(new_msg)
    print(decoded_msg)