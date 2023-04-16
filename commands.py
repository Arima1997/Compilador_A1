from mnemonic import mnemo
from string import hexdigits

"""
Type of commands that do have a Value attribute that can be a 10 bit memory address
or a 8 bit value. All values should be unsigned int values.
"""
class val_cmd(mnemo):
    VAL_COMMANDS = {"MOV"   : {"MOV A,"     : 0,
                               "MOV A, ["   : 1,
                               "MOV SP"     : 9,
                               "MOV ["      : 10},
                    "ADD"   : 2,
                    "AND"   : 3,
                    "XOR"   : 6,
                    "OR"    : 4,
                    "JMP"   : 11,
                    "JC"    : 12,
                    "JZ"    : 13,
                    "JSR"   : 14}

    def __init__(self, cmd, code):
        value = self.find_value(cmd)
        super().__init__(cmd, code, value)
    
    def find_value(self, cmd_line : str):
        val = ""
        start_f = cmd_line.find("H")
        if start_f == -1:
            raise SyntaxError (f"The Number or Address in the command line: {cmd_line} doesn't have the identifier 'h' to the right of the number")
        start_f -= 1

        while cmd_line[start_f] in hexdigits:
            val = cmd_line[start_f] + val
            start_f -= 1
        if val == "":
            raise SyntaxError(f"The command {cmd_line} must have a hexadecimal numeric value as argument...")
        
        return int(val, base=16)


"""
Type of commands that doesn't have a value when called.
"""
class non_val_cmd(mnemo):
    NON_VAL_COMMANDS = {"NOT": 5, "LSL" : 7, "LSR" : 8, "RTS" : 15}

    def __init__(self, cmd, code):
        super().__init__(cmd, code, None)
    
    def __str__(self):
        return f"{self.code}"
    
if __name__ == '__main__':
    XOR = val_cmd("MOV [2FFH], A;", 10)
    NOT = non_val_cmd("NOT", 5)

    print("XOR command")
    print(XOR)
    print("\nPrinting NOT command")
    print(NOT)

    #for x in (val_cmd.VAL_COMMANDS, non_val_cmd.NON_VAL_COMMANDS):
    #    for y in x:
    #        print(y)
    #print(val_cmd.VAL_COMMANDS["MOV"]["MOV A,"])