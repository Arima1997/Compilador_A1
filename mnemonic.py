"""
This object is the base to create all set of instructions that the
processor IMTC20 can execute.
"""
class mnemo():
    """
    The processor is able to execute sixteen commands, these are listed below here with their description.
    """
    description = {
        0  : 'Cargar Acumulador con un número “N”.',
        1  : 'Cargar Acumulador con el contenido de una dirección “DIR”.',
        2  : 'Sumar al Acumulador el contenido de una dirección “DIR”.',
        3  : 'AND lógico del Acumulador con el contenido de una dirección “DIR”.',
        4  : 'OR lógico del Acumulador con un número “N”.',
        5  : 'Complementar a uno el Acumulador.',
        6  : 'Substracción del Acumulador menos el contenido de una dirección “DIR”.',
        7  : 'Corrimiento lógico a la izquierda del acumulador (C <- ACC <- 0)',
        8  : 'Corrimiento lógico a la derecha del acumulador (0 -> ACC -> C)',
        9  : 'Cargar registro SP con un número “N”',
        10 : 'Guardar Acumulador en una dirección “DIR”.',
        11 : 'Saltar a la dirección “DIR”.',
        12 : 'Salta a la dirección “DIR” si el bit “C” está activado.',
        13 : 'Salta a la dirección “DIR” si el bit “Z” está activado.',
        14 : 'Salta a la subrutina ubicada en la dirección “DIR”',
        15 : 'Salir de la subrutina en ejecución'
    }
    
    def __init__(self, cmd, code, value):
        self.cmd    = cmd
        self.code   = code
        self.value  = value
        self.descr  = self.description[code]
        self.set_byte_size(value)

    def __eq__(self, value):
        if not isinstance(value, mnemo):
            raise ValueError(f"Can't compare {value}, not an instance of a mnemo class.")

    def __str__(self):
        return f"{self.code} {self.value}"

    def __repr__(self):
        return f"Command: {self.cmd}\nCode: {self.code}\nValue: {self.value}\nByte size: {self.byte_size}\nDescription: {self.descr}"
    
    def __getattribute__(self, name):
        if name == "code":
            return f"{super().__getattribute__('code'):02X}"
        elif name == "value":
            if super().__getattribute__('value') <= 255:
                return f"{super().__getattribute__('value'):02X}"
            else:
                tmpstr = f"{super().__getattribute__('value'):04X}"
                tmpstr = tmpstr[0:2]+ " " + tmpstr[2:4]
                return tmpstr
        else:
            return super().__getattribute__(name)

    def set_byte_size(self, val):
        if val == None:
            self.byte_size = 1
        elif val >= 0 and val <= 255:
            self.byte_size = 2
        elif val > 255 and val <= 1023:
            self.byte_size = 3
        else:
            raise ValueError(f"The Value attribute can't be a negative value: {val}")

"""
DEBUGGING AREA
"""
if __name__ == '__main__':
    MOV = mnemo("JC", 12, 1020)

    print("\nCalling command to print it hexadecimal representation...")
    print(MOV)
    print("\nCalling command method repr for debugging...")
    print(MOV.__repr__())
