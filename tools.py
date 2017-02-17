import re
import string
import numpy as np

def wordcount(filename):
    f = open(filename, 'r', encoding = "ISO-8859-1")
    bookTMP = f.read().lower().replace('\t', ' ').replace('\n', ' ').replace('\r', ' ')
    bookTMP = re.sub('[{}]'.format(string.punctuation), " ", bookTMP).split()
    f.close()
    counter = {}
    for word in bookTMP:
        if word is not "":
            counter[word] = counter.get(word, 0) + 1
    return counter

def bag(wc, threshold=1):
    return set([word for word in wc if wc[word] >= threshold])

def jaccard(s1, s2):
    return len(s1.intersection(s2))/len(s1.union(s2))

def single_linkage(D, k=2):
    #Create clusters
    cluster = np.array(range(len(D[0])))
    # calculate number of clusters
    k2 = len(set(cluster))
    #Change values of diagonal to high values
    D[np.diag_indices(len(D))] = 2.
    while k2 > k:
        #Change diagonal in every iteration
        D[np.diag_indices(len(D))] = 2.
        #calculate the minimum element in the matrix
        minimum = D.min()

        indexList = np.argwhere(minimum == D)
        # index in the cluster array of the element that is closest to the one found
        ind = indexList[0][1]
        # Move all elements that have that index to the same cluster
        copy = [i for i, x in enumerate(cluster) if x == ind]
        for p in range(len(copy)):
            cluster[copy[p]] = indexList[0][0]
        #Compute the new matrix writen 2. on every element of the just moved node and in the new cluster write the minimum distance of both
        for j in range(len(D[0])):
            D[indexList[0][0]][j] = min(D[indexList[0][0]][j], D[ind][j])
            D[j][indexList[0][0]] = D[indexList[0][0]][j]
            D[ind][j] = 2.
            D[j][ind] = 2.
        k2 = len(set(cluster))

    return cluster
