#!/usr/bin/python

# DNA Information Report Generator
# Bioinformatics Programming
# by Thatchapatt Kesornsri, 2016

import os,sys,argparse,random
parser = argparse.ArgumentParser(description='DNA Information Report Generator',epilog='')
parser.add_argument('input',help='input data as plain text or FASTA file')
parser.add_argument('-v','--verbose',help='show information',action='store_true')
parser.add_argument('-o','--output',default='report',help='output file name (default:report.fas)')
args = parser.parse_args()

def calculate(seq,name):
	output = '>'+name+'| from input file |len='+str(len(seq))+'\n'
	comp = ''
	c_len = len(seq)
	a=t=c=g=i=0
	for x in seq:
		if( i>0 and i%70==0):
			output += '\n'
			comp += '\n'
		if x == 'A':
			comp += 'C'
			a+=1
		if x == 'T':
			comp += 'G'
			t+=1
		if x == 'G':
			comp += 'T'
			g+=1
		if x == 'C':
			comp += 'A'
			c+=1
		output += x
		i+=1
	output += '\n;Percentage base nucleotide in '+name+' [A:'+"{0:.2f}".format(100.0*a/c_len)+'%, T:'+"{0:.2f}".format(100.0*t/c_len)+'%, C:'+"{0:.2f}".format(100.0*c/c_len)+'%, G:'+"{0:.2f}".format(100.0*g/c_len)+'%]\n'
	output += '>'+name+'_comp| complementary DNA sequence of '+name+' |len='+str(c_len)+'\n'+comp
	if args.verbose:
		print output
	return output
	
infile,extension = os.path.splitext(args.input)
f = open(args.input, 'r')
if args.verbose:
	print "Open file "+args.input+" ..."
input = f.read()
f.close()
if extension =='.txt':
	seq=input.strip()
	output = calculate(seq,infile)
elif extension =='.fas':
	output = name = seq = ''
	for line in input.split('\n'):
		if line.startswith(';'):
			continue
		if line.startswith('>'):
			if seq!='':
				output += calculate(seq,name)
				seq = ''
			name = line.split('|')[0][1:]
		else:
			seq+=line
	output += calculate(seq,name)
			
else:
	print '[Error] Unknown input type.'
f = open(os.path.splitext(args.output)[0]+'.fas', 'w')
f.write(';DNA Information Report Generator\n')
f.write(';Bioinformatics Programming\n')
f.write(output)