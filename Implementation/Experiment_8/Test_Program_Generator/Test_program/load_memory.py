# Copyright (C) 2018 Oyeniran Adeboye Stephen, Olusiji
#import inspect, os
import os
#path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe))) # script directory)

'''if os.path.exists("template"):
	files = [file for file in os.listdir("template")]
	for file in files:
		os.remove("template"+"/"+file)
else:
	os.mkdir("template")'''

#inputFile = "../input/data.txt"
#outputFile ="template/load_template.txt"

#f = open(inputFile,'r')         #input file
#out = open(outputFile, 'w')     #output file
offset = 0
def init_patterns(out,data_f, pattern_address):
 out.write("init_patterns:\n")
 #offset = 0
 global offset
 register = 8
 outline = []
 line = data_f.readlines()

 for i in (line):

 #selection by 16 bits
     bit_set1 = i[:16]
     bit_set2 = i[16:32]
     bit_set3 = i[32:48]
     bit_set4 = i[48:64]

 #Writing to output file
     for x in range(2):
         if (x == 0):
             most_sig_bit   = int(bit_set1,2)
             least_sig_bit  = int(bit_set2,2)
         else:
             most_sig_bit   = int(bit_set3,2)
             least_sig_bit  = int(bit_set4,2)
         out.write(" lui $%d, %d\n" % (register, most_sig_bit))
         out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
         out.write(" sw $%d, %d($%s)\n" % (register, offset, pattern_address))
         offset += 4
         if (register >= 15):
             register = 8
         else:
             register += 1
 out.write(" jr $31\n\n")

def load_branch(out, pattern_address):
    global offset
    register = offset
    out.write("load_branch:\n")
    out.write(" lw $%d, %d($%s)\n" % (15, register, pattern_address))
    out.write(" lw $%d, %d($%s)\n" % (16, register+4, pattern_address))
    out.write(" jr $31\n\n")

def init_patterns_branch(out,data_f, pattern_address):
 out.write("init_branch:\n")
 #offset = 0
 global offset
 register = 8
 outline = []
 line = data_f.readlines()

 for i in (line):

 #selection by 16 bits
     bit_set1 = i[:16]
     bit_set2 = i[16:32]
     bit_set3 = i[32:48]
     bit_set4 = i[48:64]

 #Writing to output file
     for x in range(2):
         if (x == 0):
             most_sig_bit   = int(bit_set1,2)
             least_sig_bit  = int(bit_set2,2)
         else:
             most_sig_bit   = int(bit_set3,2)
             least_sig_bit  = int(bit_set4,2)
         out.write(" lui $%d, %d\n" % (register, most_sig_bit))
         out.write(" ori $%d, $%d, %d\n" % (register, register, least_sig_bit))
         out.write(" sw $%d, %d($%s)\n" % (register, offset, pattern_address))
         offset += 4
         if (register >= 15):
             register = 8
         else:
             register += 1
 out.write(" jr $31\n\n")
