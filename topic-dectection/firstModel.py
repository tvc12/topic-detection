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
from deepai_nlp.tokenization.utils import preprocess_text
from deepai_nlp.word_embedding import word2vec_gensim
from gensim import corpora
import gensim
import os
import numpy
import pickle

tokenizer = CrfTokenizer()


def prepare_data(data, tokenizer):
    data = preprocess_text(data, tokenizer=tokenizer)
    return list(numpy.concatenate(data, axis=0))


def read_data(dir, files, rate_read):
    i = 0.0
    text_data = []
    for path in files:
        data = []
        with open(dir + path, 'r') as file:
            data = file.readlines()
            file.close()
        text_data.append(prepare_data(data, tokenizer))
        if (i / max_files >= rate_read):
            break
        else:
            print(i / max_files, i)
            i = i + 1
        files.remove(path)
    return text_data


# open folder
dir = 'data/'
path, dirs, files = next(os.walk(dir))
max_files = len(files)


# and read data
text_data = read_data(dir, files, 0.1)

# Preprocessing the raw text

# Map text
dictionary = corpora.Dictionary(text_data)


# Remove stopwords
print("Remove Stopwords")
dictionary.filter_extremes(no_below=10, no_above=0.3, keep_n=100000)
bow_corpus = [dictionary.doc2bow(doc) for doc in text_data]

# training
# parameter LdaMulticore see in https://radimrehurek.com/gensim/models/ldamulticore.html
print("Training")
lda_model = gensim.models.LdaMulticore(
    bow_corpus,
    num_topics=25,
    id2word=dictionary,
    passes=20,
    workers=8,
    minimum_probability=0.4,
    random_state=100,
    alpha=1e-2,
    chunksize=500,
    eta=0.5e-2,
)
print("Done")

for idx, topic in lda_model.print_topics(-1):
    print("Topic: {} \nWords: {}".format(idx, topic))
    print("\n")

# save model

print("Save")
# save corpus
pickle.dump(bow_corpus, open('corpus_25.pkl', 'wb'))
# save dictionary
dictionary.save('dictionary_25.gensim')
# save LDA model
lda_model.save('model_25.gensim')
