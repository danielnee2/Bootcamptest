# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:06:32 2015

@author: niyuli
"""

import Bio
import Bio.Seq
import Bio.Alphabet.IUPAC
import Bio.SeqIO
import Bio.AlignIO
import Bio.Entrez
import random

print (Bio.__version__)

myseq = Bio.Seq.Seq("CAT CAT CAT UTC UUG UCG UUG CCU CTU GUG UUG TTC UTG")

myseq = Bio.Seq.Seq(str(myseq), Bio.Alphabet.IUPAC.IUPACUnambiguousDNA())

myseq = str(myseq).replace(" ", '')
myseq = Bio.Seq.Seq(str(myseq), Bio.Alphabet.IUPAC.IUPACUnambiguousDNA())

print (myseq.translate() )
print ('whole sequnce', myseq)
print ("Every fourth necleotide: ", myseq[::4])


proteinseq = myseq.translate()
reversecomplement = myseq.reverse_complement()
revcomp_protein =  reversecomplement.translate()

print("rev complement", reversecomplement)
print ("revcomp_protien", reversecomplement.translate())

revcomp_protein = revcomp_protein[: -3]
print ("revcomp --> protein minus 3", revcomp_protein)



myseqrecord = Bio.SeqRecord.SeqRecord(id="MyFirstSeq", description = "This is my first seq record",
                                      seq=myseq)
print(myseqrecord)

myseqrecord.format("fasta")
print(myseqrecord.format("fasta"))
print(myseqrecord.format("genbank"))                                      
print(myseqrecord.format("seqxml"))


myseq = ["A","T","C","G"]*25
seq_record_list = []
for i in range(100):
    random.shuffle(myseq)
    
    myseq_object = Bio.Seq.Seq("".join(myseq), Bio.Alphabet.IUPAC.IUPACUnambiguousDNA())
    
    seq_record = Bio.SeqRecord.SeqRecord(id = str(i), description = '', seq = myseq_object)
    seq_record_list.append(seq_record)
    
count = Bio.SeqIO.write(seq_record_list, "l31_random_seqs.fna", "fasta")    


input_file = Bio.SeqIO.parse("l31_random_seqs.fna", "fasta")

for record in input_file:
    print(record.format("fasta"), end='')


my_alignment = Bio.AlignIO.read("l31_random_seqs.fna", "fasta")
print(my_alignment)

Bio.AlignIO.write(my_alignment, "l31_random_seqs.stk", "stockholm")




