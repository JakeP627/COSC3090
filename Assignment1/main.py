input0 = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
input1 = 'TGGTAGCGACGTTGGTCCCGCCGCTTGAGAATCTGGATGAACATAAGCTCCCACTTGGCTTATTCAGAGAACTGGTCAACACTTGTCTCTCCCAGCCAGGTCTGACCACCGGGCAACTTTTAGAGCACTATCGTGGTACAAATAATGCTGCCAC'
input2 = 'CAGTGGCAGATGACATTTTGCTGGTCGACTGGTTACAACAACGCCTGGGGCTTTTGAGCAACGAGACTTTTCAATGTTGCACCGTTTGCTGCATGATATTGAAAACAATATCACCAAATAAATAACGCCTTAGTAAGTAGCTTTT'
input3 = 'ATACAATTACAGTCTGGAACCGGATGAACTGGCCGCAGGTTAACAACAGAGTTGCCAGGCACTGCCGCTGACCAGCAACAACAACAATGACTTTGACGCGAAGGGGATGGCATGAGCGAACTGATCGTCAGCCGTCAGCAACGAGTATTGTTGCTGACCCTTAACAATCCCGCCGCACGTAATGCGCTAACTAATGCCCTGCTG'
input4 = 'CCAGCGGGGGTTGATGCTCTGGGGGTCACAAGATTGCATTTTTATGGGGTTGCAAAAATGTTTTTTACGGCAGATTCATTTAAAATGCCCACTGGCTGGAGACATAGCCCGGATGCGCGTCTTTTACAACGTATTGCGGGGTAAAATCGTAGATGTTTTAAAATAGGCGTAAC'

def FrequentWordsProblem(inp,k):
    counts = []
    kmerPatern = []
    for i in range(len(inp)-k+1):
        kmer = inp[i:i+k]
        if len(kmerPatern) == 0:
            #if the list is empty
            kmerPatern.append(kmer)
            counts.append(1)
        elif kmer in kmerPatern:
            #if this kmer has been seen before
            kmerPatern.append(kmer)
            counts.append(0)
            # we need to go to the first spot where that value occurs
            counts[kmerPatern.index(kmer)] += 1
        else:
            #First time occurance, add it to the list and give it a count of 1
            kmerPatern.append(kmer)
            counts.append(1)

    m = max(counts)
    output = []
    for i, val in enumerate(counts):
        if val == m:
            output.append(kmerPatern[i])

    return(output)


print(FrequentWordsProblem(input0, 4))
print(FrequentWordsProblem(input1, 3))
print(FrequentWordsProblem(input2, 4))
print(FrequentWordsProblem(input3, 5))
print(FrequentWordsProblem(input4, 5))


