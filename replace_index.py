import os
#this method only changes the first index and copies whole line to new line,after this you can remove lines via
#"keep specific classes" program. 
path="/home/ozbek/Desktop/text" #give the path of text folder
for f in os.listdir(path):
    with open(os.path.join(path,f), 'r+') as file :
        filedata = file.readlines()
        for x in filedata:
            replaced= x[0].replace(x[0], '0') #replace first index of line with 0
            edit= replaced + x[1:] #copy another indexis to new line
            file.write(edit)
