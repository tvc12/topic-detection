# install deepai_nlp
# git clone https://github.com/deepai-solutions/deepai_nlp.git
# pip install -e
# install gensim
# conda install -c anaconda gensim
# or
# pip install gensim
# core i7 6700HQ 2.6GHz
# RAM 8G - Nividia Geforce GTX 950M


from deepai_nlp.tokenization.crf_tokenizer import CrfTokenizer
from prepare import preprocess_text
from deepai_nlp.word_embedding import word2vec_gensim
from gensim import corpora
import gensim
import os
import numpy
import pickle

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
num_topic = 24

# and read data
text_data = read_data(dir, files, 0.1)

# Preprocessing the raw text

# Map text
print("Mapping")
dictionary = corpora.Dictionary(text_data)


# Remove stopwords
print("Remove Stopwords")
dictionary.filter_extremes(no_below=20, no_above=0.1, keep_n=100000)
dictionary.compactify()
bow_corpus = [dictionary.doc2bow(doc) for doc in text_data]

# training
# parameter LdaMulticore see in https://radimrehurek.com/gensim/models/ldamulticore.html
print("Training")
lda_model = gensim.models.LdaMulticore(
    bow_corpus,
    num_topics=num_topic,
    id2word=dictionary,
    passes=15,
    workers=8,
    minimum_probability=0.4,
    random_state=40,
    # alpha=1e-2,
    chunksize=100,
    # eta=0.5e-2,
)
print("Done")

for idx, topic in lda_model.print_topics(-1):
    print("Topic: {} \nWords: {}".format(idx, topic))
    print("\n")

# save model

print("Save")
# save corpus
pickle.dump(bow_corpus, open(f'corpus_{num_topic}.pkl', 'wb'))
# save dictionary
dictionary.save(f'dictionary_{num_topic}.gensim')
# save LDA model
lda_model.save(f'model_{num_topic}.gensim')
