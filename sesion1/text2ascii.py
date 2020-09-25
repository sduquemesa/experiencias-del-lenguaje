""" Conversor de texto a ASCII

Este script convierte los carácteres de un texto a su código ASCII
y guarda el resultado en el archivo output.txt

Este script acepta entrada de texto directamente de la terminal.

Para usar un archivo de texto corra este scrip con la opción --file
    python3 text2ascii --file [nombre_del_archivo.txt]
"""

import argparse

parser = argparse.ArgumentParser(description='Convierte texto a su representacion en ASCII')
parser.add_argument('--file', metavar='N', type=str, nargs='+',
                    help='archivo de texto')

args = parser.parse_args()

if args.file:
    filename = args.file[0]
    ascii_list = []
    with open(filename, 'r') as filehandle:
        for line in filehandle:
            text = line.strip()
            for char in text:
                ascii_list.append( str(ord(char)) )
else:
    text = input("Inserte su texto aquí: \n")
    ascii_list = [str(ord(char)) for char in text]

with open('output.txt', 'w') as filehandle:
    filehandle.write('\n'.join(ascii_list))

print('Se guardó un archivo de {} carácteres'.format(len(ascii_list)))