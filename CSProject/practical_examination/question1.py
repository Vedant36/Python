# file with both functions. Note: pickle module needs to be installed.
import pickle as pc

def CreateFile(file='stock.dat'):
	# Checking if file exists. initializing data as list() if not
	try:
		fp = open(file, 'rb')
		# Getting data from file if it is not empty. initializing as list() if not
		try:
			data = pc.load(fp)
		except Exception:
			data = list()
		fp.close()
	except Exception:
		data = list()

	# User Interface
	n = int(input("Number of entries(Enter 0 to skip): "))
	print("Input entries in the format: Code, Description, Price")
	entries = list()
	for i in range(n):
		entries.append([i.strip() for i in input(f"Entry {i+1}: ").split(',')])
	data.extend(entries)

	# Writing all values to file
	with open(file, 'wb') as fp:
		pc.dump(data, fp)

def SearchRec(Code, file='stock.dat'):
	with open(file, 'rb') as fp:
		data = pc.load(fp)
	notFound = True
	for i in data:
		if i[0]==Code:
			print("Code found!")
			print(f"Description: {i[1]}")
			print(f"Price: {i[2]}")
			notFound = False
	if notFound:
		print("Code not found!")

# Wrapper code to execute the created functions
def main():
	CreateFile()
	Code = input("Enter Code to search: ")
	SearchRec(Code)

if __name__=='__main__':
	main()