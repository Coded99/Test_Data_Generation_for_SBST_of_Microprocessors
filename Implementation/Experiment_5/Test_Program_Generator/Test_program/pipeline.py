# Copyright (C) 2019 Oyeniran Adeboye Stephen
import os
offset = 0
mem_loc = 0

##########################################################################
#                             Pipeline                                   #
##########################################################################
def init_alu(out, number):
  if (number == 0):
    out.write("\tlui $%d, %d\n" % (1, 0))
    out.write("\tori $%d, $%d, %d\n" % (1, 1, 0))
    out.write("\tlui $%d, %d\n" % (31, 65535))
    out.write("\tori $%d, $%d, %d\n" % (31, 31, 65535))
    out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))   ##NOP
    out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0)) 
   
  elif (number == 1):
    out.write("\tlui $%d, %d\n" % (1, 65535))
    out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))
    out.write("\tlui $%d, %d\n" % (31, 0))
    out.write("\tori $%d, $%d, %d\n" % (31, 31, 0))
    out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0)) 
    out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0)) 

def init_alu_2(out, number):
  if (number == 0):
    out.write("\tlui $%d, %d\n" % (1, 0))
    out.write("\tori $%d, $%d, %d\n" % (1, 1, 0))
    out.write("\tlui $%d, %d\n" % (31, 65535))
    out.write("\tori $%d, $%d, %d\n" % (31, 31, 65535))
    out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0)) 
   
  elif (number == 1):
    out.write("\tlui $%d, %d\n" % (1, 65535))
    out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))
    out.write("\tlui $%d, %d\n" % (31, 0))
    out.write("\tori $%d, $%d, %d\n" % (31, 31, 0))
    out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
    
def init_load_alu(out, number):
  if (number == 0):
    out.write("\tlui $%d, %d\n" % (1, 0))
    out.write("\tori $%d, $%d, %d\n" % (1, 1, 0))
    out.write("\tlui $%d, %d\n" % (31, 65535))
    out.write("\tori $%d, $%d, %d\n" % (31, 31, 65535))

  elif (number == 1):
    out.write("\tlui $%d, %d\n" % (1, 65535))
    out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))
    out.write("\tlui $%d, %d\n" % (31, 65535))
    out.write("\tori $%d, $%d, %d\n" % (31, 31, 65535))

    
def test_alu_alu(out, fixed_register, test_register, result_address):
  global offset
  init_alu(out, 0)
  out.write("\tand $%d, $%d, $%d\n" % (fixed_register, test_register, test_register))
  out.write("\tand $%d, $%d, $%d\n" % (2, fixed_register, test_register))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  #out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  #out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4
  
  init_alu(out, 1)
  out.write("\tand $%d, $%d, $%d\n" % (fixed_register, test_register, test_register))
  out.write("\tand $%d, $%d, $%d\n" % (2, fixed_register, test_register))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  #out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  #out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4

  init_alu(out, 0)
  out.write("\tand $%d, $%d, $%d\n" % (fixed_register, test_register, test_register))
  out.write("\tand $%d, $%d, $%d\n" % (2, test_register, fixed_register))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  #out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  #out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4
  
  init_alu(out, 1)
  out.write("\tand $%d, $%d, $%d\n" % (fixed_register, test_register, test_register))
  out.write("\tand $%d, $%d, $%d\n" % (2, test_register, fixed_register))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  #out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  #out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4
  
  init_alu_2(out, 0)
  out.write("\tand $%d, $%d, $%d\n" % (fixed_register, test_register, test_register))
  out.write("\tand $%d, $%d, $%d\n" % (fixed_register, fixed_register, test_register))
  out.write("\tand $%d, $%d, $%d\n" % (2, fixed_register, test_register))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  #out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  #out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4

  init_alu_2(out, 1)
  out.write("\tand $%d, $%d, $%d\n" % (fixed_register, test_register, test_register))
  out.write("\tand $%d, $%d, $%d\n" % (fixed_register, fixed_register, test_register))
  out.write("\tand $%d, $%d, $%d\n" % (2, fixed_register, test_register))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  #out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  #out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4

def pipeline_test(out, result_address, result_register):
 
  global offset
  out.write("pipeline_operation:\n")
  out.write(";.............pipeline test_alu.............;\n")
 
  test_alu_alu(out, 1, 31, result_address)
  test_alu_alu(out, 31, 1, result_address)
  
  out.write(";.............pipeline test_load_alu.............;\n")
  out.write("\tlui $%d, %d\n" % (1, 65535))
  out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))
  out.write("\tsw $%d, %d($%s)\n" % (1, offset, result_address))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  init_load_alu(out, 0)
  out.write("\tlw $%d, %d($%s)\n" % (1, offset, result_address))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tand $%d, $%d, $%d\n" % (2, 1, 31))
  offset +=4
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4
  
  out.write("\tlui $%d, %d\n" % (1, 0))
  out.write("\tori $%d, $%d, %d\n" % (1, 1, 0))
  out.write("\tsw $%d, %d($%s)\n" % (1, offset, result_address))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  init_load_alu(out, 1)
  out.write("\tlw $%d, %d($%s)\n" % (1, offset, result_address))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tand $%d, $%d, $%d\n" % (2, 1, 31))
  offset +=4
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4
  
  out.write("\tlui $%d, %d\n" % (1, 65535))
  out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))
  out.write("\tsw $%d, %d($%s)\n" % (1, offset, result_address))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  init_load_alu(out, 0)
  out.write("\tlw $%d, %d($%s)\n" % (1, offset, result_address))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tand $%d, $%d, $%d\n" % (2, 31, 1))
  offset +=4
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4
  
  out.write("\tlui $%d, %d\n" % (1, 0))
  out.write("\tori $%d, $%d, %d\n" % (1, 1, 0))
  out.write("\tsw $%d, %d($%s)\n" % (1, offset, result_address))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  init_load_alu(out, 1)
  out.write("\tlw $%d, %d($%s)\n" % (1, offset, result_address))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tand $%d, $%d, $%d\n" % (2, 31, 1))
  offset +=4
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4

  out.write(";.............pipeline test_store_load_data.............;\n")
  out.write("\tlui $%d, %d\n" % (1, 0))
  out.write("\tori $%d, $%d, %d\n" % (1, 1, 0))
  out.write("\tlui $%d, %d\n" % (31, 65535))
  out.write("\tori $%d, $%d, %d\n" % (31, 31, 65535))
  out.write("\tsw $%d, %d($%s)\n" % (1, offset, result_address))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n" % (31, offset, result_address))
  #out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tlw $%d, %d($%s)\n" % (31, offset, result_address))
  offset +=4
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tsw $%d, %d($%s)\n\n" % (31, offset, result_address))
  offset +=4


  out.write(";.............pipeline test_load_store_data.............;\n")
  out.write("\tlui $%d, %d\n" % (1, 65535))
  out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))
  out.write("\tsw $%d, %d($%s)\n" % (1, offset, result_address))
  out.write("\tlui $%d, %d\n" % (1, 0))
  out.write("\tori $%d, $%d, %d\n" % (1, 1, 0))
  out.write("\tlw $%d, %d($%s)\n" % (1, offset, result_address))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  offset +=4
  out.write("\tsw $%d, %d($%s)\n\n" % (1, offset, result_address))
  offset +=4


  out.write(";.............pipeline control hazard.............;\n")
  out.write("\tlui $%d, %d\n" % (1, 0))
  out.write("\tori $%d, $%d, %d\n" % (1, 1, 0))
  out.write("\tlui $%d, %d\n" % (30, 65535))
  out.write("\tori $%d, $%d, %d\n" % (30, 30, 65535))
  out.write("\tand $%s, $%d, $%d\n" % (result_register, 1, 30))
  out.write("\tbne $%d, $%d, %s\n" % (30, 1, "continue"))
  #out.write("\taddu $%s, $%d, $%d\n" % (result_register, 1, 30))
  #out.write("\taddu $%s, $%d, $%d\n" % (result_register, 1, 30))
  #out.write("\taddu $%s, $%d, $%d\n" % (result_register, 1, 30))
  out.write(" continue:\n")
  out.write(" sw $%s, %d($%s)\n\n" % (result_register, offset, result_address))
  offset +=4


  out.write(";.............pipeline addressing hazard store.............;\n")
  #out.write("\tlui $%d, %d\n" % (1, 65535))                   # investigate this to see if correct or needed
  #out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))
  #out.write("\tsw $%d, %d($%d)\n" % (1, offset, 0))
  #out.write("\tsw $%d, %d($%d)\n" % (0, offset, 1))
  #out.write("\tlui $%d, %d\n" % (1, 0))
  #out.write("\tori $%d, $%d, %d\n" % (1, 1, 0))
  #out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  #out.write("\tlui $%d, %d\n" % (1, 65535))
  #out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))
  #out.write("\tlw $%d, %d($%d)\n" % (31, offset, 1))
  #out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  #out.write("\tsw $%d, %d($%d)\n\n" % (31, offset, 29))
  #offset +=4


  #out.write("\tlui $%d, %d\n" % (1, 65535))
  #out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))
  #out.write("\tsw $%d, %d($%d)\n" % (1, offset, 0))
  #out.write("\tsw $%d, %d($%d)\n" % (0, offset, 1))
  #out.write("\tlui $%d, %d\n" % (31, 0))
  #out.write("\tori $%d, $%d, %d\n" % (31, 31, 0))
  #out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  #out.write("\tlui $%d, %d\n" % (1, 0))
  #out.write("\tori $%d, $%d, %d\n" % (1, 1, 0))
  #out.write("\tlui $%d, %d\n" % (31, 65535))
  #out.write("\tori $%d, $%d, %d\n" % (31, 31, 65535))
  #out.write("\tsw $%d, %d($%d)\n\n" % (1, offset, 31))
  #offset +=4

  #out.write("\tlui $%d, %d\n" % (1, 1))        # original version 
  #out.write("\tori $%d, $%d, %d\n" % (1, 1, 5000))
  #out.write("\tsw $%d, %d($%d)\n" % (1, offset, 0))
  #out.write("\tsw $%d, %d($%d)\n" % (0, offset, 1))
  #out.write("\tlui $%d, %d\n" % (31, 65535))
  #out.write("\tori $%d, $%d, %d\n" % (31, 31, 65535))
  #out.write("\tlw $%d, %d($%d)\n" % (31, offset, 1))
  #out.write("\tsw $%d, %d($%d)\n\n" % (31, offset, 31))
  #offset +=4

  out.write("\tlui $%d, %d\n" % (1, 0))         #modiied version
  out.write("\tori $%d, $%d, %d\n" % (1, 1, 0))
  out.write("\taddu $%d, $%d, $%d\n" % (1, 1, 29))
  out.write("\tsw $%d, %d($%d)\n" % (1, offset, 1))
  out.write("\tlui $%d, %d\n" % (31, 65535))
  out.write("\tori $%d, $%d, %d\n" % (31, 31, 65535))
  out.write("\tlw $%d, %d($%d)\n" % (31, offset, 1))
  out.write("\tsw $%d, %d($%d)\n\n" % (31, offset, 31))
  offset +=4

  out.write(";.............comparator test.............;\n")
  comparator(0, 31, out, result_address)
  comparator(30, 31, out, result_address)

  comparator_b(0, 31, out, result_address)
  comparator_b(30, 31, out, result_address)

  out.write(";.............comparator contd (changing result address).............;\n")
  result_address = 20
  out.write("\tlui $%d, %d\n" % (result_address, 0))
  out.write("\tori $%d, $%d, %d\n" % (result_address, result_address, 0))
  out.write("\taddu $%d, $%d, $%d %s\n\n" % (result_address, result_address, 29, ";calculate next memory address"))

  comparator_2(31,1, out, result_address)
  comparator_2(30,1, out, result_address)
  comparator_2(29,1, out, result_address)
  comparator_2(27,1, out, result_address)
  comparator_2(23,1, out, result_address)
  comparator_2(15,1, out, result_address)

  #comparator_2new(31,1, out, result_address)
  comparator_2inverse(30,1, out, result_address)
  comparator_2inverse(29,1, out, result_address)
  comparator_2inverse(27,1, out, result_address)
  comparator_2inverse(23,1, out, result_address)
  comparator_2inverse(15,1, out, result_address)

  comparator_2b(31,1, out, result_address)
  comparator_2b(30,1, out, result_address)
  comparator_2b(29,1, out, result_address)
  comparator_2b(27,1, out, result_address)
  comparator_2b(23,1, out, result_address)
  comparator_2b(15,1, out, result_address)

  #comparator_2bnew(31,1, out, result_address)
  comparator_2binverse(30,1, out, result_address)
  comparator_2binverse(29,1, out, result_address)
  comparator_2binverse(27,1, out, result_address)
  comparator_2binverse(23,1, out, result_address)
  comparator_2binverse(15,1, out, result_address)


  out.write(";.............comparator load_alu.............;\n")
  global offset 
  mem_loc = offset -4

  comparator_load_alu(0, 1, out, result_address, mem_loc)
  comparator_load_alu(30, 1, out, result_address, mem_loc)

  comparator_load_alu_b(0, 1, out, result_address, mem_loc)
  comparator_load_alu_b(30, 1, out, result_address, mem_loc)

  comparator_load_alu2(31, 1, out, result_address, mem_loc)
  comparator_load_alu2(30, 1, out, result_address, mem_loc)
  comparator_load_alu2(29, 1, out, result_address, mem_loc)
  comparator_load_alu2(27, 1, out, result_address, mem_loc)
  comparator_load_alu2(23, 1, out, result_address, mem_loc)
  comparator_load_alu2(15, 1, out, result_address, mem_loc)

  #comparator_load_alu2new(31, 1, out, result_address, mem_loc)
  comparator_load_alu2new(30, 1, out, result_address, mem_loc)
  comparator_load_alu2new(29, 1, out, result_address, mem_loc)
  comparator_load_alu2new(27, 1, out, result_address, mem_loc)
  comparator_load_alu2new(23, 1, out, result_address, mem_loc)
  comparator_load_alu2new(15, 1, out, result_address, mem_loc)

  comparator_load_alu2b(31, 1, out, result_address, mem_loc)
  comparator_load_alu2b(30, 1, out, result_address, mem_loc)
  comparator_load_alu2b(29, 1, out, result_address, mem_loc)
  comparator_load_alu2b(27, 1, out, result_address, mem_loc)
  comparator_load_alu2b(23, 1, out, result_address, mem_loc)
  comparator_load_alu2b(15, 1, out, result_address, mem_loc)

  #comparator_load_alu2bnew(31, 1, out, result_address, mem_loc)
  comparator_load_alu2bnew(30, 1, out, result_address, mem_loc)
  comparator_load_alu2bnew(29, 1, out, result_address, mem_loc)
  comparator_load_alu2bnew(27, 1, out, result_address, mem_loc)
  comparator_load_alu2bnew(23, 1, out, result_address, mem_loc)
  comparator_load_alu2bnew(15, 1, out, result_address, mem_loc)

  out.write(";.............comparator hazard.............;\n")
  comparator_load_alu_hazard(30, 1, out, result_address, mem_loc)
  comparator_load_alu_hazard(29, 1, out, result_address, mem_loc)
  comparator_load_alu_hazard(27, 1, out, result_address, mem_loc)
  comparator_load_alu_hazard(23, 1, out, result_address, mem_loc)
  comparator_load_alu_hazard(15, 1, out, result_address, mem_loc)

  comparator_load_alu_hazardnew(30, 1, out, result_address, mem_loc)
  comparator_load_alu_hazardnew(29, 1, out, result_address, mem_loc)
  comparator_load_alu_hazardnew(27, 1, out, result_address, mem_loc)
  comparator_load_alu_hazardnew(23, 1, out, result_address, mem_loc)
  comparator_load_alu_hazardnew(15, 1, out, result_address, mem_loc)


def comparator(test_register, fixed, out, result_address):
  global offset
  out.write("\tlui $%d, %d\n" % (test_register, 0))
  out.write("\tori $%d, $%d, %d\n" % (test_register, test_register, 0))
  out.write("\tlui $%d, %d\n" % (fixed, 65535))
  out.write("\tori $%d, $%d, %d\n" % (fixed, fixed, 65535))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tand $%d, $%d, $%d\n" % (test_register, fixed, fixed))
  out.write("\tand $%d, $%d, $%d\n" % (2, test_register, fixed))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4

def comparator_b(test_register, fixed, out, result_address):
  global offset
  out.write("\tlui $%d, %d\n" % (test_register, 0))
  out.write("\tori $%d, $%d, %d\n" % (test_register, test_register, 0))
  out.write("\tlui $%d, %d\n" % (fixed, 65535))
  out.write("\tori $%d, $%d, %d\n" % (fixed, fixed, 65535))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tand $%d, $%d, $%d\n" % (test_register, fixed, fixed))
  out.write("\tand $%d, $%d, $%d\n" % (2, fixed, test_register))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4

def comparator_2(test_register, fixed, out, result_address):
  global offset
  out.write("\tlui $%d, %d\n" % (fixed, 65535))
  out.write("\tori $%d, $%d, %d\n" % (fixed, fixed, 65535))
  out.write("\tlui $%d, %d\n" % (test_register, 0))
  out.write("\tori $%d, $%d, %d\n" % (test_register, test_register, 0))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tand $%d, $%d, $%d\n" % (31, fixed, fixed))
  out.write("\tand $%d, $%d, $%d\n" % (2, test_register, fixed))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4

def comparator_2inverse(test_register, fixed, out, result_address):
  global offset
  out.write("\tlui $%d, %d\n" % (fixed, 65535))
  out.write("\tori $%d, $%d, %d\n" % (fixed, fixed, 65535))
  out.write("\tlui $%d, %d\n" % (test_register, 0))
  out.write("\tori $%d, $%d, %d\n" % (test_register, test_register, 0))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tand $%d, $%d, $%d\n" % (test_register, fixed, fixed))
  out.write("\tand $%d, $%d, $%d\n" % (2, 31, fixed))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4

def comparator_2b(test_register, fixed, out, result_address):
  global offset
  out.write("\tlui $%d, %d\n" % (fixed, 65535))
  out.write("\tori $%d, $%d, %d\n" % (fixed, fixed, 65535))
  out.write("\tlui $%d, %d\n" % (test_register, 0))
  out.write("\tori $%d, $%d, %d\n" % (test_register, test_register, 0))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  #out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tand $%d, $%d, $%d\n" % (31, fixed, fixed))
  out.write("\tand $%d, $%d, $%d\n" % (2, fixed, test_register))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4

def comparator_2binverse(test_register, fixed, out, result_address):
  global offset
  out.write("\tlui $%d, %d\n" % (fixed, 65535))
  out.write("\tori $%d, $%d, %d\n" % (fixed, fixed, 65535))
  out.write("\tlui $%d, %d\n" % (test_register, 0))
  out.write("\tori $%d, $%d, %d\n" % (test_register, test_register, 0))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  #out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tand $%d, $%d, $%d\n" % (test_register, fixed, fixed))
  out.write("\tand $%d, $%d, $%d\n" % (2, fixed, 31))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4


#def mem_comparator(out, result_address):
#  test_data = '0b1000000000000000'
#  out.write("\tlui $%d, %d\n" % (1, 65535))
#  out.write("\tori $%d, $%d, %d\n" % (1, 1, 65535))
#  out.write("\tlui $%d, %d\n" % (result_address, 0))
#  out.write("\tori $%d, $%d, %d\n" % (result_address, result_address, 65535))
#  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
#  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
# 
#  for x in range (0,16):
#    data = int(test_data,2) >> x
#    out.write("\tsw $%d, %d($%s)\n" % (1, data, result_address))
#  out.write("\n")


def comparator_load_alu(test_register, fixed, out, result_address, mem_loc):
  global offset
  out.write("\tlui $%d, %d\n" % (test_register, 0))
  out.write("\tori $%d, $%d, %d\n" % (test_register, test_register, 0))
  out.write("\tlui $%d, %d\n" % (fixed, 65535))
  out.write("\tori $%d, $%d, %d\n" % (fixed, fixed, 65535))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tlw $%d, %d($%s)\n" % (test_register, mem_loc, result_address))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tand $%d, $%d, $%d\n" % (2, test_register, fixed))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4
 

def comparator_load_alu_b(test_register, fixed, out, result_address, mem_loc):
  global offset
  out.write("\tlui $%d, %d\n" % (test_register, 0))
  out.write("\tori $%d, $%d, %d\n" % (test_register, test_register, 0))
  out.write("\tlui $%d, %d\n" % (fixed, 65535))
  out.write("\tori $%d, $%d, %d\n" % (fixed, fixed, 65535))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tlw $%d, %d($%s)\n" % (test_register, mem_loc, result_address))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tand $%d, $%d, $%d\n" % (2, fixed, test_register))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4


def comparator_load_alu2(test_register, fixed, out, result_address, mem_loc):
  global offset
  out.write("\tlui $%d, %d\n" % (fixed, 65535))
  out.write("\tori $%d, $%d, %d\n" % (fixed, fixed, 65535))
  out.write("\tlui $%d, %d\n" % (test_register, 0))
  out.write("\tori $%d, $%d, %d\n" % (test_register, test_register, 0))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tlw $%d, %d($%s)\n" % (31, mem_loc, result_address))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tand $%d, $%d, $%d\n" % (2, test_register, fixed))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4

def comparator_load_alu2new(test_register, fixed, out, result_address, mem_loc):
  global offset
  out.write("\tlui $%d, %d\n" % (fixed, 65535))
  out.write("\tori $%d, $%d, %d\n" % (fixed, fixed, 65535))
  out.write("\tlui $%d, %d\n" % (test_register, 0))
  out.write("\tori $%d, $%d, %d\n" % (test_register, test_register, 0))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tlw $%d, %d($%s)\n" % (test_register, mem_loc, result_address))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tand $%d, $%d, $%d\n" % (2, 31, fixed))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4

def comparator_load_alu2b(test_register, fixed, out, result_address, mem_loc):
  global offset
  out.write("\tlui $%d, %d\n" % (fixed, 65535))
  out.write("\tori $%d, $%d, %d\n" % (fixed, fixed, 65535))
  out.write("\tlui $%d, %d\n" % (test_register, 0))
  out.write("\tori $%d, $%d, %d\n" % (test_register, test_register, 0))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tlw $%d, %d($%s)\n" % (31, mem_loc, result_address))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tand $%d, $%d, $%d\n" % (2, fixed, test_register))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4

def comparator_load_alu2bnew(test_register, fixed, out, result_address, mem_loc):
  global offset
  out.write("\tlui $%d, %d\n" % (fixed, 65535))
  out.write("\tori $%d, $%d, %d\n" % (fixed, fixed, 65535))
  out.write("\tlui $%d, %d\n" % (test_register, 0))
  out.write("\tori $%d, $%d, %d\n" % (test_register, test_register, 0))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tlw $%d, %d($%s)\n" % (test_register, mem_loc, result_address))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tand $%d, $%d, $%d\n" % (2, fixed, 31))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4


def comparator_load_alu_hazard(test_register, fixed, out, result_address, mem_loc):
  global offset
  out.write("\tlui $%d, %d\n" % (fixed, 65535))
  out.write("\tori $%d, $%d, %d\n" % (fixed, fixed, 65535))
  out.write("\tlui $%d, %d\n" % (test_register, 0))
  out.write("\tori $%d, $%d, %d\n" % (test_register, test_register, 0))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tlw $%d, %d($%s)\n" % (31, mem_loc, result_address))
  out.write("\tand $%d, $%d, $%d\n" % (2, test_register, fixed))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4

def comparator_load_alu_hazardnew(test_register, fixed, out, result_address, mem_loc):
  global offset
  out.write("\tlui $%d, %d\n" % (fixed, 65535))
  out.write("\tori $%d, $%d, %d\n" % (fixed, fixed, 65535))
  out.write("\tlui $%d, %d\n" % (test_register, 0))
  out.write("\tori $%d, $%d, %d\n" % (test_register, test_register, 0))
  out.write("\tsll $%d, $%d, %d\n" % (0, 0, 0))
  out.write("\tlw $%d, %d($%s)\n" % (test_register, mem_loc, result_address))
  out.write("\tand $%d, $%d, $%d\n" % (2, 31, fixed))
  out.write("\tsw $%d, %d($%s)\n\n" % (2, offset, result_address))
  offset +=4

##########################################################################
#                             Branches                                   #
##########################################################################




##########################################################################
#                             syscall and break                          #
##########################################################################
def syscall(out):
  out.write(" jal init_cp\n")
  out.write(" j syscalls\n\n")
  out.write("syscalls:\n")
  out.write("\tsyscall\n\n")

def breaks(out):
  out.write(" jal init_cp\n")
  out.write("j breaks\n\n")
  out.write("breaks:\n")
  out.write("\tbreak\n")



