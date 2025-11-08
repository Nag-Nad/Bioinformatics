# Define the Melting Temperature calcuator function
def Tm(seq):
    A = seq.count('A')
    T = seq.count('T')
    G = seq.count('G')
    C = seq.count('C')
    if len(seq) <= 14:
        Tm= (A+T) * 2 + (G+C) * 4
    else:
        Tm= 64.9 +41*(G+C-16.4)/(A+T+G+C) 
    return Tm

# Define the CG content of a sequence 
def CG_content(seq):
    c_content = seq.count('C')
    g_content = seq.count('G')
    CG_content = (g_content + c_content)/len(seq) * 100
    return CG_content


# Calculate the melting temperature from the user input
seq = input('please write your sequence: ')
seq = seq.upper()
melting_temprature = Tm(seq)
print('The Tm for this sequence is:', melting_temprature, '°C')

# Add two conditions of a bad and optimal Tm result 
if Tm(seq) > 65:
    print('Your primer has a tendency for secondary annealing')
elif 52<Tm(seq)<58:
    print('The melting temperature of your sequence is optimal.')
    
# Calculate the CG content from the user input
cg_content = CG_content(seq)
print('The CG content of this sequence is', cg_content,'%')

# Add a condition of an optimal CG content 
if 40<CG_content(seq)<60:
    print('The CG content of this sequence is optimal.')