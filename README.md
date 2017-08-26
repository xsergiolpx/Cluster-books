Using the Jaccard similarity on the words of the books, this software lets you find the the books that are written in the same language and cluster them together. To do so, store the txt books on the folder "books". Some books can be retrieved from [Project Gutenberg](https://www.gutenberg.org). To run it simply use:

```
python script.py books/*.txt
```

By default it creates 3 clusters. If there are more than 3 languages, then the books who share the most similar languages will be clustered together.

The output is:
- Words of each documment
- Similarity matrix of books
- Average of the similarity matrix elements
- Clusters of books in the same language
