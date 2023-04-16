import os
from commands import val_cmd, non_val_cmd


class reformatter:

    #Using Constructor of the parent class

    def create_cmd(self, linea, cod_val : list):
        if cod_val[1] == False:
            tmp_obj = non_val_cmd(linea, cod_val[0])
        else:
            tmp_obj = val_cmd(linea, cod_val[0])
        
        return tmp_obj
    
    def chk_fix_syntax(self, line : str):
        #Checks if the end of the code line is a semicolon. If not raise an error.
        if not line.endswith(";\n"):
            raise SyntaxError(f"Missing semicolon ';' at the end of the code line: {line}")
        
        #Converts all the string into uppercase to simplify the comparisons.
        line = line.upper()
        
        i = 0
        while i < line.__len__():
            #Eliminates multiple whitespaces and lets just one-
            while line[i].isspace() and line[i + 1].isspace():
                line = line[0:i+1] + line[i+2::]
            #If at the end of the line is a space between the last word and the semi_color
            #Eliminates that white space and replace it with the semicolon.
            if line[i].isspace() and line[i + 1] == ";":
                line = line[0:i] + line[i + 1]

            i += 1
            if line[i] == ";":
                break
        
        #Returns a simplified line of code.
        return line
    
    #Once we have a standarized line of code, we need to identify if is a valid command.
    def cmd_identifier(self, line : str):

        for x in val_cmd.VAL_COMMANDS:
            print(f"Printing VAL_COMMANDS from dictionary: {x}")
            #Compare each command name with the string.
            if x == "MOV":
                for y in val_cmd.VAL_COMMANDS[x]:
                    print(f"Internal MOV mnemonics: {y}")
                    if y in line:
                        return [val_cmd.VAL_COMMANDS[x][y], True]
            elif (x + " ") in line:
                return [val_cmd.VAL_COMMANDS[x], True]
                    
        for x in non_val_cmd.NON_VAL_COMMANDS:
            if (x + " ") in line or line == "RTS;":
                return [non_val_cmd.NON_VAL_COMMANDS[x], False]

        return None
    
    #def traducir(ensamblador: list):
    def __call__(self, file_read : list):
        """
        :param ensamblador:
        :return:
        """
        #List of command objects to return
        assembly_cmds = []
        std_file_read = []

        for x in file_read:
            print(x, len(x))
            std_file_read.append(self.chk_fix_syntax(x))

        for std_line in std_file_read:
            code_value = self.cmd_identifier(std_line)
            if code_value == None:
                raise SyntaxError (f"Line of code is not a command: {std_line}")
            assembly_cmds.append(self.create_cmd(std_line, code_value))
        
        #Return a list of command objects
        return assembly_cmds

#DEBUG CODE TO PROBE THE REFORMATTER
if __name__ == '__main__':
    arr = []
    hexa = []
    Ensamble = 'Ensamblador.txt'
    Hexadecimal = 'Chexa.txt'

    if not os.path.exists(Ensamble):
        f = open(Ensamble, 'x')
        f.close()

    try:
        f = open(Ensamble, 'r')
        arr = f.readlines()
    finally:
        f.close()

    hexa = reformatter.traducir(arr)
    if hexa != -1:
        print('Codigo ensamblador'.center(50, '-'))
        for i in arr:
            print(i, end='')

        print('Codigo Hexadecimal'.center(50, '-'))
        for i in hexa:
            print(i, end='')

