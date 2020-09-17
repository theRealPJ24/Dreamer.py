from sys import argv
from datetime import datetime

def main():
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    code = {'A': 'F', 'B': 'w', 'C': 'e', 'D': 'A', 'E': 'M', 'F': 'k', 'G': 'K', 'H': 'j', 'I': 'h', 'J': 'f', 'K': 't', 'L': 'Z', 'M': 'N', 'N': 'l', 'O': 'x', 'P': 'L', 'Q': 'T', 'R': 'Y', 'S': 'r', 'T': 'Q', 'U': 'z', 'V': 's', 'W': 'a', 'X': 'O', 'Y': 'B', 'Z': 'd', 'a': 'c', 'b': 'p', 'c': 'E', 'd': 'g', 'e': 'u', 'f': 'b', 'g': 'I', 'h': 'J', 'i': 'G', 'j': 'o', 'k': 'D', 'l': 'R', 'm': 'P', 'n': 'n', 'o': 'H', 'p': 'y', 'q': 'q', 'r': 'X', 's': 'v', 't': 'S', 'u': 'W', 'v': 'i', 'w': 'm', 'x': 'V', 'y': 'C', 'z': 'U'}
    
    if len(argv) != 1:
        print('invalid format')
        return 0

    file_reader = open('dream_writer.txt', 'r')
    now = str(datetime.now()).split()
    name ='Dreams/' + now[0] +'.txt'

    file_writer = open(name, 'w')
    cipher = ''
    for i in file_reader.read():
        if i in alpha:
            cipher += code[i]
        else:
            cipher += i
    file_writer.write(cipher)


    file_reader.close()
    file_writer.close()


    
main()