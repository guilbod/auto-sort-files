import sys, os

def displayHelp():
    print('''usage : main.py -p path_to_sort -m 1_or_2
    mode 1 : sort files by first letter
    mode 2 : sort files by file extension
display this help : main.py -h''')

def sortFilesByFirstLetter(path):
    list_dir = os.listdir(path)
    for file in list_dir:
        if os.path.isfile("./"+path+"/"+file):
            if not os.path.isdir("./"+path+"/"+file[0]):
                os.mkdir("./"+path+"/"+file[0])
            os.rename("./"+path+"/"+file, "./"+path+"/"+file[0]+"/"+file)

def sortFilesByExtension(path):
    list_dir = os.listdir(path)
    for file in list_dir:
        if os.path.isfile("./"+path+"/"+file):
            title, ext = os.path.splitext(file)
            extension = ext[1:] #to avoid hidden folder ".name"
            if not os.path.isdir("./"+path+"/"+extension):
                os.mkdir("./"+path+"/"+extension)
            os.rename("./"+path+"/"+file, "./"+path+"/"+extension+"/"+file)

def main():
    if(("-h" in sys.argv)):
        displayHelp()
    elif(len(sys.argv) != 5):
        displayHelp()
    else:
        if(sys.argv[1] == "-p"):
            if(sys.argv[3] == "-m"):
                if(int(sys.argv[4]) == 1):
                    sortFilesByFirstLetter(sys.argv[2])
                if(int(sys.argv[4]) == 2):
                    sortFilesByExtension(sys.argv[2])

main()
