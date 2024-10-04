import os
import re


#Finds sprite folder
directory = os.path.join(os.path.dirname(__file__), 'Sprites')

#Lists all pictures in sprites folder
folderedFiles = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


for file in folderedFiles:
    #Takes all pictures
    if file.endswith(".png"):
        #re.sub removes all instances of 'Background Removed' from the name of file
        temp = re.sub(' Background Removed', '', file)
        #Renames file to temp
        os.rename(os.path.join(directory, file), os.path.join(directory, temp))