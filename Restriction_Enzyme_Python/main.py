
import re     # Import Regex

AbcI_restriction_site = 'A[TCG]TAAT'
AbcII_restriction_site = 'GC[AG][AT]TG'


# Define the first Restriction Enzyme(RE) function

def AbcI(dna):
    AAT= re.split('AAT', dna)
    ANT= re.split('A[TCG]T', dna)      
    product_AbcI = f'{AAT[0]} {ANT[1]}'   
     
# Where the RE cuts

    length_AbcI = re.finditer(AbcI_restriction_site, dna)
    for lengths in length_AbcI:
        global restriction_start_AbcI
        
# plus 3: .start returns the start of the sequence. But, where it is cut matters. So, plus 3 (AAT)

        restriction_start_AbcI = lengths.start() + 3    
        
    return product_AbcI


 # Define the 2nd Restriction Enzyme(RE) function   
     
def AbcII(dna):
     
    TG = re.split('TG', dna)
    GCRW = re.split('GC[AG][AT]', dna)
    product_AbcII = f'{TG[0]} {GCRW[1]}'
    
    length_AbcII = re.finditer(AbcII_restriction_site, dna)
    for lengths in length_AbcII:
        global restriction_start_AbcII

# minus 2: .end returns where the RE site ends, while we need where it is cut. So, minus 2 (TG)

        restriction_start_AbcII = lengths.end() - 2
        
    return product_AbcII


# Define a function to calcculate the lenth of the cut

def restricted_fragment(restriction_start_AbcI,restriction_start_AbcII):
    restricted_fragment_length = restriction_start_AbcII - restriction_start_AbcI
    return f'The length of the cut is {restricted_fragment_length}'
 
       
dna = 'CCATTAATCCGCGATGCC'
restriction1 = AbcI(dna)
print('The AbcI cuts at', restriction1)
restriction2= AbcII(dna)
print('The AbcII cuts at', restriction2)
insert = restricted_fragment(restriction_start_AbcI,restriction_start_AbcII)
print(insert)