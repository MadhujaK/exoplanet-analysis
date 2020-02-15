import timeit

with open('../exoApp.py','r') as codeFile:
  codeString = codeFile.read()
elapsed_time = timeit.timeit(codeString, number=100)/100
print("It took approximately "+ str(elapsed_time) +"s to run script")
