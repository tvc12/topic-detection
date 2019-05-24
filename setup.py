
import setuptools

setuptools.setup(
    name="topic_detect",
    version="0.0.1",
    author="Vi-Chi-Thien",
    author_email="meomeocf98@gmail.com",
    description="Project for topic dectection",
    install_requires=[
        'python-crfsuite>=0.9.5',
        'sklearn-crfsuite>=0.3.6',
        'joblib>=0.12.5',
        'gensim>=3.5.0',
        'tensorflow>=1.8.0',
        'keras>=2.2.0'
    ],
    url="https://github.com/tvc12/topic-detection",
    packages=setuptools.find_packages(),
    package_data={'topic_detect': ['topic-detection/*']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0",
        "Operating System :: OS Independent",
    ],
)
