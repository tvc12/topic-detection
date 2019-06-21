## topic-detection

![GitHub](https://img.shields.io/github/license/tvc12/topic-detection.svg)

### Installation

**Step 1:**
Install deepai_nlp package:

```bash
git clone https://github.com/deepai-solutions/deepai_nlp.git
cd deepai_nlp
pip install -e .
## or 
pip3 install -e .

pip install matplotlib
## or
pip3 install matplotlib
```

**Step 2:**
Install **gensim (Option)** 

```bash
conda install -c anaconda gensim
## or
pip install gensim
```

**Step 3:**
Clone this project to your local:

```bash
git clone https://github.com/tvc12/topic-detection
cd topic-detection
```

### Usage

**Crawler:** crawl data from [vnexpress](https://vnexpress.net/)

```bash
cd crawl
```

Import package:

```python
from crawl import *
```

There are list method for crawl data.

| Name           | Description                                                  | Parameter                                   |
| -------------- | ------------------------------------------------------------ | ------------------------------------------- |
| crawl_giaitri  | Crawl data from [giai tri](https://vnexpress.net/giai-tri)   | **num**: is number topics will download     |
| crawl_giaoduc  | Crawl data from [giao duc](https://vnexpress.net/giao-duc)   | **path**: is location save file             |
| crawl_thoisu   | Crawl data from [thoi su](https://vnexpress.net/thoi-su)     | **header_name**: is leading name file crawl |
| crawl_phapluat | Crawl data from [phap luat](https://vnexpress.net/phap-luat) |                                             |
| crawl_thegioi  | Crawl data from [the gioi](https://vnexpress.net/the-gioi)   |                                             |
| crawl_thethao  | Crawl data from [the thao](https://vnexpress.net/the-thao)   |                                             |

**Topic detection**

```bash
cd topic-detection
```

Extra file _data.zip_:

```bash
unzip data.zip
```

**Data struct**:

| Topic     | Number | Date                 |
| --------- | ------ | -------------------- |
| Giao Duc  | 7483   | 1/1/2019 - 21/5/2019 |
| Phap Luat | 9797   | 1/1/2019 - 21/5/2019 |
| Tam Su    | 8471   | 1/1/2019 - 21/5/2019 |
| The Thao  | 5499   | 1/1/2019 - 21/5/2019 |
| Thoi su   | 6377   | 1/1/2019 - 21/5/2019 |

- Training project with first model. You must set **num_topics** at lines 60 on file `firstModel.py` then run this file.

```bash
python firstModel.py
```

- Training project with best model.

```bash
python best_model.py
```

With both training, you will receive some files model. Use it see [there](https://github.com/cuongw/article-topic)

### Contributors

| [![Vi Chi Thien](https://github.com/tvc12.png?size=100)](https://github.com/tvc12) |
| :--------------------------------------------------------------------------------: |
|                      [Vi Chi Thien](https://github.com/tvc12)                      |

### License

This project is licenced under the [Apache 2.0](https://github.com/tvc12/topic-detection/blob/master/LICENSE)
