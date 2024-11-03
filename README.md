# secret-language
Coded Message Generator and Decoder
This Python program allows users to create coded messages or decode existing ones. It provides a fun way to obfuscate text using simple transformations based on word length and position.

Features
Coded Message Creation: Converts a user-provided message into a coded format by:
Adding random letters to the start of words with four or more characters.
Reversing shorter words (less than four characters).
Message Decoding: Reverts the coded message back to its original form using a simple decoding logic:
For longer words, it rearranges the letters back to their original positions.
For shorter words, it reverses them back.
Usage
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/coded-message-generator.git
cd coded-message-generator
Run the script:

bash
Copy code
python coded_message.py
Follow the on-screen prompts to either create a coded message or decode an existing one.

Requirements
Python 3.x
License
This project is licensed under the MIT License. See the LICENSE file for details
