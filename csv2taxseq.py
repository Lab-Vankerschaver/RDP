from Bio import SeqIO
import csv
import sys

input_csv = sys.argv[1]
output_tax = sys.argv[2]
output_seq = sys.argv[3]

csvreader = csv.reader(open(input_csv))

seqDict = {}
taxList = []
for row in csvreader:
    seqDict[row[1]] = row[-1]
    id_tax_conc = []
    for n in range(6):
        id_tax_conc.append(row[n+1])
    taxList.append(id_tax_conc)

new_seqs = ''
new_taxon = ''
for i in taxList:
    new_seqs += '>' + i[0] + '\n'+ seqDict[i[0]] + '\n'
    for j in i:
        new_taxon += j + '\t'
    new_taxon += '\n'
new_seqs = new_seqs[8:-1]
new_taxon = new_taxon[:-1]


with open (output_tax, "w") as file_tax:
    file_tax.write(new_taxon)
    file_tax.close()
with open (output_seq, "w") as file_seq:
    file_seq.write(new_seqs)
    file_seq.close()
