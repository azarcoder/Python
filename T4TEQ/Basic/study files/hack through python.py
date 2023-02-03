import hashlib
pass_hash=input('Enter md5 hash:')
wordlist=input('Enter the file:')
flag=0
try:
    pass_file=open(wordlist,"r")
except:
	print('No file found')
	quit()

for word in pass_file:

	encode_word=word.encode('utf-8')
    
    digest=hashlib.md5(encode_word.strplib()).hexdigest()

    print(word)
    print(diggest)
    print(pass_hash)

    if digest == pass_hash:
    	print('Pasword found')
    	print('Password is' + word)
    	flag=1
    	break
if flag==0:
	print('Password/Passphrase is not in the list')
