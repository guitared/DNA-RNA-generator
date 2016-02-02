#!/usr/bin/python

# DNA/RNA Sequence Random Generator
# Bioinformatics Programming
# by Thatchapatt Kesornsri, 2016

import sys,argparse,random
parser = argparse.ArgumentParser(description='DNA or RNA Sequence Random Generator')
parser.add_argument('-v','--verbose',help='show information',action='store_true')
parser.add_argument('-d','--dna',help='output DNA type (default)',action='store_true')
parser.add_argument('-r','--rna',help='output RNA type',action='store_true')
parser.add_argument('-t','--text',help='generated output as plain text file (default)',action='store_true')
parser.add_argument('-f','--fasta',help='generated output as FASTA file',action="store_true")
parser.add_argument('-l','--length',type=int,default=100,help='length of generated sequence (default:100)')
parser.add_argument('-o','--output',default = 'output',help='generated file name (default:output)')
args = parser.parse_args()
if args.rna:
	seq  = 'AUCG'
	type = 'RNA'
else:
	seq = 'ATCG'
	type = 'DNA'
if args.verbose:
		print 'Generating '+str(args.length)+' random '+type+' sequence...\n'
output = ''
for i in range(args.length):
	if( i>0 and i%80==0 ):
		output += '\n'
	output += random.choice(seq)
if args.verbose:
		print output+'\n'
if args.fasta:
	outfile = args.output+'.fas'
else:
	outfile = args.output+'.txt'
if args.verbose:
		print 'Saved result to '+outfile+'\n'
f = open(outfile, 'w')
if args.fasta:
	f.write(';DNA/RNA Sequence Random Generator\n')
	f.write(';Bioinformatics Programming\n')
	f.write(';by Thatchapatt Kesornsri, 2016\n')
	f.write('>'+args.output+'|'+str(args.length)+'| generated '+str(args.length)+' random '+type+' sequence\n')
f.write(output)