from random import randint
#Dna = string
#k = length of kmer
#t = num of motifs generated i think
def RandomizedMotifSearch(dna, k, t):
    motifs = []
    for i in range(t):
        num = randint(0, len(dna[0])-k)
        kmer = dna[i][num:num+k]
        motifs.append(kmer)

    bestMotifs = motifs

    while True:
        profile = Profile(motifs)
        motifs = [] #idk why this works but I think it was having trouble overwriting the old motifs before I did this
        for i in range(t):
            motifs.append(MotifAgain(dna[i], k , profile))

        if Score(motifs) < Score(bestMotifs):
            bestMotifs = motifs
        else:
            return bestMotifs




#this profiles the motifs with pseudocounts. I think. the book was hard to understand while talking about profiling :)
def Profile(mot):
    k = len(mot[0])
    t = len(mot)
    dic = {Symbol: [1 / (t + 4)] * k for Symbol in 'ATGC'} #not gonna lie I took this from a w3schools excersize and midfied it to fit the DNA symbols (ATCG)
    for i in range(k):
        for r in mot:
            dic[r[i]][i] += 1/(t+4)
    return dic

def MotifAgain(dna, k, profile):
    motifList = []
    for i in range(len(dna) - k +1):
        motifList.append((Probability(dna[i:i+k], profile), dna[i:i+k]))

    if max(motifList)[0] == 0:
        return dna[0:k]
    else:
        return max(motifList)[1]

def Probability(dna, profile):
    concensus = 1.0
    for j, i in enumerate(dna):
        concensus *= profile[i][j]

    return concensus

def Score(Motifs):
    s = 0
    for i in range(len(Motifs[0])):
        mot = [motif[i] for motif in Motifs]
        s += (len(mot) - max(mot.count("A"), mot.count("C"), mot.count("T"), mot.count("G")))
    return s

#k=8
#t=5
input0 = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG','TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC','AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
#k=6
#t=8
input1 = [ 'AATTGGCACATCATTATCGATAACGATTCGCCGCATTGCC','GGTTAACATCGAATAACTGACACCTGCTCTGGCACCGCTC',
'AATTGGCGGCGGTATAGCCAGATAGTGCCAATAATTTCCT','GGTTAATGGTGAAGTGTGGGTTATGGGGAAAGGCAGACTG',
'AATTGGACGGCAACTACGGTTACAACGCAGCAAGAATATT','GGTTAACTGTTGTTGCTAACACCGTTAAGCGACGGCAACT',
'AATTGGCCAACGTAGGCGCGGCTTGGCATCTCGGTGTGTG','GGTTAAAAGGCGCATCTTACTCTTTTCGCTTTCAAAAAAA']
#k=6
#t=8
input2 = ['GCACATCATTAAACGATTCGCCGCATTGCCTCGATTAACC','TCATAACTGACACCTGCTCTGGCACCGCTCATCCAAGGCC',
'AAGCGGGTATAGCCAGATAGTGCCAATAATTTCCTTAACC','AGTCGGTGGTGAAGTGTGGGTTATGGGGAAAGGCAAGGCC',
'AACCGGACGGCAACTACGGTTACAACGCAGCAAGTTAACC','AGGCGTCTGTTGTTGCTAACACCGTTAAGCGACGAAGGCC',
'AAGCTTCCAACATCGTCTTGGCATCTCGGTGTGTTTAACC','AATTGAACATCTTACTCTTTTCGCTTTCAAAAAAAAGGCC']

#Test code for input0
BestMotifs = RandomizedMotifSearch(input0, 8, 5)
#i think this runs it 1000 times
for _ in range(1, 1000):
    M = RandomizedMotifSearch(input0, 8, 5)
    if Score(M) < Score(BestMotifs):
        BestMotifs = M
print(BestMotifs)

#Test code for input1
BestMotifs = RandomizedMotifSearch(input1, 6, 8)
#i think this runs it 1000 times
for _ in range(1, 1000):
    M = RandomizedMotifSearch(input1, 6, 8)
    if Score(M) < Score(BestMotifs):
        BestMotifs = M
print(BestMotifs)

#Test code for input2
BestMotifs = RandomizedMotifSearch(input2, 6, 8)
#i think this runs it 1000 times
for _ in range(1, 1000):
    M = RandomizedMotifSearch(input2, 6, 8)
    if Score(M) < Score(BestMotifs):
        BestMotifs = M
print(BestMotifs)

