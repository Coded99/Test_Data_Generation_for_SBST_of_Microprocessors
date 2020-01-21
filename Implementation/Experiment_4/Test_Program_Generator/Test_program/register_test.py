# Copyright (C) 2019 Oyeniran Adeboye Stephen
import os
registerFile_1 = "../input/register_data_1.txt" # Data for testing register decoder
registerFile_0 = "../input/register_data_0.txt" # Data for testing register decoder
offset = 0

##################################################################################
def reg_init_upward(out,data, number, pattern_address):
 out.write(" init_upward_"+str(number)+":\n")
 register = 0
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if not ((register == 31) or (register == 29)):
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))

    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\tjr $31\n\n")
 data_f.close

##################################################################################
def reg_init_downward(out,data, number, pattern_address):
 data_f = open(data,'r')
 out.write("init_downward_"+str(number)+":\n")
 register = 31
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if not ((register == 31) or (register == 29)):
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
    if (register <= 0):
      register = 31
    else:
      register -= 1
 out.write("\tjr $31\n\n")
 data_f.close

##################################################################################
def reg_upward_special(out,data, data2, result_address):
 register = 0
 global offset
 data_f = open(data,'r')
 line = data_f.readlines()

 data_f2 = open(data2,'r')
 line2 = data_f2.readlines()
 for i in (line2):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if not ((register == 1)):
      out.write("\tand $%d, $%d, $%d\n" % (register, register, register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      offset += 4
    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\n")

 for i in (line):
   bit_set1 = i[:16]
   bit_set2 = i[16:32]
   most_sig_bit   = int(bit_set1,2)
   least_sig_bit  = int(bit_set2,2)

   if not((register == 1)):
     out.write("\tnor $%d, $%d, $%d\n" % (register, register, register))
     out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
     out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
     out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
     offset += 4
     out.write("\tand $%d, $%d, $%d\n" % (register, register, register))
     out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
     offset += 4
   if (register <= 0):
     register = 31
   else:
     register -= 1
 out.write("\n")

 data_f.close
 data_f2.close
##################################################################################

def reg_upward_special_mirror(out,data, data2, result_address):
 out.write(";.............special register mirror.............;\n")
 register = 0
 global offset
 data_f = open(data,'r')
 line = data_f.readlines()
 data_f2 = open(data2,'r')
 line2 = data_f2.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if not ((register == 1)):
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))

    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\n")

 for i in (line2):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if  not ((register == 1)):
      out.write("\tnor $%d, $%d, $%d\n" % (register, register, register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      offset += 4
    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\n")

 for i in (line):
   bit_set1 = i[:16]
   bit_set2 = i[16:32]
   most_sig_bit   = int(bit_set1,2)
   least_sig_bit  = int(bit_set2,2)

   if not ((register == 1)):
     out.write("\tand $%d, $%d, $%d\n" % (register, register, register))
     out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
     out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
     out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
     offset += 4
     out.write("\tand $%d, $%d, $%d\n" % (register, register, register))
     out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
     offset += 4
   if (register <= 0):
     register = 31
   else:
     register -= 1
 out.write("\n")

 data_f.close
 data_f2.close
##################################################################################
#                 Data part testing                                              #
##################################################################################
def reg_upward_special_datapart(out,data, data2, result_address):
 register = 0
 global offset
 data_f = open(data,'r')
 line = data_f.readlines()

 data_f2 = open(data2,'r')
 line2 = data_f2.readlines()
 for i in (line2):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if not ((register == 1)):
      out.write("\tlui $%d, %d\n" % (register, 65535))
      out.write("\tori $%d, $%d, %d\n" % (register, register, 65535))

      out.write("\tand $%d, $%d, $%d\n" % (register, register, register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      offset += 4

      out.write("\tnor $%d, $%d, $%d\n" % (register, register, register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, 65535))
      out.write("\tori $%d, $%d, %d\n" % (register, register, 65535))
      offset += 4
      out.write("\tand $%d, $%d, $%d\n" % (register, register, register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      offset += 4

    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\n")

 data_f.close
 data_f2.close
##################################################################################

def reg_upward_special_mirror_datapart(out,data, data2, result_address):
 out.write(";.............special register mirror.............;\n")
 register = 0
 global offset
 data_f = open(data,'r')
 line = data_f.readlines()
 data_f2 = open(data2,'r')
 line2 = data_f2.readlines()

 for i in (line2):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if  not ((register == 1)):
      out.write("\tlui $%d, %d\n" % (register, 0))
      out.write("\tori $%d, $%d, %d\n" % (register, register, 0))

      out.write("\tnor $%d, $%d, $%d\n" % (register, register, register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      offset += 4

      out.write("\tand $%d, $%d, $%d\n" % (register, register, register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, 0))
      out.write("\tori $%d, $%d, %d\n" % (register, register, 0))
      offset += 4
      out.write("\tand $%d, $%d, $%d\n" % (register, register, register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      offset += 4

    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\n")

 data_f.close
 data_f2.close

##################################################################################

def hi_lo_upward_special(out,inst,data, data2, result_address):
 register = 0
 global offset
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if  not ((register == 1)):
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))

    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\n")

 data_f2 = open(data2,'r')
 line2 = data_f2.readlines()
 for i in (line2):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if  not ((register == 1)):
      instruction = str.strip(inst)[0:5]
      out.write("\t%s $%d\n" % (inst, register))
      #out.write(" %s $%d, $%d\n" % (instruction, register, register))
      if ((inst == "mthi") or (inst == "multu1")):
        out.write("\tmfhi $%d\n" % (register))
      else:
        out.write("\tmflo $%d\n" % (register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      offset += 4
    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\n")

 for i in (line):
   bit_set1 = i[:16]
   bit_set2 = i[16:32]
   most_sig_bit   = int(bit_set1,2)
   least_sig_bit  = int(bit_set2,2)

   if  not ((register == 1)):
     out.write("\t%s $%d\n" % (inst, register))
     #out.write(" %s $%d, $%d\n" % (instruction, register, register))
     if ((inst == "mthi")or (inst == "multu1")):
      out.write("\tmfhi $%d\n" % (register))
     else:
      out.write("\tmflo $%d\n" % (register))
     out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
     out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
     out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
     offset += 4
     out.write("\t%s $%d\n" % (inst, register))
     #out.write(" %s $%d, $%d\n" % (instruction, register, register))
     if ((inst == "mthi")or (inst == "multu1")):
      out.write("\tmfhi $%d\n" % (register))
     else:
      out.write("\tmflo $%d\n" % (register))
     out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
     offset += 4
   if (register <= 0):
     register = 31
   else:
     register -= 1
 out.write("\n")

 data_f.close
 data_f2.close

##################################################################################

def reg_test_dat(out, result_address, pattern_address):

  reg_init_upward(out, registerFile_1, 1, pattern_address)
  reg_init_upward(out, registerFile_0, 0, pattern_address)
##########################################################################
#                          HILO Register test                            #
##########################################################################
  hi_upward_op(out,registerFile_0, 0, pattern_address, result_address)
  hi_downward_op(out,registerFile_1, 1, pattern_address, result_address)
  lo_upward_op(out,registerFile_0, 0, pattern_address, result_address)
  lo_downward_op(out,registerFile_1, 1, pattern_address, result_address)

  hi_upward_op(out,registerFile_1, 1, pattern_address, result_address)
  hi_downward_op(out,registerFile_0, 0, pattern_address, result_address)
  lo_upward_op(out,registerFile_1, 1, pattern_address, result_address)
  lo_downward_op(out,registerFile_0, 0, pattern_address, result_address)

  #store_load_upward(out,registerFile_0, 0, pattern_address, result_address)
  #store_load_downward(out,registerFile_1, 1, pattern_address, result_address)

##########################################################################
#                  User-defined Special Register test                    #
##########################################################################
def special_register(out):
  out.write(";........initialize all registers..............;\n")
  out.write(" reg_special:\n")
  register = 0
  data_f = open(registerFile_1,'r')
  line = data_f.readlines()

  for i in (line):
     bit_set1 = i[:16]
     bit_set2 = i[16:32]
     most_sig_bit   = int(bit_set1,2)
     least_sig_bit  = int(bit_set2,2)
     out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
     out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
     if (register >= 31):
       register = 0
     else:
       register += 1
  out.write("\n")
  data_f.close

  out.write(";........test special purpose registers........;\n")
  result_address = 1
  res_address = 1
  out.write("\tlui $%d, %d\n" % (result_address, 1))
  out.write("\tori $%d, $%d, %d\n\n" % (result_address, result_address, 2000))

  reg_upward_special(out,registerFile_1, registerFile_0, res_address)
  reg_upward_special_mirror(out,registerFile_0, registerFile_1, res_address)

  #out.write(";........test special purpose registers with HILO........;\n")
  #hi_lo_upward_special(out,"mthi",registerFile_1, registerFile_0, result_address)
  #hi_lo_upward_special(out,"mtlo", registerFile_1, registerFile_0, result_address)
  #hi_lo_upward_special(out,"mthi",registerFile_0, registerFile_1, result_address)
  #hi_lo_upward_special(out,"mtlo", registerFile_0, registerFile_1, result_address)


def special_register_datapart(out):
  out.write(";........initialize all registers..............;\n")
  out.write(" reg_special:\n")
  out.write(";........test special purpose registers........;\n")
  result_address = 1
  res_address = 1
  out.write("\tlui $%d, %d\n" % (result_address, 1))
  out.write("\tori $%d, $%d, %d\n\n" % (result_address, result_address, 2000))

  reg_upward_special_datapart(out,registerFile_1, registerFile_0, res_address)
  reg_upward_special_mirror_datapart(out,registerFile_0, registerFile_1, res_address)

##########################################################################
#                          HILO Register test                            #
##########################################################################
def hi_upward_op(out,data, number, pattern_address, result_address):
 out.write(" hi_upward_"+str(number)+":\n")
 register = 0
 #offset = 0
 global offset
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if not ((register == 31) or (register == 29)):
      out.write("\tmthi $%d\n" % ( register))
      out.write("\tmfhi $%d\n" % (register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      offset += 4
    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\tjr $31\n\n")
 data_f.close


def hi_downward_op(out,data, number, pattern_address, result_address):
 out.write(" hi_downward_"+str(number)+":\n")
 register = 0
 global offset
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if not ((register == 31) or (register == 29)):
      out.write("\tmthi $%d\n" % ( register))
      out.write("\tmfhi $%d\n" % (register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      out.write("\tmthi $%d\n" % (register))
      out.write("\tmfhi $%d\n" % (register))
      offset += 4
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      offset += 4
    if (register <= 0):
      register = 31
    else:
      register -= 1
 out.write("\tjr $31\n\n")
 data_f.close


def lo_upward_op(out,data, number, pattern_address, result_address):
 out.write(" lo_upward_"+str(number)+":\n")
 register = 0
 global offset
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if not ((register == 31) or (register == 29)):
      out.write("\tmtlo $%d\n" % (register))
      out.write("\tmflo $%d\n" % (register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      offset += 4
    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\tjr $31\n\n")
 data_f.close


def lo_downward_op(out,data, number, pattern_address, result_address):
 out.write( "lo_downward_"+str(number)+":\n")
 register = 0
 global offset
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if not ((register == 31) or (register == 29)):
      out.write("\tmtlo $%d\n" % (register))
      out.write("\tmflo $%d\n" % (register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      out.write("\tmtlo $%d\n" % (register))
      out.write("\tmflo $%d\n" % (register))
      offset += 4
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      offset += 4
    if (register <= 0):
      register = 31
    else:
      register -= 1
 out.write("\tjr $31\n\n")
 data_f.close

 ############################################################################
def store_load_upward(out,data, number, pattern_address, result_address):
 out.write(" store_load_upward_"+str(number)+":\n")
 register = 0
 #offset = 0
 global offset
 data_f = open(data,'r')
 line = data_f.readlines()

 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if not ((register == 31) or (register == 30)):
      out.write("\tand $%d, $%d, $%d\n" % (register, register, register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, result_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      offset += 4
    if (register >= 31):
      register = 0
    else:
      register += 1
 out.write("\tjr $31\n\n")
 data_f.close


def store_load_downward(out,data, number, pattern_address, result_address):
 data_f = open(data,'r')
 out.write(" store_load_downward_"+str(number)+":\n")
 register = 31
 global offset
 #offset = 0
 line = data_f.readlines()
 for i in (line):
    bit_set1 = i[:16]
    bit_set2 = i[16:32]
    most_sig_bit   = int(bit_set1,2)
    least_sig_bit  = int(bit_set2,2)

    if not ((register == 31) or (register == 30)):
      out.write("\tnor $%d, $%d, $%d\n" % (register, register, register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, pattern_address))
      out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
      out.write("\tori $%d, $%d, %d\n" % (register, register, least_sig_bit))
      offset += 4
      #if (number == 1):
      out.write("\tand $%d, $%d, $%d\n" % (register, register, register))
      #else:
      #    out.write(" nor $%d, $%d, $%d\n" % (register, register, register))
      out.write("\tsw $%d, %d($%s)\n" % (register, offset, pattern_address))
      offset += 4
    if (register <= 0):
      register = 31
    else:
      register -= 1
 out.write("\tjr $31\n\n")
 data_f.close

##########################################################################
#def reg_test(out, result_address, pattern_address):
#  out.write("jal reset_offsets\n")
#  out.write("register_operation:\n")
#  out.write(" jal init_upward_1\n")
#  out.write(" jal store_load_upward_0\n")
#  out.write(" jal store_load_downward_1\n\n")
#
#  out.write("jal reset_offsets\n")
#  out.write("register_operation_2:\n")
#  out.write(" jal init_upward_0\n")
#  out.write(" jal store_load_upward_1\n")
#  out.write(" jal store_load_downward_0\n")
#  out.write("\n")

def hilo(out, result_address, pattern_address):
  ######################################
  out.write("jal reset_offsets\n")
  out.write("jal reset_hi_lo\n")
  out.write("hilo_register_operation:\n")
  out.write(" jal init_upward_1\n")
  out.write(" jal hi_upward_0\n")
  out.write(" jal hi_downward_1\n")
  out.write(" jal lo_upward_0\n")
  out.write(" jal lo_downward_1\n")

  out.write(" jal init_upward_0\n")
  out.write(" jal hi_upward_1\n")
  out.write(" jal hi_downward_0\n")
  out.write(" jal lo_upward_1\n")
  out.write(" jal lo_downward_0\n")
  out.write("\n")

  #out.write("jal reset_offsets\n")     #add later
  #out.write("register_operation:\n")
  #out.write(" jal init_upward_1\n")
  #out.write(" jal store_load_upward_0\n")
  #out.write(" jal store_load_downward_1\n\n")


def cop_register_new(out,result_address):
  global offset
  out.write("\tlui $%d, %d\n" % (1, 65535))
  out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))
  for i in range(1,32):
    if not ((i == 12)):
      out.write("\tmtc0 $%d, $%d\n" % (1, i))
  out.write("\n")
  for i in range(0,31):
    #if not ((i == 12)):
    out.write("\tmfc0 $%d, $%d\n" % (i, i+1))
    out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
    out.write("\tsw $%d, %d($%s)\n" % (i, offset, result_address))
    offset +=4
    out.write("\tmtc0 $%d, $%d\n" % (0, i+1))
  out.write("\n")
  for i in range(0,31):
    #if not ((i == 12)):
    out.write("\tmfc0 $%d, $%d\n" % (i, i+1))
    out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
    out.write("\tsw $%d, %d($%s)\n" % (i, offset, result_address))
    offset +=4
    out.write("\tmtc0 $%d, $%d\n" % (1, i+1))
    out.write("\tmfc0 $%d, $%d\n" % (i, i+1))
    out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
    out.write("\tsw $%d, %d($%s)\n" % (i, offset, result_address))
    offset +=4


  out.write("\tlui $%d, %d\n" % (1, 65535))
  out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))
  for i in range(1,32):
    if not ((i == 12)):
      out.write("\tmtc0 $%d, $%d\n" % (0, i))
  out.write("\n")
  for i in range(0,31):
    #if not ((i == 12)):
    out.write("\tmfc0 $%d, $%d\n" % (i, i+1))
    out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
    out.write("\tsw $%d, %d($%s)\n" % (i, offset, result_address))
    offset +=4
    out.write("\tmtc0 $%d, $%d\n" % (1, i+1))
  out.write("\n")
  for i in range(0,31):
    #if not ((i == 12)):
    out.write("\tmfc0 $%d, $%d\n" % (i, i+1))
    out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
    out.write("\tsw $%d, %d($%s)\n" % (i, offset, result_address))
    offset +=4
    out.write("\tmtc0 $%d, $%d\n" % (0, i+1))
    out.write("\tmfc0 $%d, $%d\n" % (i, i+1))
    out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
    out.write("\tsw $%d, %d($%s)\n" % (i, offset, result_address))
    offset +=4


def cop_register(out,result_address):
  out.write("jal reset_offsets\n")
  out.write("jal init_cp\n")
  out.write("cop0_register:\n")
  offset = 0
  out.write("\tlui $%d, %d\n" % (1, 65535))
  out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))
  out.write("\tmtc0 $%d, $%d\n" % (1, 8))
  out.write("\tmtc0 $%d, $%d\n" % (1, 12))
  out.write("\tmtc0 $%d, $%d\n" % (1, 13))
  out.write("\tmtc0 $%d, $%d\n" % (1, 14))
  out.write("\tmtc0 $%d, $%d\n" % (1, 15))

  out.write("\tmfc0 $%d, $%d\n" % (2, 8))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (2, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 8))

  out.write("\tmfc0 $%d, $%d\n" % (2, 12))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (2, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 12))
  out.write("\tmfc0 $%d, $%d\n" % (3, 13))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (3, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 13))
  out.write("\tmfc0 $%d, $%d\n" % (4, 14))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (4, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 14))
  out.write("\tmfc0 $%d, $%d\n" % (5, 15))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (5, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 15))

  out.write("\tmfc0 $%d, $%d\n" % (6, 8))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (6, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 8))
  out.write("\tmfc0 $%d, $%d\n" % (7, 8))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (7, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (6, 12))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (6, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 12))
  out.write("\tmfc0 $%d, $%d\n" % (7, 12))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (7, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (8, 13))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (8, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 13))
  out.write("\tmfc0 $%d, $%d\n" % (9, 13))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (9, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (10, 14))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (10, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 14))
  out.write("\tmfc0 $%d, $%d\n" % (11, 14))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (11, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (16, 15))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (16, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 15))
  out.write("\tmfc0 $%d, $%d\n" % (17, 15))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n\n" % (17, offset, result_address))
  offset +=4

  out.write(";........coprocessor mirror........;\n")
  out.write("\tlui $%d, %d\n" % (1, 65535))
  out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))

  out.write("\tmtc0 $%d, $%d\n" % (0, 8))
  out.write("\tmtc0 $%d, $%d\n" % (0, 12))
  out.write("\tmtc0 $%d, $%d\n" % (0, 13))
  out.write("\tmtc0 $%d, $%d\n" % (0, 14))
  out.write("\tmtc0 $%d, $%d\n" % (0, 15))

  out.write("\tmfc0 $%d, $%d\n" % (2, 8))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (2, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 8))

  out.write("\tmfc0 $%d, $%d\n" % (2, 12))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (2, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 12))
  out.write("\tmfc0 $%d, $%d\n" % (3, 13))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (3, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 13))
  out.write("\tmfc0 $%d, $%d\n" % (4, 14))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (4, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 14))
  out.write("\tmfc0 $%d, $%d\n" % (5, 15))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (5, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (1, 15))

  out.write("\tmfc0 $%d, $%d\n" % (6, 8))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (6, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 8))
  out.write("\tmfc0 $%d, $%d\n" % (7, 8))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (7, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (6, 12))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (6, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 12))
  out.write("\tmfc0 $%d, $%d\n" % (7, 12))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (7, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (8, 13))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (8, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 13))
  out.write("\tmfc0 $%d, $%d\n" % (9, 13))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (9, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (10, 14))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (10, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 14))
  out.write("\tmfc0 $%d, $%d\n" % (11, 14))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (11, offset, result_address))
  offset +=4

  out.write("\tmfc0 $%d, $%d\n" % (16, 15))
  out.write("\tsw $%d, %d($%s)\n" % (16, offset, result_address))
  offset +=4
  out.write("\tmtc0 $%d, $%d\n" % (0, 15))
  out.write("\tmfc0 $%d, $%d\n" % (17, 15))
  out.write("\tsw $%d, %d($%s)\n\n" % (17, offset, result_address))
