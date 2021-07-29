This program is written in Python 3.
It uses the following libraries: sys, math, random.

OPTIONAL: Once program is cloned, and permissions are changed to execute, create alias by including
"alias crypter='python3 /path/to/file/main.py" in .bashrc

Example Usage:

crypter [OPTION] SOURCE DESTINATION

Letting test.txt be a file we want to encrypt, then we can use

"crypter e test.txt encrypted_test.txt"

Decrypting is simply

"crypter d encrypted_test.txt decrypted_test.txt"
