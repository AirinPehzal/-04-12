import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
download_stopwords = stopwords.words('russian')
stop_text = []
text='Думаешь, что гуманитарии «не умеют» в экономику? У них никогда не получится построить бизнес просто потому, что они не знают, как считать деньги? Кафедра русского языка спешит разрушить эти мифы!'
textnew=open("textnew.txt","w")
tokens = word_tokenize(text)    #токенизация
for i in tokens:
    if i not in download_stopwords:
        stop_text.append(i)

stems = []
stemmer = SnowballStemmer("russian")
for token in tokens:
    token = stemmer.stem(token)
    if token != "":
        stems.append(token)

for i in tokens:
    textnew.write(str(i))
    textnew.write('  ')
textnew.write('\n')
for i in stop_text:
    textnew.write(str(i))
    textnew.write('  ')
textnew.write('\n')
for i, j in zip(tokens, stems):
        textnew.write(str(i))
        textnew.write(':')
        textnew.write(str(j))
        textnew.write('   ')
textnew.write('\n')
textnew.write(str(len(tokens)))
textnew.write('\n')
textnew.write(str(len(tokens)-len(stop_text)))
textnew.write('\n')
textnew.write(str(((len(tokens)-len(stop_text))/len(tokens))*100))
textnew.write('\n')
