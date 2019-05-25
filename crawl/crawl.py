from get_links import get_urls_new
from get_content import get_content
from save_file import save_content
from const import *
import os


def crawl_giaitri(num=5000, path='data/giaitri/', header_name='giaitri_'):
    urls = get_urls_new(VNEXPRESS_GIAITRI,  num)
    import os
    if not os.path.exists(path):
        os.makedirs(path)
    for url in urls:
        new = get_content(url)
        if new != '':
            print("Write url: {}".format(url))
            save_content(path, header_name, new)


def crawl_thegioi(num=5000, path='data/thegioi/', header_name='thegioi_'):
    urls = get_urls_new(VNEXPRESS_THEGIOI,  num)
    if not os.path.exists(path):
        os.makedirs(path)
    for url in urls:
        new = get_content(url)
        if new != '':
            print("Write url: {}".format(url))
            save_content(path, header_name, new)

def crawl_thoisu(num=5000, path='data/thoisu/', header_name='thoisu_'):
    if not os.path.exists(path):
        os.makedirs(path)
    urls = get_urls_new(VNEXPRESS_THOISU,  num)
    for url in urls:
        new = get_content(url)
        if new != '':
            print("Write url: {}".format(url))
            save_content(path, header_name, new)

def crawl_tamsu(num=5000, path='data/tamsu/', header_name='tamsu_'):
    if not os.path.exists(path):
        os.makedirs(path)
    urls = get_urls_new(VNEXPRESS_TAMSU,  num)
    for url in urls:
        new = get_content(url)
        if new != '':
            print("Write url: {}".format(url))
            save_content(path, header_name, new)

def crawl_thethao(num=5000, path='data/thethao/', header_name='thethao_'):
    if not os.path.exists(path):
        os.makedirs(path)
    urls = get_urls_new(VNEXPRESS_THETHAO,  num)
    for url in urls:
        new = get_content(url)
        if new != '':
            print("Write url: {}".format(url))
            save_content(path, header_name, new)

def crawl_phapluat(num=5000, path='data/phapluat/', header_name='phapluat_'):
    if not os.path.exists(path):
        os.makedirs(path)
    urls = get_urls_new(VNEXPRESS_PHAPLUAT,  num)
    for url in urls:
        new = get_content(url)
        if new != '':
            print("Write url: {}".format(url))
            save_content(path, header_name, new)