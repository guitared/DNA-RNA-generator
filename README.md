## DNA/RNA Sequence Random Generator
#### Bioinformatics Programming

###### generator.py
generated DNA or RNA with probability from relative proportions (%) of bases in human DNA, from [Chargaff's rules](https://en.wikipedia.org/wiki/Chargaff%27s_rules)
```
usage: generator.py [-h] [-v] [-d] [-r] [-t] [-f] [-l LENGTH] [-o OUTPUT]

DNA or RNA Sequence Random Generator

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         show information
  -d, --dna             output DNA type (default)
  -r, --rna             output RNA type
  -t, --text            generated output as plain text file (default)
  -f, --fasta           generated output as FASTA file
  -l LENGTH, --length LENGTH
                        length of generated sequence (default:100)
  -o OUTPUT, --output OUTPUT
                        generated file name (default:output)
```
###### report.py
generated complementary DNA sequence of the input sequence, aequence length, and percentage of existence of each base nucleotide as FASTA file

```
usage: report.py [-h] [-v] [-o OUTPUT] input

DNA Information Report Generator

positional arguments:
  input                 input data as plain text or FASTA file

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         show information
  -o OUTPUT, --output OUTPUT
                        output file name (default:report.fas)
```