class reporter():
    
    @staticmethod
    def desp_errores(line: str, nline, err):
        """
        Metodo que se encarga de desplegar el texto de los errores del programa
        :param line: Cadena del codigo.
        :param nline: Indice de la linea de codigo.
        :param err: Codigo interno de error
            0 => Error operando tipo N
            1 => Error operando tipo DIR
            2 => Error comando no reconocido
            3 => Linea de codigo con terminacion invalida
        :return:
        """
        nline += 1
        line = line.replace('\n', ' ')

        if err == 0:
            print(f'Error en la linea de código: {nline}...')
            print(f'El operando N en {line}no pertenece a un hexadecimal...')
        elif err == 1:
            print(f'Error en la linea de código: {nline}...')
            print(f'El operando DIR en {line}no pertenece a un hexadecimal...')
        elif err == 2:
            print(f'Error en la linea: {nline}')
            print(f'{line}no es un comando válido...')
        elif err == 3:
            print(f'La linea de codigo {nline}:{line}no terminó como se esperaba...')