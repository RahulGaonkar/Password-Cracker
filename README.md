# Password-Cracker
Password cracker is an system which can be used by penetration testers and network auditors to identify weak passwords
## Synopsis
Designed a Password cracker to crack plaintext passwords, SHA-1 hashed passwords and SHA-256 hashed passwords containing salt with the help of dictionary and brute force attacks by creating custom wordlist as well as using available wordlist
## How to Use
It has three parts which crack passwords depending on how the password is stored on disk
1. <b>Password_Cracker_Recovering_Plaintext_Passwords:</b><br>
Here 'Password_File_To_Be_Cracked.file' is a input file that contains passwords stored in the plaintext form and the password is cracked and stored in two steps in the Intermediate.txt and Cracked_Passwords.txt respectively.
2. <b>Password_Cracker_Dictionary_Attack_Recovering_SHA1_Hashed_Passwords:</b><br>
Here SHA-1 hashed passwords are cracked using the dictionary attack with the help of wordlist stored in the file 'Wordlist.txt',SHA1 hashes of the passwords to be cracked that are stored in 'SHA1_Hash.txt' and the cracked passwords are stored in 'Cracked_Passwords.txt'
3. <b>Password_Cracker_Dictionary_Attack_Recovering_SHA256_Hashed_Passwords_With_Salt:</b><br>
Here SHA-256 hashed passwords with salt are cracked using the hybrid attack which is a combination of dictionary and brute force attack where the program generates a custom wordlist that contains only four digit passwords containing lowercase alphabets and stores them in 'WordList_Generator.txt' which is preappended with a two digit numeric salt generated and stored in 'Salt.txt'.This result of preappending the salt with the word from the wordlist is stored in 'Salted_Word.txt' which is then used to crack SHA-256 hashed passwords with salt stored in 'SHA256_Hash.txt' and the cracked passwords are stored in 'Cracked_Passwords.txt'       
