# Copyright (C) 2020 Oyeniran Adeboye Stephen, Osidibo

def pseudo_template(inputFile, out, instruct, result_register):
  f = open(inputFile, 'r')  # input file

  instruction = instruct

  out.write("jal reset_offsets\n")
  if(instruction[0:2] == "mf" or instruction[0:2] == "mt"):
      out.write("jal reset_hi_lo\n")
  if(instruction[0:] == "add" or instruction[0:] == "sub"):
      out.write("jal init_cp\n")
  out.write("operation_"+instruction+"_psuedo:\n")
  offset = 0
  register = 2
  outline = []

  line = f.readlines()

  def load_data(i, register):
  # selection by 16 bits
      bit_set1 = i[:16]
      bit_set2 = i[16:32]
      bit_set3 = i[32:48]
      bit_set4 = i[48:68]
      for x in range(2):
         if (x == 0):
             most_sig_bit = int(bit_set1, 2)
             least_sig_bit = int(bit_set2, 2)
         else:
             most_sig_bit = int(bit_set3, 2)
             least_sig_bit = int(bit_set4, 2)
         out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
         out.write("\tori $%d, $%d, %d\n" %
                   (register, register, least_sig_bit))
         if (register >= 3):
             register = 2
         else:
             register += 1

  def load_data_immediate(i, register, opcode):
      bit_set1 = i[:16]
      bit_set2 = i[16:32]
      bit_set3 = i[32:48]
      bit_set4 = i[48:68]
      for x in range(2):
         if (x == 0):
             most_sig_bit = int(bit_set1, 2)
             least_sig_bit = int(bit_set2, 2)
             out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
             out.write("\tori $%d, $%d, %d\n" %
                       (register, register, least_sig_bit))
         else:
             most_sig_bit = int(bit_set3, 2)
             least_sig_bit = int(bit_set4, 2)
             out.write("\t%s $%s, $%d, %d\n" %(opcode, result_register, register+1, least_sig_bit))
         if (register >= 2):
             register = 1
         else:
             register += 1

  def load_data_shift(i, register, opcode):
      bit_set1 = i[:16]
      bit_set2 = i[16:32]
      bit_set3 = i[32:48]
      bit_set4 = i[48:68]
      shift_amount = 5
      for x in range(2):
         if (x == 0):
             most_sig_bit = int(bit_set1, 2)
             least_sig_bit = int(bit_set2, 2)
         else:
          if(opcode == "lui"):
              out.write("\tlui $%d, %d\n" % (register+1, most_sig_bit))
          elif(str(opcode[0:2]) == "mf" or str(opcode[0:2]) == "mt"):
              out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
              out.write("\tori $%d, $%d, %d\n" %
                        (register, register, least_sig_bit))
              out.write("\t%s $%d\n" % (opcode, register))
          else:
              most_sig_bit = int(bit_set3, 2)
              least_sig_bit = int(bit_set4, 2)
              out.write("\tlui $%d, %d\n" % (register, most_sig_bit))
              out.write("\tori $%d, $%d, %d\n" %
                        (register, register, least_sig_bit))
              out.write("\t%s $%s, $%d, %d\n" %
                        (opcode, result_register, register, shift_amount))
         if (register >= 2):
             register = 2
         else:
             register += 1

  def alu_shifts(file_name, offset, opcode):
      for i in (line):
          load_data_shift(i, register, opcode)
          out.write("\tsw $%s, %d($29)\n" % (result_register, offset))
          out.write("\tjal increment\n")
          # offset += 4

  def alu_immediate(file_name, offset, opcode):
      for i in (line):
          load_data_immediate(i, register, opcode)
          out.write("\tsw $%s, %d($29)\n" % (result_register, offset))
          out.write("\tjal increment\n")
          # offset += 4

  def alu_op(file_name, offset):
      for i in (line):
          load_data(i, register)
          out.write("\t%s $%s, $%d, $%d\n" %
                    (instruction, result_register, register, register+1))
          out.write("\tsw $%s, %d($29)\n" % (result_register, offset))
          out.write("\tjal increment\n")
          # offset += 4

  def mult_op(file_name, offset):
      for i in (line):
          load_data(i, register)
          out.write("\t%s $%d, $%d\n" % (instruction, register, register+1))
          out.write("\tmflo $%s\n" % (result_register))
          out.write("\tsw $%s, %d($29)\n" % (result_register, offset))
          out.write("\tmfhi $%s\n" % (result_register))
          out.write("\tsw $%s, %d($29)\n" % (result_register, offset))
          out.write("\tjal increment\n")
          # offset += 4

  def hi_lo(file_name, offset, opcode):
      for i in (line):
          load_data_shift(i, register, opcode)
          if(opcode[2:4] == "hi"):
              out.write("\tmfhi $%d\n" % (register+2))
          else:
          	out.write("\tmflo $%d\n" % (register+2))
          	out.write("\tsw $%d, %d($29)\n" % (register+2, offset))
          	out.write("\tjal increment\n")
         	 # offset += 4
  

  if ((instruction =="mult") or (instruction =="multu")):
      mult_op(f, offset)
  elif((instruction =="addiu") or (instruction =="addi") or (instruction =="andi")or (instruction =="ori")or (instruction =="xori") or (instruction =="sltiu")or (instruction =="slti")): 
      alu_immediate(f, offset, instruction)
  elif((instruction =="sll") or (instruction =="sra")or (instruction =="srl")or (instruction =="lui")):
      alu_shifts(f,offset,instruction)
  elif((instruction == "mtlo") or (instruction =="mthi")):
      hi_lo(f,offset,instruction)
  else:
      alu_op(f,offset)

  f.close()

def make_pseudo_template(para, outputFile, result_register):
  Ins = open(para,'r')
  data_lines = []
  firstPass = True

  for line in Ins:
    if "=" not in line:
      try:
        catergory = line[0:2]
        line = line.rstrip()
        instru = line[2:]
        instr = str.strip(instru)
        instruction = instr[0:]
        if (catergory == 'p_'):
          if (instruction == 'addu' or instruction == 'add' or instruction == 'addi' or instruction == 'addiu'):
            inputFile = '../input/pseudo_input/all.txt'
            pseudo_template(inputFile, outputFile, instruction, result_register)
            outputFile.write("\n")
          elif(instruction == 'subu'or instruction == 'sub'):
            inputFile = '../input/pseudo_input/all.txt'
            pseudo_template(inputFile, outputFile, instruction, result_register)
            outputFile.write("\n")     
          elif(instruction == 'or' or instruction == 'xor' or instruction == 'nor' or instruction == 'and' or instruction == 'andi' or instruction == 'ori' or instruction == 'xori'):
            inputFile = '../input/pseudo_input/all.txt'
            pseudo_template(inputFile, outputFile, instruction, result_register)
            outputFile.write("\n")    
          elif(instruction == 'sll' or instruction == 'srl' or instruction == 'sra' or instruction == 'srav' or instruction == 'slt' or instruction == 'sltu' or instruction == 'slti' or instruction == 'sltiu'):
            inputFile = '../input/pseudo_input/all.txt'
            pseudo_template(inputFile, outputFile, instruction, result_register)
            outputFile.write("\n") 
          elif(instruction == 'mult' or instruction == 'multu'):
            inputFile = '../input/pseudo_input/mult.txt'
            pseudo_template(inputFile, outputFile, instruction, result_register)
            outputFile.write("\n")     
      except IndexError:
        firstPass = False
    else:
      do='nothing'

  Ins.close()

