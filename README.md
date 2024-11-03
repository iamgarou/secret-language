# secret-language
Coded Message and Decoder Program
Description
This Python program allows users to encode and decode messages. It offers two functionalities: creating a coded message by rearranging words and generating a secret message from a decoded format. The program handles words based on their length, applying different methods for encoding and decoding.

Features
Coded Message Creation: Transforms input messages by rearranging letters and adding random letters for words longer than 3 characters.
Decoding Functionality: Reverses the encoding process by rearranging characters back to their original order for longer words.
Requirements
Python 3.x
Usage
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/coded-message-decoder.git
cd coded-message-decoder
Run the program:

bash
Copy code
python coded_message.py
Choose an option:

Enter 1 to create a coded message.
Enter 2 to decode a previously coded message.
Example
Coded Message Creation:

plaintext
Copy code
1. To make a coded message.
2. To decode your secret message.
Your choice: 1
Write your message: Hello World
Llohe Rldow
Decoding a Message:

plaintext
Copy code
1. To make a coded message.
2. To decode your secret message.
Your choice: 2
Write your message: Llohe Rldow
Hello World
Notes
Ensure the input message contains words that vary in length to see the effect of encoding and decoding.
This program serves as a basic example of string manipulation and can be expanded with additional features for more complex coding schemes.
License
This project is licensed under the MIT License. See the LICENSE file for details
