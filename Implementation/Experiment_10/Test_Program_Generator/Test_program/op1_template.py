# Copyright (C) 2018 Oyeniran Adeboye Stephen, Olusiji
import reset
def generate_immediate(instruct, out, result_register, result_address, inputFile):
	data_lines = []
	total_pattern = len(open('../input/data.txt').readlines())
 	f = open(inputFile,'r')
	k = 0
	n = 0
 	for line in f:
	 n = n + 1
 	 bit_set1 = line[48:64]
 	 immediate = str(int(bit_set1,2))
	 immediate_fun(instruct, out, result_register,result_address, immediate, k)
	 if (total_pattern == n):
	 	out.write("\n")
	f.close()

def immediate_fun(instruction, file, result_register, result_address, immediate, k):
    file.write("\tjal load_patterns\n")
    file.write("\t%s $%s, $%d, %s\n" % (instruction, result_register, 15, immediate))
    file.write("\tsw $%s, %s($%s)\n" % (result_register, k, result_address))
    file.write("\tjal increment_immediate\n")

def branch_1(instruction, file, result_register,result_address,iterator,pattern_count, instr):
    file.write("\tjal load_patterns\n")
    file.write("\t%s $%s, $%d, $%d\n" % ('and', result_register, 15, 16))
    file.write("\t%s $%d, $%d, store_branch\n" % (instruction, 15, 16))
    file.write("\tjal increment_offset\n")
    file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr))

def branch_2(instruction, file, result_register,result_address,iterator,pattern_count, instr):
    file.write("\tjal load_patterns\n")
    file.write("\t%s $%s, $%d, $%d\n" % ('and', result_register, 15, 316))
    if ((instruction == 'bgezal') or (instruction == 'bltzal')):
    	file.write("\t%s $%d, store_branch\n" % (instruction, 15))
    else:
    	store = str("store_"+instruction)
    	file.write("\t%s $%d, %s\n" % (instruction, 15, store))
    file.write("\tsw $%d, %d($%s)\n" % (0, 0, result_address))
    file.write("\tjal increment_offset\n")
    file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr))

def branc_location(instruction, file, result_address):
    file.write(" store_"+instruction+":\n")
    file.write("\tsw $%d, %d($%s)\n" % (18, 0, result_address))
    file.write("\tjal increment_offset\n\n")

def co_processor_fun(instruction, file, result_register, result_address, iterator, pattern_count, instr, cp_register):
	file.write("\tjal load_patterns\n")
	file.write("\t%s $%d, $%d\n" % (instruction, 15, cp_register-1))
	file.write("\t%s $%d, $%d\n" % (instruction, 16, cp_register))
	file.write("\tswc0 $%s, %d($%s)\n" % (cp_register-1, 0, result_address))
	file.write("\tswc0 $%s, %d($%s)\n" % (cp_register, 4, result_address))
	file.write("\tjal increment_offset\n")
	file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr))

def co_processor_fun_2(instruction, file, result_register, result_address, iterator, pattern_count, instr, cp_register):
	file.write("\tjal load_patterns\n")
	file.write("\t%s $%d, $%d\n" % ('mtc0', 15, cp_register-1))
	file.write("\t%s $%s, $%d\n" % (instruction, result_register, cp_register-1))
	file.write("\tsw $%s, %d($%s)\n" % (result_register, 0, result_address))
	file.write("\t%s $%d, $%d\n" % ('mtc0', 16, cp_register))
	file.write("\t%s $%s, $%d\n" % (instruction, result_register, cp_register))
	file.write("\tsw $%s, %d($%s)\n" % (result_register, 4, result_address))
	file.write("\tjal increment_offset\n")
	file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr))

def lw0_sw0_fun(instruction, file, result_register, result_address, iterator, pattern_count, instr, pattern_address):
	file.write("\tlwc0 $%s, %d($%s)\n" % (result_register, 0, pattern_address))
	file.write("\tswc0 $%s, %d($%s)\n" % (result_register, 0, result_address))
	file.write("\tjal increment_offset\n")
	file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr))

def lw_sw_fun(instruction, file, result_register, result_address, iterator, pattern_count, instr, pattern_address):
	file.write("\tlw $%s, %d($%s)\n" % (result_register, 0, pattern_address))
	file.write("\tsw $%s, %d($%s)\n" % (result_register, 0, result_address))
	file.write("\tjal increment_offset\n")
	file.write("\tbne $%s, $%s, operation_%s\n\n" % (iterator, pattern_count, instr))

def print_tags(file, instr):
	file.write("jal reset_offsets\n")
	file.write("jal init_cp\n")
	file.write("operation_"+instr+":\n")

def ops1_template(para, out, result_register, result_address, inputFile,iterator, pattern_count, pattern_address ):
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
		 if (catergory == 'i_'):
			print_tags(out, instr)
			generate_immediate(instru,out,result_register,result_address, inputFile)
		 elif(catergory == '1_'):
			 print_tags(out, instr)
			 if (instruction == 'mtc0'):
			 	co_processor_fun(instruction, out,result_register,result_address, iterator,pattern_count, instr, cp_register)
			 elif(instruction == 'mfc0'):
			 	co_processor_fun_2(instruction, out,result_register,result_address, iterator,pattern_count, instr, cp_register)
		 elif(catergory == '2_'):
			 print_tags(out, instr)
			 lw_sw_fun(instruction, out,result_register,result_address, iterator,pattern_count, instr, pattern_address)
		 elif(catergory == '3_'):
			 print_tags(out, instr)
			 lw0_sw0_fun(instruction, out,result_register,result_address, iterator,pattern_count, instr, pattern_address)
		 elif(catergory == 'd_'):
			print_tags(out, instr)
			branch_1(instruction, out,result_register,result_address,iterator,pattern_count, instr)
		 elif(catergory == 'e_'):
			print_tags(out, instr)
			if ((instr == 'bgezal') or (instr == 'bltzal')):
				branch_2(instruction, out,result_register,result_address,iterator,pattern_count, instr)
			else:
				branch_2(instruction, out,result_register,result_address,iterator,pattern_count, instr)
				branc_location(instruction, out, result_address)
		except IndexError:
 				firstPass = False
	else:
		do='nothing'

 Ins.close()
