import pickle
'''
#sss
sssssss
'''
file = open("./contacts.dat", mode="rb")
permsg = pickle.load(file)
print(permsg)
permsg = pickle.load(file)
print(permsg)
permsg = pickle.load(file)
print(permsg)
print("  hel  lo  ".strip())
file.close()