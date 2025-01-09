file_testo = open("file.txt")

while(True):
    riga = file_testo.readline()

    if(riga == ''):
        break
    else:
        print(riga)

file_testo.close()
