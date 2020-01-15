Japanese Word2Vec Model Builder
===============================

A tool for building gensim word2vec model for Japanese.

It uses MeCab for tokenization with mecab-ipadic-NEologd as a dictionary.
Wikipedia is used as a corpus for training word2vec model.

Setup
-----

```
docker build -t w2v .
```

Run
---

An example to build a model at the default path. (output/word2vec.gensim.model)

```
./build --download-neologd --csv-dataset-path CSV_DIR --build-gensim-model
```

Another example to specify hyper parameters.

```
./build --download-neologd --csv-dataset-path CSV_DIR --build-gensim-model \
    -o output/another.model --size=50 --window=10 --min-count=5
```

How to use the model
--------------------

```
from gensim.models.word2vec import Word2Vec

model_path = 'output/word2vec.gensim.model'
model = Word2Vec.load(model_path)
```

How to demo
-----------

```
# python3 similar.py 下落 暴落
['下落', '暴落']
('急落', 0.906057596206665)
('急騰', 0.896533191204071)
('急上昇', 0.8698370456695557)
('上昇', 0.8561219573020935)
('乱高下', 0.8194584846496582)
('暴騰', 0.790680468082428)
('高騰', 0.7381042838096619)
('値上がり', 0.7311292886734009)
('軟化', 0.7152347564697266)
('低下', 0.7109802961349487)
```
