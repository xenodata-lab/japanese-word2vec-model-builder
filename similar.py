import sys
import gensim

model = gensim.models.KeyedVectors.load('output/word2vec.gensim.model')

print(sys.argv[1:])
for word in model.wv.most_similar(sys.argv[1:]):
    print(word)
