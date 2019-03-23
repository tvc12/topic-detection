#from deepai_nlp.wikicrawler.wiki_bs4 import WikiTextCrawler
#from deepai_nlp.tokenization.crf_tokenizer import CrfTokenizer
#from deepai_nlp.tokenization.utils import preprocess_text
from deepai_nlp.word_embedding import word2vec_gensim
from gensim.models import KeyedVectors
#crawler = WikiTextCrawler() #Khởi tạo object
#keywords = ['chó', 'mèo', 'gà', 'chuột', 'dán', 'hổ', 'xe', 'người', 'động vật'
#            ,'táo', 'dữ liệu', "Trái cây", "quả đu đủ", "cóc", "hiếp dâm", "tội phạm", "Đi tù", "nghỉ dưỡng",
#		"chính sách", "tha hoá", "chủ nghĩa", "đạo đức", "pháp luật", "trí tưởng tượng", "siêu anh hùng"]
#url_list = []
#
##Tìm kiếm links bài viết từ keyword
#for kw in keywords: 
#    urls = crawler.search(kw)
#    url_list += urls
##Crawl bài viết về thành file text
#for url in url_list:
#    crawler.write_text(output_file='data.txt', url=url, mode='a')
#    
#with open('data.txt', 'r') as f:
#    document = f.readlines()
#print("Tranning")
#tokenizer = CrfTokenizer()
#documents = preprocess_text(document, tokenizer=tokenizer) # Tách từ và clean
#model = word2vec_gensim.Word2Vec (documents, size=100, window=5, min_count=5, workers=1, sg=1)
#model.train(documents,total_examples=len(documents),epochs=10)
#wv_path = "word2vec.model"
#model.wv.save(wv_path)
#
#print("Done")

wv_path = "word2vec.model"
model = KeyedVectors.load(wv_path)
#vector = model.wv['mèo']
#print(model.match(w1="táo",w2="quả_táo"))
#sim_words = model.wv.most_similar('chó')
#print(sim_words)
