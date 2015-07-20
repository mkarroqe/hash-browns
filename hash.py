# hash(ed) browns? unfortunately, no
import hashlib

def init():
	infile = raw_input("Please enter the absolute path of the file you would like to hash: ")
	choice = raw_input("Would you like to hash your message as an MD5 xor a SHA-1? Type '1' for MD5 xor '2' for SHA-1.")
	
	if choice == "1":
		hash1 = md5generator(infile)
		print(hash1)
	elif choice == "2":
		hash2 = sha1generator(infile)
		print(hash2)
	else:
		print("Error :/.  I quit.")
		quit()

def md5generator(infile):
	print(infile)
	hasher = hashlib.md5()

	with open(infile, 'rb') as afile:
		buff = afile.read()
		hasher.update(buff)

	print(hasher.hexdigest())

	choice = raw_input("Would you like to create a SHA-1 hash? Type 'yes' or 'no'.")
	if choice == "yes":
		hash2 = sha1generator(infile)
		print(hash2)
		quit()
	else:
		print("k.")
		quit()

def sha1generator(infile):
	hasher = hashlib.sha1()

	with open(infile, 'rb') as afile:
		buff = afile.read()
		hasher.update(buff)

	print(hasher.hexdigest())

	choice = raw_input("Would you like to create a MD5 hash? Type 'yes' or 'no'.")
	if choice == "yes":
		hash1 = md5generator(infile)
		print(hash1)
		quit()
	else:
		print("k.")
		quit()

init()

# md5generator('/Users/mkarroqe/Desktop/myFile.txt')
# md5generator(infile)
# next let's decrypt this hehe