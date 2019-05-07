# install deepai_nlp
# git clone https://github.com/deepai-solutions/deepai_nlp.git
# pip install -e
# install gensim
# conda install -c anaconda gensim
# or
# pip install gensim
# core i7 6700HQ 2.6GHz
# RAM 8G - Nividia Geforce GTX 950M

import matplotlib.pyplot as plt
import os
import pickle

import gensim
import numpy
from gensim import corpora
from gensim.models.coherencemodel import CoherenceModel

from deepai_nlp.tokenization.crf_tokenizer import CrfTokenizer
from deepai_nlp.word_embedding import word2vec_gensim
from prepare import preprocess_text
from coherence import compute_coherence_values

tokenizer = CrfTokenizer()


def read_data(dir, files, rate_read):
    i = 0
    data = []
    for path in files:
        print('Load file', path)
        with open(dir + path, 'r') as file:
            data.append(file.read())
            file.close()

        files.remove(path)
        # break
        if (i / max_files > rate_read):
            break
        else:
            i = i + 1
            print("Count: ", i)

    print("Clean text")
    return preprocess_text(data, tokenizer)


# open folder
dir = 'data/'
path, dirs, files = next(os.walk(dir))
max_files = len(files)
num_topic = 71

# and read data
text_data = read_data(dir, files, 0.01)

# Preprocessing the raw text

# Map text
print("Mapping")
dictionary = corpora.Dictionary(text_data)


# Remove stopwords
print("Remove Stopwords")
dictionary.filter_extremes(no_below=10, no_above=0.1, keep_n=100000)
dictionary.compactify()
bow_corpus = [dictionary.doc2bow(doc) for doc in text_data]

# training
# parameter LdaMulticore see in https://radimrehurek.com/gensim/models/ldamulticore.html
print("Training")
# lda_model = gensim.models.LdaMulticore(
#     bow_corpus,
#     num_topics=num_topic,
#     id2word=dictionary,
#     passes=15,
#     workers=8,
#     minimum_probability=0.04,
#     random_state=50,
#     alpha=1e-2,
#     chunksize=3000,
#     eta=0.5e-2,
# )
limit = 50
start = 15
step = 10

model_list, coherence_values = compute_coherence_values(
    dictionary=dictionary, bow_corpus=bow_corpus, texts=text_data, start=start, limit=limit, step=step)
x = range(start, limit, step)

plt.plot(x, coherence_values)
plt.xlabel("Num Topics")
plt.ylabel("Coherence score")
plt.legend(("coherence_values"), loc='best')
plt.show()

lda_model = []
num_topic = 0
cv_max = 0
i = 0
for m, cv in zip(x, coherence_values):
    if cv_max <= cv:
        num_topic = m
        cv_max = cv
        lda_model = model_list[i]
    i += 1
print("Done")

# for idx, topic in lda_model.print_topics(-1):
#     print("Topic: {} \nWords: {}".format(idx, topic))
#     print("\n")

# save model

print("Save")
# save corpus
pickle.dump(bow_corpus, open(f'corpus_{num_topic}.pkl', 'wb'))
# save dictionary
dictionary.save(f'dictionary_{num_topic}.gensim')
# save LDA model
lda_model.save(f'model_{num_topic}.gensim')
