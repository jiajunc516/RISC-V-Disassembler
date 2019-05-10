
def r_type(s):
    func3 = s[-15:-12]
    rd = bin_2_dec(s[-12:-7])
    rs1 = bin_2_dec(s[-20:-15])
    rs2 = bin_2_dec(s[-25:-20])
    func7 = s[0:7]
    op = ""
    if func3 == "000":
        if func7 == "0000000":
            op = "add"
        elif func7 == "0100000":
            op = "sub"
    elif func3 == "001":
        op = "sll"
    elif func3 == "010":
        op = "slt"
    elif func3 == "011":
        op = "sltu"
    elif func3 == "100":
        op = "xor"
    elif func3 == "101":
        if func7 == "0000000":
            op = "srl"
        elif func7 == "0100000":
            op = "sra"
    elif func3 == "110":
        op = "or"
    elif func3 == "111":
        op = "and"

    print ("{} r{},r{},r{}".format(op, rd, rs1, rs2))

def i_type(s):
    func3 = s[-15:-12]
    rd = bin_2_dec(s[-12:-7])
    rs1 = bin_2_dec(s[-20:-15])
    imm = bin_2_dec(s[0:12])
    op = ""
    shifti = False
    if func3 == "000":
            op = "addi"
    elif func3 == "010":
        op = "slti"
    elif func3 == "011":
        op = "sltiu"
    elif func3 == "100":
        op = "xori"
    elif func3 == "110":
        op = "ori"
    elif func3 == "111":
        op = "andi"
    else:
        shifti = True
        imm = bin_2_dec(s[7:12])
        if func3 == "001":
            op = "slli"
        elif func3 == "101":
            func7 = s[0:7]
            if func7 == "0000000":
                op = "srli"
            elif func7 == "0100000":
                op = "srai"

    print ("{} r{},r{},{}".format(op, rd, rs1, imm))

def s_type(s):
    func3 = s[-15:-12]
    imm2 = s[-12:-7]
    rs1 = bin_2_dec(s[-20:-15])
    rs2 = bin_2_dec(s[-25:-20])
    imm1 = s[0:7]
    op = ""
    if func3 == "000":
        op = "sb"
    elif func3 == "001":
        op = "sh"
    elif func3 == "010":
        op = "sw"

    print ("{} r{},{}(r{})".format(op, rs2, bin_2_dec(imm1+imm2), rs1))

def b_type(s):
    func3 = s[-15:-12]
    imm2 = s[-12:-7]
    rs1 = bin_2_dec(s[-20:-15])
    rs2 = bin_2_dec(s[-25:-20])
    imm1 = s[0:7]
    op = ""
    if func3 == "000":
        op = "beq"
    elif func3 == "001":
        op = "bne"
    elif func3 == "100":
        op = "blt"
    elif func3 == "101":
        op = "bge"
    elif func3 == "110":
        op = "bltu"
    elif func3 == "111":
        op = "bgeu"

    print ("{} r{},r{},{}".format(op, rs1, rs2, bin_2_dec(imm1+imm2)))

def u_type(s):
    opcode = s[-7:]
    rd = bin_2_dec(s[-12:-7])
    imm = bin_2_dec(s[0:21])
    op = ""
    if opcode == "0110111":
        op = "lui"
    elif opcode == "0010111":
        op = "auipc"
    print ("{} r{},{}".format(op, rd, imm))

def j_type(s):
    opcode = s[-7:]
    rd = bin_2_dec(s[-12:-7])
    imm = bin_2_dec(s[0:12])
    rs1 = ""
    rs1 = bin_2_dec(s[12:17])
    if opcode == "1101111":
        op = "jal"
        print ("{} r{},{}".format(op, rd, imm))
    elif opcode == "1100111":
        op = "jalr"
        print ("{} r{},r{},{}".format(op, rd, rs1, imm))

def load(s):
    func3 = s[-15:-12]
    rd = bin_2_dec(s[-12:-7])
    rs1 = bin_2_dec(s[-20:-15])
    imm = bin_2_dec(s[0:12])
    op = ''
    if func3 == '000':
        op = 'lb'
    elif func3 == '001':
        op = 'lh'
    elif func3 == '010':
        op = 'lw'
    elif func3 == '100':
        op = 'lbu'
    elif func3 == '101':
        op = 'lhu'

    print ("{} r{},{}(r{})".format(op, rd, imm, rs1))

def bin_2_dec(s):
    l = len(s) - 1
    dec = 0
    for i in s:
        dec += int(i) * (2 ** l)
        l -= 1
    return dec

if __name__ == '__main__':
    f = open ("inst.txt", 'r')
    instructions = f.read().split('\n')
    f.close()

    for l in instructions:
        opcode = l[-7:]
        if opcode == '0110011': # R_type
            r_type(l)
        elif opcode == '0010011': # i_type
            i_type(l)
        elif opcode == '0100011': # s_type
            s_type(l)
        elif opcode == '1100011': # b_type
            b_type(l)
        elif opcode == '0110111' or opcode == '0010111': # u_type
            u_type(l)
        elif opcode == '1101111' or opcode == '1100111': # j_type
            j_type(l)
        elif opcode == '0000011': # load
            load(l)
        else:
            print ("Unmatched opcode: {}\nInstruction: {}".format(opcode, l))

