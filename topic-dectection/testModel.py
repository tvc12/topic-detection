from deepai_nlp.tokenization.crf_tokenizer import CrfTokenizer
from prepare import preprocess_text
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
num_topic = 15
max_files = len(files)



def read_data(dir, files, rate_read):
    i = 0
    id = []
    data = []
    for path in files:
        print('Load file', path)
        with open(dir + path, 'r') as file:
            data.append(file.read())
            file.close()

        files.remove(path)
        id.append(path)
        # break
        if (i / max_files > rate_read):
            break
        else:
            i = i + 1
    return id, preprocess_text(data, tokenizer)


dictionary = gensim.corpora.Dictionary.load(f'dictionary_{num_topic}.gensim')
corpus = pickle.load(open(f'corpus_{num_topic}.pkl', 'rb'))
lda_model = gensim.models.ldamodel.LdaModel.load(f'model_{num_topic}.gensim')

# dictionary.compactify()

# for idx, topic in lda_model.print_topics(-1):
#     print("Topic: {} \nWords: {}".format(idx, topic))
#     print("\n")

id, test_data = read_data(dir, files, 0.01)

test_corpus = [dictionary.doc2bow(doc) for doc in test_data]


document_dist = np.array(
[print(tup) for tup in lda_model.get_document_topics(bow=test_corpus)]
)

# print(document_dist)

# print(get_most_similar_documents(lda_model, corpus, document_dist))


#test_dictionary = corpora.Dictionary(test_data)


# for test in test_data:
#     bow_vector = dictionary.doc2bow(test)
#     for index, score in sorted(lda_model[bow_vector],
#                                key=lambda tup: -1 * tup[1]):
#         print("Score: {}\t Topic: {} {}".format(score, index,
#                                                 lda_model.print_topic(index)))
