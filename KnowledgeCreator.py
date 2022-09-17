from WriterClass import writer, Compiler, Counter
import os

def main():
    fileNombre= input("Enter the name of the file if it exists already:")+".txt"
    if os.path.isfile(fileNombre):
        print("Opening file")
        fileOpener(fileNombre)
    else:
        print("Creating file")
        fileSetter()

def fileSetter():
    textFile = Compiler(input("Enter the name of the file to be opened:"), input("Enter the title of this project:"))
    fileName = textFile.getFile() + ".txt"
    fileIn = open(fileName, "w")
    fileIn.write("*" * 4)
    fileIn.write(textFile.getTitle())
    fileIn.write("*" * 4 + "\n")
    fileIn.write("This is project: " + str(textFile.getNum()) +"\n")
    fileIn.close()
    fileOpener(fileName)

def fileOpener(file):
    fileIn = open (file, "a")
    counter = Counter(input("Enter the number of the item to follow:"))
    statements = []
    sentence = input("Write the statements learned:")
    statements.append(sentence)
    while len(sentence) != 0 :
        sentence = input("Write the statements learned:(leave it empty to finish it)")
        if sentence == "" :
            pass
        else:
            statements.append(sentence)
            print("appending of statements finished")
    fileIn.write(str(writer.datee+"\n"))
    for i in range(len(statements)):
        fileIn.write(str(counter.getCount()) +".-" )
        fileIn.write (statements[i] +"\n")
        counter.addUp()
    fileIn.close()

main()
