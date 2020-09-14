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
            kmerPatern.append(kmer)
            counts.append(1)
        elif kmer in kmerPatern:
            kmerPatern.append(kmer)
            #we need to go to the first spot where that value occurs
        else:
            kmerPatern.append(kmer)
            counts.append(1)

        # elif kmer in kmerPatern:
        #     counts.append(0)
        #     counts[kmerPatern.index(kmer)] += 1


    # for x, y in zip(kmerPatern, counts):
    #      print(x,y)
    #print(kmerPatern)
    # print(counts)
    #print(len(counts))

    m = max(counts)
    output = []
    for val in counts:
        if val == m:
            output.append(kmerPatern[counts.index(val)])

    print(output)




FrequentWordsProblem(input0, 4)
FrequentWordsProblem(input1, 3)
FrequentWordsProblem(input2, 4)
FrequentWordsProblem(input3, 5)
FrequentWordsProblem(input4, 5)
#print(len(input0))


