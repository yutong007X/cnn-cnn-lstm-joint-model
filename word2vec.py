import os
import json
from gensim.models.word2vec import LineSentence, Word2Vec


def func(fin, fout):
    for line in fin:
        line = line.strip()
        if not line:
            continue
        #print(line)
        sentence = json.loads(line)
        sentence = sentence["sentText"].strip().strip('"').lower()
        fout.write(sentence + '\n')


def make_corpus():
    #print("-------------haha")
    with open('data/new/corpus.txt', 'wt', encoding='utf-8') as fout:
        with open('data/new/train.json', 'rt', encoding='utf-8') as fin:
            func(fin, fout)
        with open('data/new/test.json', 'rt', encoding='utf-8') as fin:
            func(fin, fout)


if __name__ == "__main__":
    #if not os.path.exists('data/new/corpus.txt'):
    make_corpus()

    sentences = LineSentence('data/new/corpus.txt')
    model = Word2Vec(sentences, sg=1, size=300, workers=4, iter=8, negative=8, min_count=1)
    word_vectors = model.wv
    word_vectors.save('data/new/word2vec')
    word_vectors.save_word2vec_format('data/new/word2vec.txt', fvocab='data/new/vocab.txt')
