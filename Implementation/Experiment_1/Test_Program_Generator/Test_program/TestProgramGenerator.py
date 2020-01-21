# Copyright (C) 2020 Oyeniran Adeboye Stephen, Olusiji, Osidibo
import reset
import load_memory
import op2_template
import op1_template
import pseudo_template
import register_test
import pipeline


parameter = "parameter.txt"

l = open(parameter,'r')
out = open('outputme.txt', 'w')

#interrupt
reset.interrupt_function(out)

#reset registers
reset.reset_function(out)

iterator = 0
pattern_count = 0
result_address = 0
pattern_address = 0
result_register = 0
shift_amount = 0
jump_address = 0
branch_count = 0
source_register1 = 0
source_register2 = 0

# fixes the parameter used for the program
print "............parameters............."
firstPass = True
for line in l:
	if "=" in line:
		try:
		 	check = line.split("=")
			if (check[0] == 'iterator'):
				iterator = check[1].rstrip()
			elif (check[0] == 'pattern_count'):
				pattern_count = check[1].rstrip()
			elif (check[0] == 'result_address'):
				result_address = check[1].rstrip()
			elif (check[0] == 'pattern_address'):
				pattern_address = check[1].rstrip()
			elif (check[0] == 'result_register'):
				result_register = check[1].rstrip()
			elif (check[0] == 'shift_amount'):
				shift_amount = check[1].rstrip()
			elif (check[0] == 'jump_address'):
				jump_address = check[1].rstrip()
			elif (check[0] == 'branch_count'):
				branch_count = check[1].rstrip()
			elif (check[0] == 'source_register1'):
				source_register1 = check[1].rstrip()
			elif (check[0] == 'source_register2'):
				source_register2 = check[1].rstrip()
		except IndexError:
			firstPass = False

print 'iterator =', iterator
print 'pattern_count =', pattern_count
print 'store_result_address =', result_address
print 'test_pattern_address =', pattern_address
print 'result_register =', result_register
print 'jump_address =', jump_address
print 'branch_count =', branch_count
print 'source_register1 =', source_register1
print 'source_register2 =', source_register2
print "...................................."

out.write(" main:\n")
out.write(";........other test........;\n")
out.write(";........reset $26 back for branch loops........;\n")
out.write(" lui $%s, %d\n" % (branch_count, 0))
#out.write(" ori $%s, $%s, %d\n" % (branch_count, branch_count, branch_total_pattern*2))
out.write(";........reset $28 back for other test loops........;\n")
out.write(" lui $%s, %d\n" % (pattern_count, 0))
#out.write(" ori $%s, $%s, %d\n" % (pattern_count, pattern_count, total_pattern*2))
out.write(";........set memory location for signature........;\n")
out.write(" lui $%s, %d\n" % (result_address, 1))
out.write(" ori $%s, $%s, %d\n\n" % (result_address, result_address, 6000))

out.write(" jal reset_offsets\n")

#syscall
pipeline.syscall(out)

##template for psuedo-exhaustive data
out.write(";..........data-path test..........;\n")
out.write(" lui $%s, %d\n" % (result_address, 1))
out.write(" ori $%s, $%s, %d\n\n" % (result_address, result_address, 10000))
pseudo_template.make_pseudo_template(parameter,out, result_register)

#break
pipeline.breaks(out)

#pattern loading, reset offset module, increment offset
reset.end_program(out)
reset.load_pattern(out, pattern_address)
reset.reset_offsets(out, pattern_address,iterator,result_register)
reset.increment_offset(out, pattern_address,iterator, result_address)
reset.increment(out, pattern_address,iterator, result_address)
reset.store(out,result_register, result_address)
reset.init_cp(out)


out.write("end:\n")
out.write("\t j end\n")

out.close()
l.close()
