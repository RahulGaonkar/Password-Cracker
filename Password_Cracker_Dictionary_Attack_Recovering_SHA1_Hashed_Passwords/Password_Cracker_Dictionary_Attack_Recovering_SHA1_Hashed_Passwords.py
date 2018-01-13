# Dictionary Attack
# Reading the Wordlist
import hashlib
with open('Cracked_Passwords.txt', 'w')as f3:
    with open('Wordlist.txt', 'rb') as f:
        f_data = f.readlines()
        with open('SHA1_Hash.txt', 'r') as f1:
            f_data_1 = f1.readlines()
            for data in f_data:
                sliced_data = data.strip('\r\n')
                hex_dig = (hashlib.sha1(sliced_data)).hexdigest()
                for data1 in f_data_1:
                    sliced_data_1 = data1.strip('\n')
                    if hex_dig == sliced_data_1:
                        f3.write('Hash Value: ' + sliced_data_1 + ' ' + 'Cracked Password: ' + sliced_data + '\n')
