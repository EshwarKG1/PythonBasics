# COmmand-line argument using sys
import sys

n = len(sys.argv)

print("The name of the script is :",sys.argv[0])

for i in range(1,n):
    print("The elements are:",sys.argv[i])
    
print("Sum is:")
sum =0
for i in range(1,n):
    sum += int(sys.argv[i])
    
print(sum)

# command-line argument using Argparser
import argparse
parser = argparse.ArgumentParser()
parser.parse_args()

# Command-line argument using Getopt()
import getopt,sys
arg_elements = sys.argv[1:]

options = "hmo:"

long_options = ["Help", "My_file", "Output ="]

try:
    arguments, values = getopt.getopt(arg_elements, options, long_options)
     
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--Help"):
            print ("Displaying Help")
             
        elif currentArgument in ("-m", "--My_file"):
            print ("Displaying file_name:", sys.argv[0])
             
        elif currentArgument in ("-o", "--Output"):
            print (("Enabling special output mode (% s)") % (currentValue))
             
except getopt.error as err:
    print (str(err))