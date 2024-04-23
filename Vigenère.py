BOARD = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'D' : 3,
    'E' : 4,
    'F' : 5,
    'G' : 6,
    'H' : 7,
    'I' : 8,
    'J' : 9,
    'K' : 10,
    'L' : 11,
    'M' : 12,
    'N' : 13,
    'O' : 14,
    'P' : 15,
    'Q' : 16,
    'R' : 17,
    'S' : 18,
    'T' : 19,
    'U' : 20,
    'V' : 21,
    'W' : 22,
    'X' : 23,
    'Y' : 24,
    'Z' : 25
} # Letters convert

def machine(text: str, overt: str, mode: bool) -> str:
    text_list: list[str] = []
    i: int = 0
    j: int = 0
    text = text.upper()
    overt = overt.upper()
    pices: str = list(text)
    overt = list(overt)
    for letter in pices:
        if(i >= len(overt) - j):
            i = 0
            j = 0
        if(letter == ' '):
            continue
        if(overt[i] == ' '):
            i += 1
            j += 1
        x = BOARD[letter]
        y = BOARD[overt[i]]
        i += 1
        if(mode):
            text_list.append(list(BOARD.keys())[list(BOARD.values()).index((x + y) % 26)])
        else:
            text_list.append(list(BOARD.keys())[list(BOARD.values()).index((x - y) % 26)])
    i = 0
    pices.reverse()
    for letter in pices:
        if(letter == ' '):
            text_list.insert(i, ' ')
        i -= 1
    text = ''.join(text_list)
    return text

def ui() -> None:
    while(True):
        print('---Vigenère cipher---\n1: Encript\n2: Dencript')
        x: str = input('Option: ')
        match x:
            case '1':
                message: str = input('Message: ')
                overt: str = input('Overt: ')
                print(machine(message, overt, True))
            case '2':
                ciphertext: str = input('Ciphertext: ')
                overt: str = input('Overt: ')
                print(machine(ciphertext, overt, False))
            case _:
                exit()

def main() -> None:
    ui()

if __name__ == '__main__':
    main()