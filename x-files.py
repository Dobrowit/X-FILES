#!/usr/bin/python3

from datetime import date, timedelta
import time
import subprocess

# Mapowanie liter na kształty ASCII (7x5)
ascii_letters = {
    'A': [
        "  #  ",
        " # # ",
        "#   #",
        "#   #",
        "#####",
        "#   #",
        "#   #",
    ],
    'B': [
        "#### ",
        "#   #",
        "#   #",
        "#### ",
        "#   #",
        "#   #",
        "#### ",
    ],
    'C': [
        " ####",
        "#    ",
        "#    ",
        "#    ",
        "#    ",
        "#    ",
        " ####",
    ],
    'D': [
        "#### ",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#### ",
    ],
    'E': [
        "#####",
        "#    ",
        "#    ",
        "#### ",
        "#    ",
        "#    ",
        "#####",
    ],
    'F': [
        "#####",
        "#    ",
        "#    ",
        "#### ",
        "#    ",
        "#    ",
        "#    ",
    ],
    'G': [
        " ### ",
        "#   #",
        "#    ",
        "# ###",
        "#   #",
        "#   #",
        " ### ",
    ],
    'H': [
        "#   #",
        "#   #",
        "#   #",
        "#####",
        "#   #",
        "#   #",
        "#   #",
    ],
    'I': [
        "#####",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
        "#####",
    ],
    'J': [
        "#####",
        "    #",
        "    #",
        "    #",
        "#   #",
        "#   #",
        " ### ",
    ],
    'K': [
        "#   #",
        "#  # ",
        "###  ",
        "###  ",
        "#  # ",
        "#   #",
        "#   #",
    ],
    'L': [
        "#    ",
        "#    ",
        "#    ",
        "#    ",
        "#    ",
        "#    ",
        "#####",
    ],
    'M': [
        "#   #",
        "## ##",
        "# # #",
        "# # #",
        "#   #",
        "#   #",
        "#   #",
    ],
    'N': [
        "#   #",
        "##  #",
        "##  #",
        "# # #",
        "#  ##",
        "#  ##",
        "#   #",
    ],
    'O': [
        " ### ",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        " ### ",
    ],
    'P': [
        "#### ",
        "#   #",
        "#   #",
        "#### ",
        "#    ",
        "#    ",
        "#    ",
    ],
    'Q': [
        " ### ",
        "#   #",
        "#   #",
        "#   #",
        "# # #",
        "#  ##",
        " ####",
    ],
    'R': [
        "#### ",
        "#   #",
        "#   #",
        "#### ",
        "#   #",
        "#   #",
        "#   #",
    ],
    'S': [
        " ### ",
        "#   #",
        "#    ",
        " ### ",
        "    #",
        "#   #",
        " ### ",
    ],
    'T': [
        "#####",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
    ],
    'U': [
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        " ### ",
    ],
    'V': [
        "#   #",
        "#   #",
        "#   #",
        "#   #",
        " # # ",
        " # # ",
        "  #  ",
    ],
    'W': [
        "#   #",
        "#   #",
        "#   #",
        "# # #",
        "# # #",
        "## ##",
        "#   #",
    ],
    'X': [
        "#   #",
        "#   #",
        " # # ",
        "  #  ",
        " # # ",
        "#   #",
        "#   #",
    ],
    'Y': [
        "#   #",
        "#   #",
        " # # ",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
    ],
    'Z': [
        "#####",
        "    #",
        "   # ",
        "  #  ",
        " #   ",
        "#    ",
        "#####",
    ],
    ' ': [
        "     ",
        "     ",
        "     ",
        "     ",
        "     ",
        "     ",
        "     ",
    ],
    ':': [
        "     ",
        "  #  ",
        "  #  ",
        "     ",
        "  #  ",
        "  #  ",
        "     ",
    ],
    '-': [
        "     ",
        "     ",
        "     ",
        " ### ",
        "     ",
        "     ",
        "     ",
    ],
    ')': [
        "  #  ",
        "   # ",
        "    #",
        "    #",
        "    #",
        "   # ",
        "  #  ",
    ],
    ';': [
        "     ",
        "  #  ",
        "  #  ",
        "     ",
        "  #  ",
        " #   ",
        "     ",
    ],
    '(': [
        "  #  ",
        " #   ",
        "#    ",
        "#    ",
        "#    ",
        " #   ",
        "  #  ",
    ],
    '_': [
        "     ",
        "     ",
        "     ",
        "     ",
        "     ",
        "     ",
        "#####",
    ],
    '3': [
        " ### ",
        "#   #",
        "    #",
        "  ## ",
        "    #",
        "#   #",
        " ### ",
    ],
}
    
def generate_ascii_text(text, char='#', width=52, height=7):
    # Tworzymy matrycę ASCII o zadanej szerokości i wysokości
    matrix = [[' ' for _ in range(width)] for _ in range(height)]

    # Wstawianie tekstu do matrycy
    x_offset = 0
    for letter in text:
        if letter.upper() in ascii_letters:
            letter_shape = ascii_letters[letter.upper()]
            for row in range(height):
                for col in range(len(letter_shape[row])):
                    if letter_shape[row][col] == '#':
                        # Ustawiamy znak na odpowiedniej pozycji w matrycy
                        if x_offset + col < width:
                            matrix[row][x_offset + col] = char
            x_offset += len(letter_shape[0]) + 1  # Przesuwamy o szerokość litery + 1 (odstęp)

            if x_offset >= width:
                break

    # Wypisujemy wynik
    for row in matrix:
        print(''.join(row))

    return matrix

def matrix_to_list(matrix):
    enumerated_list = []
    counter = 1
    for col in range(len(matrix[0])):  # Iterujemy po kolumnach
        for row in range(len(matrix)):  # Iterujemy po wierszach
            enumerated_list.append((counter, matrix[row][col]))
            counter += 1
    return enumerated_list
    
def execmd(command):
    try:
        result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = result.communicate()
        if stderr:
            print("Error", stderr)
        return stdout.strip() if not stderr else ""
    except subprocess.CalledProcessError as e:
        print("Error", f"Command failed: {e}")
        return ""
    
text = "AI_DEVS_3"
matrix = generate_ascii_text(text)
enumerated_matrix = matrix_to_list(matrix)

start_date = date(2023, 1, 1)
num_days = 364
dates = [start_date + timedelta(days=i) for i in range(num_days)]
date_mapping = {i + 1: dates[i] for i in range(num_days)}

execmd(f"sudo timedatectl set-ntp false")
i = 1
for element in enumerated_matrix:
    stan = enumerated_matrix[i-1][1]
    data = date_mapping[i]
    czas = '15:00:00'
    #print(element, data, stan)
    print(i)
    if stan == "#":
        for f in range(5): # jasność
            execmd(f"sudo timedatectl set-time '{data} {czas}'")
            #print(f"sudo timedatectl set-time '{data} {czas}'")
            file = f"file_{data}-{f}.txt"
            execmd(f"touch {file}")
            czas = f"15:{10+f}:00"
            execmd(f"git add .")
            execmd(f"git commit -m {text}")
    i = i + 1
execmd(f"sudo timedatectl set-ntp true")

# GIT_AUTHOR_DATE={date} GIT_COMMITTER_DATE={date} git commit --allow-empty -m "X-FILES" > /dev/null
