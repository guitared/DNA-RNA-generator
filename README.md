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