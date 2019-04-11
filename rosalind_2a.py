# sun.huaiyu
# PROT
codon = '''UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G '''

codon_table = dict(zip(codon.split()[0::2], codon.split()[1::2]))

rna = open('rosalind_2a.txt').readline().rstrip()

protein = [codon_table[rna[i:i+3]] for i in range(0, len(rna), 3)]

f = open('rosalind_2a_ans.txt', 'wt')
f.write(''.join(protein[:-1]))
f.close()