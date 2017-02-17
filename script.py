# import glob
import tools
import numpy as np
import sys


# Load books
#bookFiles = glob.glob("./books/*.txt")
bookFiles = [x for x in sys.argv[1:]]

# Count words
books = []
for book in bookFiles:
    books.append(tools.wordcount(book))


# Create bag of words
bags = []
for book in books:
    bags.append(tools.bag(book,10))
print(sorted([len(bag) for bag in bags], reverse=True))

# Create jaccard distance matrix
le = len(bags)
m = np.zeros((le, le))
mean = []
for i in range(le):
    for j in range(le):
        element = 1-tools.jaccard(bags[i],bags[j])
        mean.append(element)
        m[i][j] = element
print(np.around(m, decimals=2))

# Calculate mean of the matrix's elements
print(np.sum(mean)/len(mean))

# Cluster
cluster = tools.single_linkage(m,3)
result = []
for b in list(set(cluster)):
    tmp = []
    for a in range(len(cluster)):
        if cluster[a] == b:
            tmp.append(a)
    result.append(tmp)

print(result)
