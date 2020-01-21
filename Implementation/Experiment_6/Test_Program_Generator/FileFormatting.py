f = open('out.txt','r')      #input file
out = open('output.txt', 'w') #output file

#Number of testpatterns
line_number = len(open('input/data.txt').readlines())
print "pattern number: ", line_number

line=f.readlines() # Copying all content of the input file to variable line
numberLine = len(line) # Getting the total number of line in the input file

counter=1
counterResult=0
position=0

lines=[]    # Array for writing operands and results
operandArray = list() # List to copy out operands from the file
resultArray = list()    #List to copy out result of operation from the file
first = False         # Boolean variable to manage exception

#number_of_input=int(input('number of inputs: '))  # Getting the number of input data
number_of_input = line_number *2 # This will give the total number of operands(Operand A + Operand B)
if (number_of_input %2) == 0:
    for i in line:
        if counter<= number_of_input:
            operandArray.append(i.strip())  #Copying out operands from the file to the operand list
        else:
            resultArray.append(i.strip())   #Copying out result of operation to the list
        counter+=1

# Getting the number of lines in the output files. Variably determining the number of rows and column
    lengthOfOperandArray =len(operandArray)
    lengthOfResultArray = len(resultArray)
    numberOfOperation = lengthOfResultArray  / lengthOfOperandArray  # number of columns
    setOfOperand= number_of_input /2 # number of rows

    for x in range(0,setOfOperand):
            try:
                lines.append(operandArray[position] + " " + operandArray [position+1])   #Formatting pair of operands and storing them in the lines array
                position= position + 2
            except IndexError:
                first = True

 # Appending each pair of operands with their corresponding result
    for y in range(0, lengthOfResultArray):
        for z in range(0, setOfOperand):
            try:
               if counterResult <= lengthOfResultArray:
                lines[z] += " "  + resultArray[counterResult]
                counterResult +=1
            except IndexError:
                 first=True

 # Writing the content in the lines array to a file
    for line in lines:
        out.write(line + "\n")

# Closing the files
    out.close()
    f.close()

else:
    print ("The operands is a pair of two values so number of operand must be an even number")
