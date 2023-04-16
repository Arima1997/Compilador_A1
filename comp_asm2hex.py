"""
Assembler to Hexadecimal compiler.
This software is created to compile an Asembler code to its corresponding rpresentation
in hexadecimal code, that this will be saved in a ROM memory to be used as a program
of my processor IMTC20.
"""
print(f'Andrés Rivera Márquez.')
print(f'''Este programa realiza la conversión de un archivo de texto de código
ensamblador a un archivo de texto que contiene su representación en código
hexadecimal para su guardado en una memoria ROM.''')

from Reformatter import reformatter
from file_manager import file_mgr
#import env.defines

RutaEnsamblador = 'Ensamblador.txt'
RutaHexadecimal = 'Hexadecimal.txt'

d = None
while d != 0:
    print(f'''
Que desea realizar?
1: Traducir codigo a Hexadecimal
2: Especificar ruta de codigo Ensamblador
3: Especificar ruta de guardado del ensable
4: Imprimir status actual...
0: Finalizar''')
    d = int(input('Ingrese la opcion deseada: '))
    print('\n')

    if d == 1:
        f_mgr = file_mgr(RutaEnsamblador, RutaHexadecimal)
        print("File manager created")
        compiler = reformatter()
        print("Compiler created")

        f_mgr.create_file()
        CodEnsa = f_mgr.read_file()

        if CodEnsa == 0:
            raise SystemError(f'El archivo {RutaEnsamblador} no contiene información...')
    
        print(f'Se obtuvo la información de {RutaEnsamblador}...')
        CodHexa = compiler(CodEnsa)
        if CodHexa == -1:
            raise SystemError('No se ha podido realizar la conversión...')
        else:
            f_mgr.write_file(CodHexa)
            print(f'Se ha generado el archivo {RutaHexadecimal} exitosamente...')
    elif d == 2:
        RutaEnsamblador = input("Indique la ruta del archivo a leer... ")
    elif d == 3:
        RutaHexadecimal = input("Indique la ruta de guardado... ")
    elif d == 4:
        print(RutaEnsamblador)
        print(RutaHexadecimal)
