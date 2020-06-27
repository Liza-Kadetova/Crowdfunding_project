#!/usr/bin/env python
# coding: utf-8

# In[59]:


import pandas as pd
import re
from string import digits
import pymorphy2
from nltk.corpus import stopwords
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report


# In[37]:


df = pd.read_csv("/Users/liza/PycharmProjects/Planeta_project/plset_fin_upd_clustered.tsv", sep ="\t")
df = df.drop(df.columns[0:2], axis=1)
df = df.rename_axis(None, axis=1).rename_axis('Id', axis=1)


# In[57]:


# Создаем кастомизированный токенизатор, который можно вставить в Pipeline
class Prep(BaseEstimator, TransformerMixin):

    def __init__(self):
        self.morph_analyzer = pymorphy2.MorphAnalyzer()
        self.stop_words = stopwords.words('russian')
        self.stop_words.extend(['это', '–', '-', 'фонд', 'наш', 'помощь', 'помогать',
                   'помочь', 'поддержать', 'поддержка', 'средство', 'который', 'весь',
                   'благотворительный', 'деньги', 'рубль', 'год', 'день', 'тысяча',
                   'ваш', 'сегодня', 'завтра', 'этот', 'дать', 'проект', 'свой' ])

    def prep(self, text):
        clean_text = text.translate(str.maketrans('', '', '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~«»№!—'))
        clean_text = clean_text.translate(str.maketrans('', '', digits))
        clean_text = re.sub("-", " ", clean_text)
        # clean_text = re.sub("[a-zA-Z]", "", clean_text)  # исключаем слова латиницей
        clean_text = clean_text.lower()
        clean_text = clean_text.split()
        

        # words = [word for word in clean_text if word not in self.stop_words]
        # return words

        lemmas = [self.morph_analyzer.parse(word)[0].normal_form for word in clean_text]
        lemmas = [word for word in lemmas if word not in self.stop_words]
        return ' '.join(lemmas)

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X = X.map(self.prep)

        return X
        print(X)

# Укладываем все три процесса работы над текстом в пайп
pipe = Pipeline([
    ('tokenizer', Prep()),
    ('vectorizer', CountVectorizer()),
    ('classifier', LogisticRegression(max_iter=5000))
    ]
    )

# Делим исходные данные
X_train, X_test, y_train, y_test = train_test_split(df.Description,
                                                    df.Category,
                                                    stratify=df.Category)
# Обучаем пайп как обычный классификатор
pipe.fit(X_train, y_train)

# Дальше предсказывать, оценивать и  сохранять


# In[60]:


print(classification_report(y_test, pipe.predict(X_test), zero_division=0))

