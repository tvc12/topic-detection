from deepai_nlp.tokenization.crf_tokenizer import CrfTokenizer
from deepai_nlp.tokenization.utils import preprocess_text
from deepai_nlp.word_embedding import word2vec_gensim
from distances import get_most_similar_documents
from gensim import corpora
import gensim
import os
import numpy
import pickle
import numpy as np


tokenizer = CrfTokenizer()
dir = 'test/'
path, dirs, files = next(os.walk(dir))

max_files = len(files)


def prepare_data(data, tokenizer):
    data = preprocess_text(data, tokenizer=tokenizer)
    return list(numpy.concatenate(data, axis=0))


def read_data(dir, files, rate_read):
    i = 0
    text_data = []
    for path in files:
        print('Load file', path)
        data = []
        with open(dir + path, 'r') as file:
            data = file.readlines()
            file.close()
        text_data.append(prepare_data(data, tokenizer))
        if (i / max_files > rate_read):
            break
        else:
            i = i + 1
        files.remove(path)
    return text_data


dictionary = gensim.corpora.Dictionary.load('dictionary_25.gensim')
corpus = pickle.load(open('corpus_25.pkl', 'rb'))
lda_model = gensim.models.ldamodel.LdaModel.load('model_25.gensim')


# for idx, topic in lda_model.print_topics(-1):
#     print("Topic: {} \nWords: {}".format(idx, topic))
#     print("\n")
for idx, topic in lda_model.print_topics(-1):
    print("Topic: {} \nWords: {}".format(idx, topic))
    print("\n")

test_data = read_data(dir, files, 0.05)

test_dictionary = corpora.Dictionary(test_data)

# for test in test_data:
#     bow_vector=test_dictionary.doc2bow(test)
#     document_dist = np.array(
#         [tup[1] for tup in lda_model.get_document_topics(bow=bow_vector)]
#     )
#     print(get_most_similar_documents(lda_model, corpus, document_dist))

for test in test_data:
    bow_vector=test_dictionary.doc2bow(test)
    for index, score in sorted(lda_model[bow_vector],
                               key=lambda tup: -1 * tup[1]):
        print("Score: {}\t Topic: {}".format(score,
                                             lda_model.print_topic(index)))
