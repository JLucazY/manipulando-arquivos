import os
try:
    f = open('d:/rato.txt', 'x', encoding='utf-8')
    f.close()

    f = open('d:/rato.txt', 'w', encoding='utf-8')
    f.write('o rato roeu')
    f.write(' a roupa do rei de Roma')
    f.close()

    f = open('d:/rato.txt', 'r', encoding='utf-8')
    for i in f:
        print(i)
    f.close()
except FileNotFoundError:
    print("Arquivo não encotrado")
