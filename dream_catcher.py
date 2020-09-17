from sys import argv

def main():
    if len(argv) != 2:
        print('Format: python3 dream_cather.py Dreams/filename')
        return 0
    try:
        file_reader = open('Dreams/' + str(argv[1]), 'r')
    except:
        print('Error!')
        return 0
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    dcode = {'F': 'A', 'w': 'B', 'e': 'C', 'A': 'D', 'M': 'E', 'k': 'F', 'K': 'G', 'j': 'H', 'h': 'I', 'f': 'J', 't': 'K', 'Z': 'L', 'N': 'M', 'l': 'N', 'x': 'O', 'L': 'P', 'T': 'Q', 'Y': 'R', 'r': 'S', 'Q': 'T', 'z': 'U', 's': 'V', 'a': 'W', 'O': 'X', 'B': 'Y', 'd': 'Z', 'c': 'a', 'p': 'b', 'E': 'c', 'g': 'd', 'u': 'e', 'b': 'f', 'I': 'g', 'J': 'h', 'G': 'i', 'o': 'j', 'D': 'k', 'R': 'l', 'P': 'm', 'n': 'n', 'H': 'o', 'y': 'p', 'q': 'q', 'X': 'r', 'v': 's', 'S': 't', 'W': 'u', 'i': 'v', 'm': 'w', 'V': 'x', 'C': 'y', 'U': 'z'}
    dream = ''
    for i in file_reader.read():
        if i in alpha:
            dream += dcode[i]
        else:
            dream += i
    print(dream)

main() 