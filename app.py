#Path lib it's a library that works with file exploring
from pathlib import Path


path_email = Path("emails") #An object that works with 'emails' directory

if not path_email.exists(): #This function gives True or False if 'emails' directory NOT exists
    path_email.mkdir() #creating 'emails' directory

############################################
############################################

path_current = Path() #An object that works with current directory

#Let's store in a list all files
files_current = []

for file in path_current.glob("*"):
    files_current.append(file)

print(files_current)