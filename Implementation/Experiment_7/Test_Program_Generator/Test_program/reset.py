# Copyright (C) 2018 Oyeniran Adeboye Stephen, Olusiji
def interrupt_function(file):
    file.write(" ;CODE MEMORY: (0x00000000-0x0000FFFF) \n")
    file.write(" ;DATA MEMORY: (0x00010000-0x0001FFFF) \n\n")
    offset = 0
    file.write(" org 0000 \n\n")
    file.write(" mfc0 $%d, $%d\n" % (16, 13))
    file.write(" beq $%d, $%d, %s\n\n" % (16, 0, "_reset"))
    
    file.write(" exception_handler: \n")
    file.write("\tmfc0 $%d, $%d\n" % (16, 12))
    file.write("\tmfc0 $%d, $%d\n" % (17, 13))
    file.write("\tmfc0 $%d, $%d\n" % (19, 14))
    file.write("\tmfc0 $%d, $%d\n" % (20, 15))
    file.write("\tsw $%s, %d($29)\n" % (16, offset))
    offset +=4
    file.write("\tsw $%s, %d($29)\n" % (17, offset))
    offset +=4
    file.write("\tsw $%s, %d($29)\n" % (19, offset))
    offset +=4
    file.write("\tsw $%s, %d($29)\n" % (20, offset))
    offset +=4
    file.write("\taddi $%d, $%d, %d\n" % (19, 19, 4))
    file.write("\tmtc0 $%d, $%d\n" % (19, 14))
    #file.write("\tmtc0 $%d, $%d\n" % (0, 13))
    file.write("\tmfc0 $%d, $%d\n" % (21, 12))
    file.write("\taddi $%d, $%d, %d\n" % (21, 21, 65533))
    file.write("\tori $%d, $%d, %d\n" % (21, 21, 1))
    file.write("\tmtc0 $%d, $%d\n" % (21, 12))
    file.write("\tcop0 %d\n" % (4))
    file.write("\tjr $%d\n" % (19))
    file.write("\n")

def end_program(file):
    file.write(" j %s\n\n" % ("end"))

def reset_function(file):
    file.write(" _reset: \n")
    for x in range(32):
        file.write("\txor $%d, $%d, $%d\n" % (x, x, x))
    file.write("\n")

def reset_reg(file):
    for x in range(29):
        if not ((x == 0)):
            file.write(" xor $%d, $%d, $%d\n" % (x, x, x))
    file.write("\n")

def reset_offsets(file, pattern_address, iterator, result_register):
    file.write("reset_offsets:\n")
    file.write("\tlui $%s, %d\n" % (pattern_address, 1))
    file.write("\tori $%s, $%s, %d\n" % (pattern_address, pattern_address, 8))
    file.write("\txor $%s, $%s, $%s\n" % (iterator, iterator, iterator))
    file.write("\txor $%s, $%s, $%s\n" % (result_register, result_register, result_register))
    file.write("\tjr $31\n\n")

def load_pattern(file, pattern_address):
    file.write("load_patterns:\n")
    file.write("\tlw $%d, %d($%s)\n" % (15, 0, pattern_address))
    file.write("\tlw $%d, %d($%s)\n" % (16, 4, pattern_address))
    file.write("\tjr $31\n\n")

def increment_offset(file, pattern_address, iterator, result_address):
    file.write("increment_offset:\n")
    file.write("\taddi $%s, $%s, %d\n" % (pattern_address, pattern_address, 8))
    file.write("\taddi $%s, $%s, %d\n" % (iterator, iterator, 2))
    file.write("\taddi $%s, $%s, %d\n" % (result_address, result_address, 4))
    file.write("\tjr $31\n\n")
    file.write("increment_immediate:\n")
    file.write("\taddi $%s, $%s, %d\n" % (pattern_address, pattern_address, 8))
    file.write("\taddi $%s, $%s, %d\n" % (result_address, result_address, 4))
    file.write("\tjr $31\n\n")

def increment(file, pattern_address, iterator, result_address):
    file.write("increment:\n")
    file.write("\taddi $%s, $%s, %d\n" % (result_address, result_address, 4))
    file.write("\tjr $31\n\n")

def reset_hi_lo(file):
    file.write("reset_hi_lo:\n")
    file.write("\tmthi $%d\n" % (0))
    file.write("\tmtlo $%d\n" % (0))
    file.write("\tjr $31\n\n")

def init_cp(file):
    file.write("init_cp:\n")
    file.write("\tmtc0 $%d, $%d\n" % (0, 12))
    file.write("\tmtc0 $%d, $%d\n" % (0, 13))
    file.write("\tmtc0 $%d, $%d\n" % (0, 14))
    file.write("\tmtc0 $%d, $%d\n" % (0, 15))
    file.write("\tjr $31\n\n")

def store_branch(file, source_register1, result_address):
    file.write("store_branch:\n")
    file.write("\tsw $%s, %d($%s)\n" % (source_register1, 0, result_address))
    file.write("\tjr $31\n\n")

def store(file, result_register, result_address):
    file.write("store:\n")
    file.write("\tsw $%s, %d($%s)\n" % (result_register, 0, result_address))
    result_register = int(result_register)+1
    file.write("\tsw $%d, %d($%s)\n" % (result_register, 0, result_address))
    file.write("\tjr $31\n\n")
