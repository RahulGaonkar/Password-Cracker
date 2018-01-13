import itertools
import hashlib
with open('Salt.txt', 'w') as f:
   characters = '0123456789'
   n = 2
   for x in itertools.product(characters, repeat=n):
      f.write(''.join(x) + '\n')
with open('WordList_Generator.txt', 'w') as f1:
   characters = 'abcdefghijklmnopqrstuvwxyz'
   n = 4
   for x in itertools.product(characters, repeat=n):
       f1.write(''.join(x) + '\n')
with open('Salt.txt', 'r') as f:
     with open('WordList_Generator.txt', 'r') as f1:
            with open('Salted_Word.txt', 'w') as f2:
                 for s in f:
                     for w in f1:
                         s_strip = s.strip('\n')
                         w_strip = w.strip('\n')
                         salted_word = s_strip + w_strip
                         f2.write(s_strip + w_strip + '\n')
with open('Cracked_Passwords.txt', 'w') as f2:
   with open('Salted_Word.txt', 'rb') as f1:
       f1_data = f1.readlines()
       with open('SHA256_Hash.txt', 'r') as f:
            f_data = f.readlines()
            for SW in f1_data:
                SW_strip = SW.strip('\r\n')
                hex_dig = (hashlib.sha256(SW_strip)).hexdigest()
                for fo in f_data:
                    fo_strip = fo.strip('\n')
                    if hex_dig == fo_strip:
                        f2.write('Hash Value: ' + fo + '\n' + 'Password including Salt: ' + SW + 'Cracked Password: ' + SW[2:] + '\n')

