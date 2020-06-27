from time import strptime

import pandas as pd
import re
import nltk
from nltk.tokenize import sent_tokenize
import datetime as dt
from datetime import date
from datetime import timedelta
import string
from string import digits
import pymorphy2
import nltk
from nltk import word_tokenize
morph_analyzer = pymorphy2.MorphAnalyzer()
pd.options.display.max_columns = 15

from nltk.corpus import stopwords
stop_words = stopwords.words('russian')
stop_words.extend(['это', '–'])
print(stop_words)

df = pd.read_csv('plset_fin.tsv', encoding="utf-8", header=0, sep ="\t")
df.info()
#df = df.fillna("NaN") #проставили nan во всех пустых ячейках (иначе na считается float, c которым потом не работают строковые методы)
#df.info()
#df = df.drop_duplicates(subset="Description", keep="first")
#df.info()
df = df.drop(df.columns[0], axis=1)  # выбросили колонку с индексами, чтобы не дублировалась при записи нового файла


df["Result"] = df["Result"].str.replace('\D', '') #убираем пробелы и буквы из колонок с цифрами
df["Goal"] = df["Goal"].str.replace('\D', '')
df["Donations"] = df["Donations"].str.replace('\D', '')
#df.info()

def date_change(str):
    cal = {"января": "Jan", "февраля": "Feb", "марта": "Mar", "апреля": "Apr",
           "мая": "May", "июня": "Jun", "июля": "Jul", "августа": "Aug", "сентября": "Sep",
           "октября": "Oct", "ноября": "Nov", "декабря": "Dec"}
    for k, v in cal.items():
        str = re.sub(k, v, str)
    return str

def text_length(text):
    text = text.translate(str.maketrans('', '', '\n!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~«»!—№ '))
    #print(text)
    return(len(text)) #без проблелов, пунктуации, переносов строки

def words_used(text):
    text = text.split() #все словоупотребления, слова через дефис считаются как одно, числа считаются как слова
    return(len(text))

def num_sent(text):
    #print(text)
    text = re.sub(r"\d+\.+\d|([A-Za-z]|\d)\.(\d|[A-Za-z])|\(\!\)|[А-Я]\.[А-Я]\.", "YYY", text) #убираем числа с точкой, веб-ссылки, (!), инициалы
    text = re.sub(r"\!\.+|\?\.+|\?{1,}|\!{1,}|\?\!|\!\?|\.{2,}", "\. ", text) #!, ? и двойные знаки преп. заменяем одной точкой
    reduced = open("reduct_per.txt", "r") #файл с сокращениями
    reduced = reduced.read()
    stops_mid = re.split(r"\*", reduced)  #разбиваем сокращения на список по разделителю *
    stops_end = [" т.п.", " т. п.", " т.д.", " т. д.", "др.",
                 "руб."]  # созд. отд. спис., т.к. из основного по паттерну тащит сокр. типа "пос. Юкки" в сер. предл.
    for i in stops_end:
        text = re.sub(r'{}\s[А-Я]'.format(re.escape(i)), " XXX.", text) #концевые сокр. превращаем в одну точку
    for i in stops_mid:
        text = text.replace(i, " XXX") #убираем сокращения в середине предл.
    #print(text)
    text = re.split("\.\s+[А-Я]|\n", text) #разбиваем текст по точке+пробел+большая буква или по переносу строки, получаем список из предложений
    #print(text)
    return(len(text)) #считаем длину списка

def num_sent_nltk(text):
    text = sent_tokenize(text)
    return(len(text))

def text_prep(text):
    clean_text = text.translate(str.maketrans('', '', '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~«»№!—'))
    clean_text = clean_text.translate(str.maketrans('', '', digits))
    clean_text = re.sub("-", " ", clean_text)
    clean_text = re.sub("NaN", "", clean_text)
    clean_text = re.sub("[a-zA-Z]", "", clean_text) #исключаем слова латиницей
    clean_text = clean_text.lower()
    clean_text = clean_text.split()
    clean_words = [word for word in clean_text if word not in stop_words]
    lemmas = [morph_analyzer.parse(word)[0].normal_form for word in clean_words]
    return lemmas

len_sg = []
len_wd = []
len_st = []
len_st_n = []
started = []
finished = []
brief = []

for br in df["Briefly"]:
    br = text_prep(br)
    brief.append([l for l in br])

for descr in df["Description"]:
    signs = text_length(descr)
    len_sg.append(signs)
    words = words_used(descr)
    len_wd.append(words)
    sents = num_sent(descr)
    len_st.append(sents)
    sentsn = num_sent_nltk(descr)
    len_st_n.append(sentsn)

for date in df["Start"]: #ВАЖНО! Специально старт и финиш наборот, т.к. изначально при сборе спутаны ОТМЕНЕНО
    date = date_change(date)
    started.append(date)

for date in df["Finish"]:
    date = date_change(date)
    finished.append(date)

df = df.assign(LengthZn=len_sg)
df = df.assign(LengthWd=len_wd)
df = df.assign(NumSent=len_st)
df = df.assign(NumSentNLTK=len_st_n)
df = df.assign(Started = started)
df = df.assign(Finished = finished)
#df = df.drop(df.columns[6], axis=1) #удаляем старый старт и финиш, индексы одинаковые с учетом смещения нумерация после выполнения первого удаления
#df = df.drop(df.columns[6], axis=1)
df = df.assign(LeadBag = brief)
df['DaysLong'] = (pd.to_datetime(df['Started'], errors='coerce') - pd.to_datetime(df['Finished'], errors='coerce')).dt.days
df['DaysLong'] = df['DaysLong'].fillna(0.0).astype(int).abs() #Na зам. на числа, берем целые, без минусов (абс. знач.)
df = df.to_csv("plset_fin_upd.csv")
df = pd.read_csv('plset_fin_upd.csv', encoding="utf-8", sep=",")


print(df.head(7))
#print(df.iloc[785])
