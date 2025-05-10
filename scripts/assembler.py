import argparse
import os
import sys
import json

def get_Args():
    parser = argparse.ArgumentParser(prog='8sc Assembler', description="Creates a program ROM for the 8sc processor")
    parser.add_argument("input", help="This is the assembly input file.")
    parser.add_argument("output", help="This is the file that the ROM is output to.")
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()

def open_Files(args):
    if not os.path.isfile(args.input):
        print("Error: Assembly file either does not exist or is not a file.")
        sys.exit(1)
    
    if os.path.exists(args.output) and not args.overwrite:
        print("Error: File or folder exists at output file location. Will not overwrite.")
        sys.exit(1)
    
    i = open(args.input, "r")
    o = open(args.output, "w")
    return i, o
 
def parse_Add(command, line_Number):
    binary_String = "000"
    
    registers = ["a","b","c","d"]
    r1 = command[1].lower()
    r2 = command[2].lower()
    
    if (r1 not in registers) or (r2 not in registers):
        print(f"Error: Assembler: Line {line_Number}: Invalid register name.")
        sys.exit(1)
    
    match r1:
        case "a":
            binary_String += "00"
        case "b":
            binary_String += "01"
        case "c":
            binary_String += "10"
        case "d":
            binary_String += "11"
    
    match r2:
        case "a":
            binary_String += "00"
        case "b":
            binary_String += "01"
        case "c":
            binary_String += "10"
        case "d":
            binary_String += "11"
    
    binary_String += "0"
    
    return binary_String

def parse_Nand(command, line_Number):
    binary_String = "001"
    
    registers = ["a","b","c","d"]
    r1 = command[1].lower()
    r2 = command[2].lower()
    
    if (r1 not in registers) or (r2 not in registers):
        print(f"Error: Assembler: Line {line_Number}: Invalid register name.")
        sys.exit(1)
    
    match r1:
        case "a":
            binary_String += "00"
        case "b":
            binary_String += "01"
        case "c":
            binary_String += "10"
        case "d":
            binary_String += "11"
    
    match r2:
        case "a":
            binary_String += "00"
        case "b":
            binary_String += "01"
        case "c":
            binary_String += "10"
        case "d":
            binary_String += "11"
    
    binary_String += "0"
    
    return binary_String
    

def parse_Shftrt(command, line_Number):
    binary_String = "010"
    
    registers = ["a","b","c","d"]
    r1 = command[1].lower()
    r2 = command[2].lower()
    
    if (r1 not in registers) or (r2 not in registers):
        print(f"Error: Assembler: Line {line_Number}: Invalid register name.")
        sys.exit(1)
    
    match r1:
        case "a":
            binary_String += "00"
        case "b":
            binary_String += "01"
        case "c":
            binary_String += "10"
        case "d":
            binary_String += "11"
    
    match r2:
        case "a":
            binary_String += "00"
        case "b":
            binary_String += "01"
        case "c":
            binary_String += "10"
        case "d":
            binary_String += "11"
    
    binary_String += "0"
    
    return binary_String
    

def parse_Bgt(command, line_Number):
    binary_String = "011"
    
    direction = command[1]
    
    if direction not in ["+","-"]:
        print(f"Error: Assembler: Line {line_Number}: Invalid direction name.")
        sys.exit(1)
    
    if not command[2].isdigit():
        print(f"Error: Assembler: Line {line_Number}: Constant is not a number.")
        sys.exit(1)
        
        
    value = int(command[2])
    
    if value > 15 or value < 0:
        print(f"Error: Assembler: Line {line_Number}: Constant is out of range.")
        sys.exit(1)
        
    if direction == "+":
        binary_String += "0"
    else:
        binary_String += "1"
    
    binary_String += bin(value)[2:].zfill(4)
    
    return binary_String


def parse_Ld(command, line_Number):
    binary_String = "100"
    
    registers = ["a","b","c","d"]
    r1 = command[1].lower()
    r2 = command[2].lower()
    
    if (r1 not in registers) or (r2 not in registers):
        print(f"Error: Assembler: Line {line_Number}: Invalid register name.")
        sys.exit(1)
    
    match r1:
        case "a":
            binary_String += "00"
        case "b":
            binary_String += "01"
        case "c":
            binary_String += "10"
        case "d":
            binary_String += "11"
    
    match r2:
        case "a":
            binary_String += "00"
        case "b":
            binary_String += "01"
        case "c":
            binary_String += "10"
        case "d":
            binary_String += "11"
    
    binary_String += "0"
    
    return binary_String

def parse_Str(command, line_Number):
    binary_String = "101"
    
    registers = ["a","b","c","d"]
    r1 = command[1].lower()
    r2 = command[2].lower()
    
    if (r1 not in registers) or (r2 not in registers):
        print(f"Error: Assembler: Line {line_Number}: Invalid register name.")
        sys.exit(1)
    
    match r1:
        case "a":
            binary_String += "00"
        case "b":
            binary_String += "01"
        case "c":
            binary_String += "10"
        case "d":
            binary_String += "11"
    
    match r2:
        case "a":
            binary_String += "00"
        case "b":
            binary_String += "01"
        case "c":
            binary_String += "10"
        case "d":
            binary_String += "11"
    
    binary_String += "0"
    
    return binary_String

def parse_Ldl(command, line_Number):
    binary_String = "110"
    registers = ['a', 'b']
    r1 = command[1].lower()
    
    if r1 not in registers:
        print(f"Error: Assembler: Line {line_Number}: Invalid register name.")
        sys.exit(1)
        
    match r1:
        case "a":
            binary_String += "0"
        case "b":
            binary_String += "1"
            
    if not command[2].isdigit():
        print(f"Error: Assembler: Line {line_Number}: Constant is not a number.")
        sys.exit(1)

    if int(command[2]) > 15 or int(command[2]) < 0:
        print(f"Error: Assembler: Line {line_Number}: Constant is out of range.")
        sys.exit(1)
    
    value = int(command[2])
    
    binary_String += bin(value)[2:].zfill(4)
    
    return binary_String
    
def parse_Ldh(command, line_Number):
    binary_String = "111"
    registers = ['a', 'b']
    r1 = command[1].lower()
    
    if r1 not in registers:
        print(f"Error: Assembler: Line {line_Number}: Invalid register name.")
        sys.exit(1)
        
    match r1:
        case "a":
            binary_String += "0"
        case "b":
            binary_String += "1"
            
    if not command[2].isdigit():
        print(f"Error: Assembler: Line {line_Number}: Constant is not a number.")
        sys.exit(1)

    if int(command[2]) > 15 or int(command[2]) < 0:
        print(f"Error: Assembler: Line {line_Number}: Constant is out of range.")
        sys.exit(1)
    
    value = int(command[2])
    
    binary_String += bin(value)[2:].zfill(4)
    
    return binary_String
    

def parse_Command(command, line_Number):
    binary_String = ""
    
    command_Selection = ['add', 'nand', 'shftrt', 'bgt', 'ld', 'str', 'ldl', 'ldh']
    c = command[0].lower()
    
    if c not in command_Selection:
        print(f"Error: Assembler: Line {line_Number}: Invalid command name.")
        sys.exit(1)
    
    match c:
        case "add":
            binary_String += parse_Add(command, line_Number)
        case "nand":
            binary_String += parse_Nand(command, line_Number)
        case "shftrt":
            binary_String += parse_Shftrt(command, line_Number)
        case "bgt":
            binary_String += parse_Bgt(command, line_Number)
        case "ld":
            binary_String += parse_Ld(command, line_Number)
        case "str":
            binary_String += parse_Str(command, line_Number)
        case "ldl":
            binary_String += parse_Ldl(command, line_Number)
        case "ldh": 
            binary_String += parse_Ldh(command, line_Number)
            
    return binary_String
    
def assemble_Line(line, line_Number):
    substrings = line.split()
    
    if not substrings[0].isdigit():
        print(f"Error: Assembler: Line {line_Number}: Address is not a number.")
        sys.exit(1)
    
    address = int(substrings[0])
    
    if address > 255 or address < 0:
        print(f"Error: Assembler: Line {line_Number}: Address is out of range.")
        sys.exit(1)
    
    
    parsed_Command = parse_Command(substrings[1:], line_Number)
    
    return address, parsed_Command
    

def assemble_Input(i_File):
    assembled = ["00000000"] * 256
    
    for line_Number, line in enumerate(i_File, start=1):
        if line.strip() == "":
            continue
        
        if line.split()[0] == "#":
            continue
        
        address, parsed_Command = assemble_Line(line, line_Number)
        assembled[address] = parsed_Command
    
    return assembled

def write_Output(o_File, assembled):
    json_Dict = {"words": assembled}
    json_Dump = json.dumps(json_Dict)
    o_File.write(json_Dump)
    o_File.flush()

def main():
    args = get_Args()
    i, o = open_Files(args)
    assembled = assemble_Input(i)
    write_Output(o, assembled)
    i.close()
    o.close()
    print("Finished assembling program.")
         
main()
