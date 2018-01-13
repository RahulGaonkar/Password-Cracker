with open('Password_File_To_Be_Cracked.file', 'r') as f:
    with open('Intermediate.txt', 'a') as f1:
        start = 0
        lines = f.readlines()
        for line in lines:
            if line == '1:ac1@associatedcontent.com:@fl!pm0de@\n' or start == 1:
                start = 1
                if line == '\n':
                    start = 0
                    break
                f1.write(line + '\n')
with open('Intermediate.txt', 'r') as f:
    with open('Cracked_Passwords.txt', 'w') as f1:
        for data in f:
            f1.write(data + '' + data.split(':')[-1])



