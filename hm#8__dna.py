#Yandi Xu
#CSC 110, Section: 001k
#Project #8: DNA
#This function has used input file and list to build a new output file. 

MINIMUM = 5  #minimum number of codons in a coding sequence.
PERCENT = 30  #minimum sum of p(C+G) in a coding sequence.
NUCLEOTID = 4  #number of nucletides in DNA.
PRECODON = 3  #number of nucleotides in pre codon.
DASH = "-"  #dash symbol

def main():
    intro()
    name,sequence = file_read() #the name cotent sequences returned a list. 
    total = []
    dash = []
    nsequence = []
    
    for line in sequence:
        nucleotides = count(line)
        total.append(nucleotides)  #add all nucletodies list together。
        dash_num = 0

        #this for loop is used to count the occurence of dash in each sequence.
        for words in line:
            if words == DASH:
                dash_num += 1
            sub_dash = dash_num           
        dash.append(sub_dash)
        
        #this while loop is used to remove the dash symbols in sequences.
        while DASH in line:  
            line = line.replace(DASH,'')
        nsequence.append(line.upper())
    #get the mass list and a sum list of all mass lists
    mass,totalmass = masscal(total,dash)
    #get the sum list of all codons in sequences.
    codons = codon(nsequence) 
    
    outfile = input("Output file name? ")  #get the name of output file
    output = open(outfile,"w")  #open the output file

    #this for loop is used to add string into the output file.
    for i in range(len(sequence)):
        output.write("Region Name: "+name[i])
        output.write("Nucleotides: "+sequence[i].upper())
        output.write("Nuc. Counts: "+str(total[i])+"\n")       
        output.write("Total Mass%: "+str(mass[i])+" of "+str(totalmass[i])+"\n")
        output.write("Codons List: "+str(codons[i])+"\n")
        #identify whether a senquence is coding sequence.
        result = protein(mass)
        for j in range(len(mass)):
            massstr = mass[j]
            if float(massstr[1]+massstr[2]) >= PERCENT:
                result += 1
        if result == 2:
            string = "YES"
        else:
            string = "NO"
        output.write("Is Protein? "+string+"\n")
        output.write("\n")
    output.close() #close the output file

#This function print the introduction of the whole program.
def intro():
    print("This program reports information about DNA")
    print("nucleotide sequences taht my encode proteins.")
    
#This function read the input file and seprate it into two list.
#Return: name: a list contain the name of each sequnece
#        sequnece: a list contain the original form of each sequence.       
def file_read():
    name = []
    sequence = []
    filename = input("Input file name? ")
    lines = open(filename).readlines()  #read the file by lines.
    
    #identify which list should the lne goes to.
    for i in range(len(lines)):
        if i%2 == 0:
            name.append(lines[i])
        else:
            sequence.append(lines[i])
    return name,sequence

#This function count the number of A,C,G,T in each sequence.
#Parameter： line： line in sequence list
#Return： nucleotides：a list 
def count(line):
    nucleotides = [0]*NUCLEOTID
    for words in line:       
        if words.upper() == "A":
            nucleotides[-4] += 1
        elif words.upper() == "C":
            nucleotides[-3] += 1
        elif words.upper() == "G":
            nucleotides[-2] += 1
        elif words.upper() == "T":
            nucleotides[-1] += 1           
    return nucleotides
                             
#This function list the mass of each nucleotide in a sequence， and for these
#lists to a new summary list.
#Parameter: total: a list contain the number A,C,G,T in each sequence.
#           dash: a list of dashes in each sequence.
#Return: mass: a list of A,C,G,T in a sequence
#        totalmass: a sum list of mass lists
def masscal(total,dash,):
    mass = [] 
    totalmass = []
    for j in range(len(total)):
        dashcount = dash[j] #get the number of dahs in each sequence
        line = total[j]      
        massa = round(135.128*line[-4],1)
        massc = round(111.103*line[-3],1)
        massg = round(151.128*line[-2],1)
        masst = round(125.107*line[-1],1)
        mass_subsum = round(massa+ massc + massg + masst + dashcount*100,1)            
        mass.append([round(massa/mass_subsum*100,1),
                     round(massc/mass_subsum*100,1),
                     round(massg/mass_subsum*100,1),
                     round(masst/mass_subsum*100,1)])
        totalmass.append(mass_subsum) 
    return mass,totalmass

#This function used to seperate each sequence by 3 to get a codon list.
#Parameter: nsequence:list of sequences without dash and all be capitial letter.
#Return: codon_sum: a sum list for the codons in each sequence.   
def codon(nsequence):
    codon_list = [] #list of codon in each sequence
    codon_sum = [] #sum of codon_list
    for line in nsequence:
        for i in range(0,len(line)-1,PRECODON):
            codons = line[i:i+PRECODON]
            codon_list.append(str(codons))
        codon_sum.append(codon_list)
        codon_list = []       
    return codon_sum

#This function used to identify whether a sequenceis a coding sequence.
#Parameter: codons: codon_sum list return from codon(sequence) function.
#Return: TRUE: an accumu number help to identity.            
def protein(codons):
    TRUE = 0
    for i in range(len(codons)):
        if codons[i][0] == "ATG" and (codons[i][-1] in "TAA"or"TAG"or"TGA"):
            TRUE += 1
        if len(codons[i]) >= MINIMUM:
            TRUE += 1
    return TRUE
    
        
main()
    
