# Copyright (C) 2018 Oyeniran Adeboye Stephen, Olusiji
#This template generates OP2 instructions. The functionality is described as follow
#op2_func and variants generate test for OP2 instructions while hi_lo and variants generate
#test for HILO. The parameter file helps organize the test with the help of the HLDD

def op2_func(instruction, file, result_register,result_address,iterator,pattern_count, instr):
    file.write("\tjal load_patterns\n")
    file.write("\t%s $%s, $%d, $%d\n" % (instruction, result_register, 2, 3))
    file.write("\t%s $%s, $%d, $%d\n" % (instruction, str(int(result_register)+1), 2, 3)) #added
    #file.write("\tsw $%s, %d($%s)\n" % (result_register, 0, result_address))
    out.write("\tjal store\n") #added
    file.write("\tjal increment_offset\n")
    file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr))

def op2_mult_u_func(instruction, file, result_register,result_address,iterator,pattern_count, instr):
    file.write("\tjal load_patterns\n")
    file.write("\t%s $%d, $%d\n" % (instruction, 2, 3))
    file.write("\tsw $%s, %d($%s)\n" % (result_register, 0, result_address))
    file.write("\tjal increment_offset\n")
    file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr))

def op2_mthi_lo_func(instruction, file, result_register,result_address,iterator,pattern_count, instr):
    file.write("\tjal load_patterns\n")
    file.write("\t%s $%d\n" % (instruction, 2))
    file.write("\tsw $%s, %d($%s)\n" % (result_register, 0, result_address))
    file.write("\tjal increment_offset\n")
    file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr))

def op2_mfhi_lo_func(instruction, file, result_register,result_address,iterator,pattern_count, instr):
    file.write("\tjal load_patterns\n")
    file.write("\t%s $%s\n" % (instruction, result_register))
    file.write("\tsw $%s, %d($%s)\n" % (result_register, 0, result_address))
    file.write("\tjal increment_offset\n")
    file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr))

def op2_shift_amount_func(instruction, file, result_register,result_address,iterator,pattern_count, instr, shift_amount):
    file.write("\tjal load_patterns\n")
    file.write("\t%s $%s ,$%d, %s\n" % (instruction, result_register, 2, shift_amount ))
    file.write("\tsw $%s, %d($%s)\n" % (result_register, 0, result_address))
    file.write("\tjal increment_offset\n")
    file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr))

def hi_lo_func_func(instruction, file, result_register,result_address,iterator,pattern_count, instr):
    file.write("\tjal load_patterns\n")
    file.write("\t%s $%d, $%d\n" % (instruction, 15, 16))
    file.write("\t%s $%s\n" % ('mflo',result_register))
    file.write("\t%s $%d, $%d\n" % (instruction, 16, 15))
    file.write("\t%s $%s\n" % ('mflo',str(int(result_register)+1)))
    #file.write("\tsw $%s, %d($%s)\n" % (result_register, 0, result_address))
    file.write("\tjal store\n")
    file.write("\tjal increment_offset\n")
    file.write("\tbne $%s, $%s, operation_%s_lo\n\n" % (iterator, pattern_count, instr))

def hi_lo_func_func_a(instruction, file, result_register,result_address,iterator,pattern_count, instr):
    file.write("\tjal load_patterns\n")
    file.write("\t%s $%d, $%d\n" % (instruction, 15, 16))
    file.write("\t%s $%s\n" % ('mfhi',result_register))
    file.write("\t%s $%d, $%d\n" % (instruction, 16, 15))
    file.write("\t%s $%s\n" % ('mfhi',str(int(result_register)+1)))
    #file.write("\tsw $%s, %d($%s)\n" % (result_register, 0, result_address))
    file.write("\tjal store\n")
    file.write("\tjal increment_offset\n")
    file.write("\tbne $%s, $%s, operation_%s_hi\n\n" % (iterator, pattern_count, instr))

def hi_lo_mt_func(instruction, file, result_register,result_address,iterator,pattern_count, instr):
    if (instruction == 'mthi'):
        subInstruct = 'mfhi'
    else:
        subInstruct = 'mflo'
    file.write("\tjal load_patterns\n")
    file.write("\t%s $%d\n" % (instruction, 2))
    file.write("\t%s $%s\n" % (subInstruct ,result_register))
    file.write("\tsw $%s, %d($%s)\n" % (result_register, 0, result_address))
    file.write("\tjal increment_offset\n")
    file.write("\tbne $%s, $%s, operation_%s_hi_lo\n\n" % (iterator, pattern_count, instr))

def print_tags(file, instr):
	file.write("jal reset_offsets\n")
        file.write("jal init_cp\n")
	file.write("operation_"+instr+":\n")

def op2_template(para, out, result_register,result_address,iterator,pattern_count, shift_amount):
 f = open(para,'r')
 firstPass = True

 for line in f:
 	if "=" not in line:
 		try:
 			catergory = line[0:2]
 			line = line.rstrip()
 			instru = line[2:]
 			instr = str.strip(instru)
 			instruction = instr[0:]
 			if (catergory == 'a_'):
				if ((instr == 'mult') or (instr == 'multu')):
				 	print_tags(out, instr)
					op2_mult_u_func(instruction, out, result_register,result_address,iterator,pattern_count, instr)
				elif((instr == 'mthi') or (instr == 'mtlo')):
					print_tags(out, instr)
					op2_mthi_lo_func(instruction, out, result_register,result_address,iterator,pattern_count, instr)
				elif((instr == 'mfhi') or (instr == 'mflo')):
					out.write("jal reset_offsets\n")
					out.write("jal reset_hi_lo\n")
					out.write("operation_"+instr+":\n")
					op2_mfhi_lo_func(instruction, out, result_register,result_address,iterator,pattern_count, instr)
				elif((instr == 'sll') or (instr == 'sra') or (instr == 'srl')):
					print_tags(out, instr)
					op2_shift_amount_func(instruction, out, result_register,result_address,iterator,pattern_count, instr, shift_amount)
				else:
					print_tags(out, instr)
					op2_func(instruction, out, result_register,result_address,iterator,pattern_count, instr)
			elif (catergory == 'b_'):
				out.write("jal reset_offsets\n")
				out.write("operation_"+instr+"_lo:\n")
				hi_lo_func_func(instruction, out, result_register,result_address,iterator,pattern_count, instr)
				out.write("jal reset_offsets\n")
				out.write("operation_"+instr+"_hi:\n")
				hi_lo_func_func_a(instruction, out, result_register,result_address,iterator,pattern_count, instr)
			elif (catergory == 'c_'):
				out.write("jal reset_offsets\n")
				out.write("operation_"+instr+"_hi_lo:\n")
				hi_lo_mt_func(instruction, out, result_register,result_address,iterator,pattern_count, instr)
			else:
				nothing = ''
 		except IndexError:
 			firstPass = False
 	else:
 		do="nothing"

 f.close()
