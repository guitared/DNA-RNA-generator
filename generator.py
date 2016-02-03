#!/usr/bin/python

# DNA/RNA Sequence Random Generator
# Bioinformatics Programming
# by Thatchapatt Kesornsri, 2016

import os,sys,argparse,random
parser = argparse.ArgumentParser(description='DNA or RNA Sequence Random Generator')
parser.add_argument('-v','--verbose',help='show information',action='store_true')
parser.add_argument('-d','--dna',help='output DNA type (default)',action='store_true')
parser.add_argument('-r','--rna',help='output RNA type',action='store_true')
parser.add_argument('-t','--text',help='generated output as plain text file (default)',action='store_true')
parser.add_argument('-f','--fasta',help='generated output as FASTA file',action="store_true")
parser.add_argument('-l','--length',type=int,default=100,help='length of generated sequence (default:100)')
parser.add_argument('-o','--output',default = 'output',help='generated file name (default:output)')
args = parser.parse_args()

# Relative proportions (%) of bases in human DNA ,Chargaff's rules, 1952
# A:29.3% G:20.7% C:20.0% T:30.0%

def weighted_choice(choices):
   total = sum(w for c, w in choices)
   r = random.uniform(0, total)
   upto = 0
   for c, w in choices:
      if upto + w >= r:
         return c
      upto += w
   assert False, "Shouldn't get here"

if args.rna:
	seq  = [('A',29.3),('G',20.7),('C',20.0),('U',30.0)]
	type = 'RNA'
else:
	seq = [('A',29.3),('G',20.7),('C',20.0),('T',30.0)]
	type = 'DNA'
if args.verbose:
		print 'Generating '+str(args.length)+' random '+type+' sequence...\n'
output = ''
for i in range(args.length):
	if( i>0 and i%70==0 and args.fasta):
		output += '\n'
	output += weighted_choice(seq)
if args.verbose:
		print output+'\n'
if args.fasta:
	outfile = os.path.splitext(args.output)[0]+'.fas'
else:
	outfile = os.path.splitext(args.output)[0]+'.txt'
if args.verbose:
		print 'Saved result to '+outfile+'\n'
f = open(outfile, 'w')
if args.fasta:
	f.write(';DNA/RNA Sequence Random Generator\n')
	f.write(';Bioinformatics Programming\n')
	f.write('>'+args.output+'| generated random '+type+' sequence |len='+str(args.length)+'\n')
f.write(output)